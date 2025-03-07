import serial

uart = serial.Serial("/dev/ttyAMA2", baudrate=9600, timeout=1)

try:
    while True:
        if uart.in_waiting > 0:
            data = uart.readline().decode('utf-8').strip()
            print("Donnée reçue :", data)
except KeyboardInterrupt:
    print("Arrêt du programme.")
    uart.close()
