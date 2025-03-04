#!/bin/bash

# Chemins vers les scripts Python
PYTHON_SCRIPT1="/home/kartuser/SAE_kart/centralisation_interface/main.py"
PYTHON_SCRIPT2="/home/kartuser/SAE_kart/BMS/testBMS.py"
PYTHON_SCRIPT3="/home/kartuser/SAE_kart/gestion_gpio/gestion_boutons/gestion_boutons.py"
PYTHON_SCRIPT4="/home/kartuser/SAE_kart/gestion_gpio/gestion_charge/gestion_charge.py"
PYTHON_SCRIPT5="/home/kartuser/SAE_kart/connection_wifi/connect_wifi.py"
SCRIPT6="/home/kartuser/KARTSERIAL"
PYTHON_SCRIPT7="/home/kartuser/SAE_kart/GPS/testGPS5.py"


# Lancer les scripts Python en arrière-plan et capturer leurs PID
python3 "$PYTHON_SCRIPT2" &
SCRIPT2_PID=$!

python3 "$PYTHON_SCRIPT3" &
SCRIPT3_PID=$!

# python3 "$PYTHON_SCRIPT4" &
# SCRIPT4_PID=$!

# python3 "$PYTHON_SCRIPT5" &
# SCRIPT5_PID=$!

"$SCRIPT6" &
SCRIPT6_PID=$!

python3 "$PYTHON_SCRIPT7" &
SCRIPT7_PID=$!

echo "Scripts lancés avec les PID :"
echo "Script 2 PID: $SCRIPT2_PID"
echo "Script 3 PID: $SCRIPT3_PID"
# echo "Script 4 PID: $SCRIPT4_PID"
# echo "Script 5 PID: $SCRIPT5_PID"
echo "Script 6 PID: $SCRIPT6_PID"
echo "Script 7 PID: $SCRIPT7_PID"

# Lancer le premier script avec X et attendre qu'il se termine
xinit /bin/bash -c "python3 '$PYTHON_SCRIPT1'; pkill X" -- :0
wait # Attendre la fin du processus `xinit`

# Une fois que le script 1 se termine, arrêter les autres scripts
echo "Arrêt des scripts en arrière-plan..."
kill $SCRIPT2_PID 2>/dev/null
kill $SCRIPT3_PID 2>/dev/null
# kill $SCRIPT4_PID 2>/dev/null
# kill $SCRIPT5_PID 2>/dev/null
kill $SCRIPT6_PID 2>/dev/null
kill $SCRIPT7_PID 2>/dev/null
echo "Scripts arrêtés."

# Nettoyer les processus orphelins si nécessaire
pkill -f "$PYTHON_SCRIPT2"
pkill -f "$PYTHON_SCRIPT3"
pkill -f "$PYTHON_SCRIPT4"
pkill -f "$PYTHON_SCRIPT5"
pkill -f "$SCRIPT6"
pkill -f "$PYTHON_SCRIPT7"
echo "Nettoyage terminé."
