#!/bin/bash

# Chemins vers les scripts Python
PYTHON_SCRIPT1="/home/kartuser/SAE_kart/centralisation_interface/interface_central.py"
PYTHON_SCRIPT2="/home/kartuser/BMS/test.py"
PYTHON_SCRIPT3="/home/kartuser/SAE_kart/gestion_gpio/gestion_boutons/gestion_boutons.py"


# Lancer le deuxième script Python en arrière-plan et capturer son PID
python3 "$PYTHON_SCRIPT2" &
python3 "$PYTHON_SCRIPT3" &
SCRIPT2_PID=$!
SCRIPT3_PID=$!



# Lancer le premier script avec X et attendre qu'il se termine
xinit /bin/bash -c "python3 '$PYTHON_SCRIPT1'; pkill X" -- :0
wait # Cette commande attend la fin du processus `xinit`

# Une fois que le script 1 se termine, arrêter le script 2
kill $SCRIPT2_PID
kill $SCRIPT3_PID
