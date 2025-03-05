#!/bin/bash

# Liste des processus à arrêter (noms des scripts)
SCRIPTS=(
    "testBMS.py"
    "gestion_boutons.py"
    "KARTSERIAL"
    "testGPS5.py"
)

MAIN_SCRIPT="main.py"

SCRIPT_START="/tmp/start-all.pid"

echo "Arrêt définitif des processus..."

# Arrêter le serveur X s'il a été démarré par xinit
x_pid=$(pgrep -f "xinit")
if [ -n "$x_pid" ]; then
    echo "Arrêt du serveur X (PID: $x_pid)..."
    kill $x_pid
    sleep 1  
    x_pid_restant=$(pgrep -f "xinit")
    if [ -n "$x_pid_restant" ]; then
        echo "Forçage de l'arrêt du serveur X..."
        kill -9 $x_pid_restant
    fi
else
    echo "Le serveur X n'est pas en cours d'exécution."
fi

# Tuer main.py
pids=$(pgrep -f "$MAIN_SCRIPT")
if [ -n "$pids" ]; then
    echo "Arrêt de main.py (PID: $pids)..."
    kill $pids
    sleep 1  
    pids_restants=$(pgrep -f "$MAIN_SCRIPT")
    if [ -n "$pids_restants" ]; then
        echo "Forçage de l'arrêt de main.py..."
        kill -9 $pids_restants
    fi
fi

# Vérifier si le fichier PID existe
if [ -f "$SCRIPT_START" ]; then
    pids=$(cat "$SCRIPT_START")
    if [ -n "$pids" ]; then
        echo "Arrêt de start-all.sh (PID: $pids)..."
        kill $pids
        sleep 1  
        pids_restants=$(pgrep -f "start-all.sh")
        if [ -n "$pids_restants" ]; then
            echo "Forçage de l'arrêt de start-all.sh..."
            kill -9 $pids_restants
        fi
    fi
    rm "$SCRIPT_START"  # Nettoyage du fichier PID
else
    echo "start-all.sh n'est pas en cours d'exécution."
fi

# Tuer tous les autres scripts
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

echo "Tous les processus ont été arrêtés définitivement."
