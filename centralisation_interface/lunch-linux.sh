#!/bin/bash

# Chemin vers le script Python
PYTHON_SCRIPT="interface_central.py"

# Lancer X avec le script Python
xinit python3 "$PYTHON_SCRIPT" -- :0

# Une fois que le script Python se termine, arrêter X
pkill X
