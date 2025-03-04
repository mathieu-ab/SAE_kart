#!/bin/bash

PYTHON_SCRIPT1="/home/kartuser/SAE_kart/centralisation_interface/main.py"
PYTHON_SCRIPT2="/home/kartuser/SAE_kart/BMS/testBMS.py"
PYTHON_SCRIPT3="/home/kartuser/SAE_kart/gestion_gpio/gestion_boutons/gestion_boutons.py"
SCRIPT6="/home/kartuser/KARTSERIAL"
PYTHON_SCRIPT7="/home/kartuser/SAE_kart/GPS/testGPS5.py"

# Lancer les scripts en arrière-plan avec nohup
python3 "$PYTHON_SCRIPT2" &
python3 "$PYTHON_SCRIPT3" &
"$SCRIPT6" &
python3 "$PYTHON_SCRIPT7" &

# Attendre un peu pour éviter que xinit démarre trop tôt
sleep 2

# Lancer l’interface graphique
xinit /bin/bash -c "python3 '$PYTHON_SCRIPT1'; pkill X" -- :0 &
wait