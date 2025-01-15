#!/bin/bash

# Chemin vers le premier script Python
PYTHON_SCRIPT1="/home/kartuser/SAE_kart/centralisation_interface/interface_central.py"

# Chemin vers le deuxième script Python
PYTHON_SCRIPT2="/home/kartuser/BMS/BMS_lireSOC.py"

# Fonction pour lancer le premier script avec X
start_script1() {
    echo "Lancement du script 1 avec X..."
    xinit /bin/bash -c "python3 '$PYTHON_SCRIPT1'; pkill X" -- :0 &
    PID1=$!  # Sauvegarder le PID du processus
}

# Fonction pour lancer le deuxième script dans une boucle infinie
start_script2() {
    echo "Lancement du script 2 dans une boucle infinie..."
    while true; do
        python3 "$PYTHON_SCRIPT2"
        sleep 10
    done &
    PID2=$!  # Sauvegarder le PID du processus
}

# Lancer les deux scripts
start_script1
start_script2

# Attendre que l'un des scripts se termine (facultatif)
wait $PID1 $PID2

# Message de confirmation lorsque les deux scripts sont arrêtés
echo "Les deux scripts sont terminés."
