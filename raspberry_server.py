import time
import board
import busio
import digitalio
from adafruit_max30102 import MAX30102
from adafruit_adxl34x import ADXL345
import requests

# Setup for MAX30102
i2c = busio.I2C(board.SCL, board.SDA)
max30102 = MAX30102(i2c)

# Setup for ADXL345
adxl345 = ADXL345(i2c)

# Setup for emergency button
button_pin = digitalio.DigitalInOut(board.D17)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP

def send_alert(message):
    url = "http://your-notification-endpoint"
    data = {"message": message}
    requests.post(url, json=data)

def check_heart_rate():
    while not max30102.check_for_sample():
        pass
    red, ir = max30102.read_fifo()
    return ir  # Simplified example, should implement actual heart rate calculation

def check_fall():
    acceleration = adxl345.acceleration
    x, y, z = acceleration
    if abs(x) > threshold or abs(y) > threshold or abs(z) > threshold:
        return True
    return False

threshold = 15  # Adjust the threshold based on your calibration

while True:
    heart_rate = check_heart_rate()
    if heart_rate < 50 or heart_rate > 150:  # Example thresholds for abnormal heart rate
        send_alert("Abnormal heart rate detected!")

    if check_fall():
        send_alert("Fall detected!")

    if not button_pin.value:
        send_alert("Emergency button pressed!")

    time.sleep(1)