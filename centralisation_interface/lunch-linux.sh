#!/bin/bash

# Chemin vers les scripts Python
PYTHON_SCRIPT1="/home/kartuser/SAE_kart/centralisation_interface/interface_central.py"
PYTHON_SCRIPT2="/home/kartuser/BMS/BMS_lireSOC.py"

# Lancer le premier script avec X
xinit /bin/bash -c "python3 '$PYTHON_SCRIPT1'; pkill X" -- :0 &

# Lancer le deuxième script Python en arrière-plan
python3 "$PYTHON_SCRIPT2" &
