#!/bin/bash

# Chemins vers les scripts Python
PYTHON_SCRIPT1="/home/kartuser/SAE_kart/centralisation_interface/interface_central.py"
PYTHON_SCRIPT2="/home/kartuser/BMS/test.py"

# Lancer le deuxième script Python en arrière-plan et capturer son PID
python3 "$PYTHON_SCRIPT2" &
SCRIPT2_PID=$!

# Lancer le premier script avec X
xinit /bin/bash -c "python3 '$PYTHON_SCRIPT1'; pkill X" -- :0

# Une fois que le script 1 se termine, arrêter le script 2
kill $SCRIPT2_PID
