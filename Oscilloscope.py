import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import matplotlib.pyplot as plt

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Read from A0
chan = AnalogIn(ads, ADS.P0)

data = []

plt.ion()

while True:
    voltage = chan.voltage
    data.append(voltage)

    if len(data) > 200:
        data.pop(0)

    plt.clf()
    plt.plot(data)
    plt.title("Oscilloscope")
    plt.ylabel("Voltage")
    plt.xlabel("Samples")
    plt.pause(0.01)
