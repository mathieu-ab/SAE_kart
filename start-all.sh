#!/bin/bash


# Déclaration des scripts à exécuter
SCRIPTS=(
    "/home/kartuser/SAE_kart/BMS/testBMS.py"
    "/home/kartuser/SAE_kart/gestion_gpio/gestion_boutons/gestion_boutons.py"
    "/home/kartuser/SAE_kart/KARTSERIAL"
    "/home/kartuser/SAE_kart/GPS/testGPS5.py"
    "/home/kartuser/SAE_kart/Navion/visualise.py"
    "/home/kartuser/SAE_kart/endormissement/endormissement.py"
)

MAIN_SCRIPT="/home/kartuser/SAE_kart/centralisation_interface/main.py"

declare -A PIDS  # Tableau associatif pour stocker les PIDs

echo "Démarrage des scripts..."

# Démarrer main.py une seule fois avec xinit
start_main() {
    echo "Démarrage de main.py avec xinit..."
    xinit /usr/bin/python3 "$MAIN_SCRIPT" -- :0 &
    PIDS[$MAIN_SCRIPT]=$!
}

# Fonction pour démarrer un script et stocker son PID
start_script() {
    local script="$1"
    echo "Démarrage de $script..."

    if [[ "$script" == *.py ]]; then
        python3 "$script" &  
    else
        "$script" &  
    fi
    
    PIDS[$script]=$!  # Stocker le PID du processus
}

# Démarrer main.py une seule fois
start_main

# Démarrer les autres scripts
for script in "${SCRIPTS[@]}"; do
    start_script "$script"
done

# Surveillance et redémarrage des scripts (sauf main.py) s'ils s'arrêtent
while true; do
    sleep 5  # Attendre 5 secondes entre chaque vérification

    for script in "${!PIDS[@]}"; do
        pid=${PIDS[$script]}
        if ! kill -0 $pid 2>/dev/null; then  
            if [[ "$script" == "$MAIN_SCRIPT" ]]; then
                echo "main.py s'est arrêté, mais ne sera pas redémarré."
            else
                echo "Attention : $script s'est arrêté ! Redémarrage..."
                start_script "$script"
            fi
        fi
    done
done
