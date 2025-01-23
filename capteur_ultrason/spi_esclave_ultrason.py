import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device (CS) 0
spi.max_speed_hz = 50000

def read_distance():
    # Request 2 bytes from Arduino (MSB, LSB)
    response = spi.xfer2([0x00, 0x00])
    distance = (response[0] << 8) | response[1]  # Combine MSB and LSB
    return distance

try:
    while True:
        dist = read_distance()
        print(f"Distance: {dist} cm")
        time.sleep(0.5)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Exiting...")
finally:
    spi.close()
