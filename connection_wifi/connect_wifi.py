import wifi
import time

# scan for available WiFi networks
wifi_scanner = wifi.Cell.all('wlan0')

# print available networks

# connect to a WiFi network
network_ssid = "XNetwork"
network_pass = "12345678"

for cell in wifi_scanner:
	if cell.ssid == network_ssid:
		scheme = wifi.Scheme.for_cell('wlan0', cell.ssid, cell, network_pass)
		scheme.save()
		scheme.activate()
		print(f"Connected to network: {network_ssid}")
		break
else:
	print(f"Unable to find network: {network_ssid}")