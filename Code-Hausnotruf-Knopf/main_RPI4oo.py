import time
import requests
import RPi.GPIO as GPIO
from gpiozero import PWMLED, Button
from smbus2 import SMBus
from mpu6050 import mpu6050

# Netzwerk einrichten WLAN-Verbindung
ssid = AndroidAP25A5
password = gjht7545

# Das Netzwerk wird in der Regel über die grafische Oberfläche oder ein Terminal eingerichtet
# Siehe vorherige Anleitung

# RGB-LED Setup
led_r = PWMLED(15)
led_g = PWMLED(16)
led_b = PWMLED(17)

def set_led_color(r, g, b)
    led_r.value = r  255.0
    led_g.value = g  255.0
    led_b.value = b  255.0

def blink_led(r, g, b, duration=0.5)
    set_led_color(r, g, b)
    time.sleep(duration)
    set_led_color(0, 0, 0)
    time.sleep(duration)

# Matrix-API Einstellungen
matrix_server = httpsmatrix.org  # Matrix-Server, Element als App installiert
access_token = syt_aHNucmFuYmE_vSvbFHbibprhTxvJBBoD_4IRejw  # Teilnehmerin
room_id = !FTmUTmQleJsspLegXDmatrix.org  
# oder der Raum auf deinem Server httpsmatrix.to##NotrufePicoWmatrix.org

# Nachricht senden
def send_message(message)
    url = f{matrix_server}_matrixclientr0rooms{room_id}sendm.room.messageaccess_token={access_token}
    headers = {
        Content-Type applicationjson
    }
    payload = {
        msgtype m.text,
        body message
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200
        print(Nachricht gesendet System gestartet und verbunden!)
    else
        print(fFehler beim Senden der Nachricht {response.status_code}, {response.text})

# Nachricht senden
send_message(System gestartet und verbunden)
set_led_color(0, 255, 0)  # Grün ohne Blinken

# Setup für Notfallknopf
button = Button(14)
print(Notfallknopf aktiviert)

# Setup für den Beschleunigungssensor MPU6050
i2c = SMBus(1)
accelerometer = mpu6050(0x68)

# Funktion zum Erkennen eines Sturzes
def detect_fall()
    threshold = 15
    acceleration = accelerometer.get_accel_data()
    total_acc = sum([abs(acceleration['x']), abs(acceleration['y']), abs(acceleration['z'])])
    return total_acc  threshold

def wait_for_button_press(duration)
    start_time = time.time()
    while time.time() - start_time  duration
        if button.is_pressed
            return False
        time.sleep(0.1)
    return True

try
    while True
        if button.is_pressed
            set_led_color(0
