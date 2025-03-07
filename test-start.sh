#!/bin/bash




MAIN_SCRIPT="/home/kartuser/SAE_kart/centralisation_interface/main.py"



echo "Démarrage des scripts..."


# Démarrer main.py une seule fois
xinit /usr/bin/python3 "$MAIN_SCRIPT" -- :0 &
python3 "/home/kartuser/SAE_kart/Navion/visualise.py"
