#!/bin/bash

# Chemin vers le script Python
PYTHON_SCRIPT="/home/SAE_kart/centralisation_interface/interface_central.py"

# Lancer X et attendre la fin du script Python
xinit /bin/bash -c "python3 '$PYTHON_SCRIPT'" -- :0

# Attendre un instant pour s'assurer que X est arrêté proprement
sleep 1