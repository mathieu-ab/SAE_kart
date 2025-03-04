#!/bin/bash

# Liste des processus à arrêter (noms des scripts)
SCRIPTS=(
    "main.py"
    "testBMS.py"
    "gestion_boutons.py"
    "KARTSERIAL"
    "testGPS5.py"
)

echo "Arrêt définitif des processus..."

# Tuer tous les processus liés aux scripts
for script in "${SCRIPTS[@]}"; do
    pids=$(pgrep -f "$script")
    if [ -n "$pids" ]; then
        echo "Arrêt de $script (PID: $pids)..."
        kill $pids
        sleep 1
        pids_restants=$(pgrep -f "$script")
        if [ -n "$pids_restants" ]; then
            echo "Forçage de l'arrêt de $script..."
            kill -9 $pids_restants
        fi
    else
        echo "$script n'est pas en cours d'exécution."
    fi
done

# Arrêter le serveur X s'il a été démarré par xinit
x_pid=$(pgrep -f "Xorg|X")
if [ -n "$x_pid" ]; then
    echo "Arrêt du serveur X (PID: $x_pid)..."
    kill $x_pid
    sleep 1
    x_pid_restant=$(pgrep -f "Xorg|X")
    if [ -n "$x_pid_restant" ]; then
        echo "Forçage de l'arrêt du serveur X..."
        kill -9 $x_pid_restant
    fi
else
    echo "Le serveur X n'est pas en cours d'exécution."
fi

echo "Tous les processus ont été arrêtés définitivement."
