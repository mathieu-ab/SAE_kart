import json
import time
import requests
import serial
import paho.mqtt.client as mqtt

broker = "192.168.1.205"
port = 1883
zoom_topic = "gps/zoom"
destination_topic = "gps/destination"
zoom_level = 15
destination_address = None
destination_coords = None
API_KEY = "AIzaSyDLvUcraTLttRBcvn728IaGCe_prAZK24Q"

def on_message(client, userdata, msg):
    global zoom_level, destination_address, destination_coords
    try:
        message = msg.payload.decode("utf-8")
        if msg.topic == zoom_topic:
            if message == "zoom":
                zoom_level = min(zoom_level + 1, 20)
            elif message == "dezoom":
                zoom_level = max(zoom_level - 1, 5)
            print(f"Zoom level set to {zoom_level}")
        elif msg.topic == destination_topic:
            destination_address = message
            destination_coords = get_destination_coordinates(destination_address)
            print(f"Received new destination: {destination_address} -> {destination_coords}")
    except Exception as e:
        print(f"MQTT error: {e}")

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port)
client.subscribe(zoom_topic)
client.subscribe(destination_topic)
client.loop_start()

def publish_gps(lat, lon):
    payload = json.dumps({"latitude": lat, "longitude": lon})
    client.publish("gps/position", payload)

def get_gps_coordinates():
    ser = serial.Serial('/dev/ttyAMA1', 9600, timeout=1)
    while True:
        line = ser.readline().decode('utf-8', errors='ignore')
        if line.startswith('$GPGGA'):
            lat, lon = parse_gpgga(line)
            if lat and lon:
                return lat, lon
        time.sleep(0.5)

def parse_gpgga(data):
    parts = data.split(',')
    if len(parts) > 5:
        lat = convert_to_degrees(parts[2])
        lat_dir = parts[3]
        lon = convert_to_degrees(parts[4])
        lon_dir = parts[5]
        if lat and lon:
            lat = -lat if lat_dir == 'S' else lat
            lon = -lon if lon_dir == 'W' else lon
            return lat, lon
    return None, None

def convert_to_degrees(raw_value):
    if not raw_value:
        return None
    try:
        d = int(float(raw_value) / 100)
        m = float(raw_value) - d * 100
        return d + (m / 60)
    except ValueError:
        return None

def get_destination_coordinates(address):
    """  Google Geocoding API  """
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    response = requests.get(url).json()
    if response["status"] == "OK":
        location = response["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    return None

def get_route(start_lat, start_lon, dest_lat, dest_lon):
    """ Google Directions API  """
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_lat},{start_lon}&destination={dest_lat},{dest_lon}&mode=driving&key={API_KEY}"
    response = requests.get(url).json()
    if response["status"] == "OK":
        return response["routes"][0]["overview_polyline"]["points"]
    return None

def get_google_map(lat, lon, route=None):
    """ Télécharge une carte Google Maps avec la position GPS """
    global zoom_level, destination_coords
    base_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom_level}&size=600x400&maptype=roadmap&markers=color:red%7C{lat},{lon}&key={API_KEY}"
    
    if destination_coords:
        base_url += f"&markers=color:blue%7C{destination_coords[0]},{destination_coords[1]}"
    
    if route:
        base_url += f"&path=color:0x0000ff|weight:5|enc:{route}"

    response = requests.get(base_url)
    with open('/home/kartuser/SAE_kart/GPS/map.png', 'wb') as f:  # Chemin absolu pour éviter les erreurs
        f.write(response.content)
    print("Image map.png mise à jour !")

def update_map():
    while True:
        try:
            latitude, longitude = get_gps_coordinates()
            print(f"GPS Location: LAT: {latitude}, LON: {longitude}")
            publish_gps(latitude, longitude)

            route = None
            if destination_coords:
                route = get_route(latitude, longitude, *destination_coords)

            get_google_map(latitude, longitude, route)
            
            time.sleep(3)  # Mettre à jour la carte toutes les 3 secondes

        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(3)  # Attendre un peu avant de réessayer en cas d'erreur

if __name__ == "__main__":
    update_map()
