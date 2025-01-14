#!/bin/bash

# Chemin vers le script Python
PYTHON_SCRIPT="/home/user/SAE_kart/centralisation_interface/interface_central.py"


# Lancer X et exécuter le script Python
xinit /bin/bash -c "python3 '$PYTHON_SCRIPT'; pkill X" -- :0

# Attendre un instant pour s'assurer que X se ferme correctement
sleep 1

# Message de confirmation
echo "Le script s'est terminé