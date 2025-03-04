#!/bin/bash

PYTHON_SCRIPT1="/home/kartuser/SAE_kart/centralisation_interface/main.py"
PYTHON_SCRIPT2="/home/kartuser/SAE_kart/BMS/testBMS.py"
PYTHON_SCRIPT3="/home/kartuser/SAE_kart/gestion_gpio/gestion_boutons/gestion_boutons.py"
PYTHON_SCRIPT6="/home/kartuser/KARTSERIAL"
PYTHON_SCRIPT7="/home/kartuser/SAE_kart/GPS/testGPS5.py"

# Lancer les scripts en arrière-plan avec nohup
nohup python3 "$PYTHON_SCRIPT2" > /dev/null 2>&1 &
nohup python3 "$PYTHON_SCRIPT3" > /dev/null 2>&1 &
nohup "$PYTHON_SCRIPT6" > /dev/null 2>&1 &
nohup python3 "$PYTHON_SCRIPT7" > /dev/null 2>&1 &

# Attendre un peu pour éviter que xinit démarre trop tôt
sleep 2

# Lancer l’interface graphique
xinit /bin/bash -c "python3 '$PYTHON_SCRIPT1'; pkill X" -- :0 &
wait