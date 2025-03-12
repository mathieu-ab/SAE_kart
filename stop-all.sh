#!/bin/bash

# Arrêter le service via systemctl
echo "Arrêt du service kart..."
sudo systemctl stop kart.service

# Vérifier si le service est toujours en cours d'exécution
if systemctl is-active --quiet kart.service; then
    echo "Forçage de l'arrêt de kart..."
    sudo systemctl kill kart.service
else
    echo "kart est arrêté."
fi

# Liste des scripts à arrêter
SCRIPTS=(
    "main.py"
    "testBMS.py"
    "gestion_boutons.py"
    "KARTSERIAL"
    "testGPS5.py"
    "visualise.py"
    "test.py"
)

# Arrêter le serveur X
x_pid=$(pgrep -f "xinit")
if [ -n "$x_pid" ]; then
    echo "Arrêt du serveur X (PID: $x_pid)..."
    kill $x_pid
    sleep 1  
    if pgrep -f "xinit" > /dev/null; then
        echo "Forçage de l'arrêt du serveur X..."
        kill -9 $(pgrep -f "xinit")
    fi
fi

# Arrêter tous les autres scripts
for script in "${SCRIPTS[@]}"; do
    pids=$(pgrep -f "$script")
    if [ -n "$pids" ]; then
        echo "Arrêt de $script (PID: $pids)..."
        kill $pids
        sleep 1  
        if pgrep -f "$script" > /dev/null; then
            echo "Forçage de l'arrêt de $script..."
            kill -9 $(pgrep -f "$script")
        fi
    else
        echo "$script n'est pas en cours d'exécution."
    fi
done

echo "Tous les processus ont été arrêtés."
