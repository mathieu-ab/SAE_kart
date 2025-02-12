import subprocess

# Scanner les réseaux WiFi disponibles
def scan_wifi():
    result = subprocess.run(["nmcli", "-t", "-f", "SSID", "dev", "wifi"], capture_output=True, text=True)
    networks = result.stdout.strip().split("\n")
    return networks

# Se connecter à un réseau WiFi
def connect_wifi(ssid, password):
    subprocess.run(["nmcli", "dev", "wifi", "connect", ssid, "password", password])

# Afficher les réseaux disponibles
available_networks = scan_wifi()
print(f"Available Networks: {available_networks}")

# Demander à l'utilisateur de se connecter
network_ssid = "XNetwork"
network_pass = "12345678"
connect_wifi(network_ssid, network_pass)

print(f"Trying to connect to {network_ssid}...")
