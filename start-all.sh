#!/bin/bash

# Déclaration des scripts à exécuter
SCRIPTS=(
    "/home/kartuser/SAE_kart/centralisation_interface/main.py"
    "/home/kartuser/SAE_kart/BMS/testBMS.py"
    "/home/kartuser/SAE_kart/gestion_gpio/gestion_boutons/gestion_boutons.py"
    "/home/kartuser/KARTSERIAL"
    "/home/kartuser/SAE_kart/GPS/testGPS5.py"
)

declare -A PIDS  # Tableau associatif pour stocker les PIDs

echo "Démarrage des scripts..."

# Fonction pour démarrer un script et stocker son PID
start_script() {
    local script="$1"
    echo "Démarrage de $script..."
    $script &  # Lance le script en arrière-plan
    PIDS[$script]=$!  # Stocke le PID du processus
}

# Démarrer tous les scripts
for script in "${SCRIPTS[@]}"; do
    start_script "$script"
done

# Surveillance et redémarrage des scripts s'ils s'arrêtent
while true; do
    sleep 3  # Attendre 3 secondes entre chaque vérification

    for script in "${!PIDS[@]}"; do
        pid=${PIDS[$script]}
        if ! kill -0 $pid 2>/dev/null; then  # Vérifie si le processus existe encore
            echo "Attention : $script s'est arrêté ! Redémarrage..."
            start_script "$script"
        fi
    done
done
