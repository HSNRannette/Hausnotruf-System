import network
import urequests as requests
import time
from machine import Pin, PWM, I2C
from mpu6050 import MPU6050

# Netzwerk einrichten/ WLAN-Verbindung
ssid = "AndroidAP25A5"
password = "gjht7545"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# RGB-LED Setup
led_r = PWM(Pin(15))
led_g = PWM(Pin(16))
led_b = PWM(Pin(17))

led_r.freq(1000)
led_g.freq(1000)
led_b.freq(1000)

def set_led_color(r, g, b):
    led_r.duty_u16(int(r * 65535 / 255))
    led_g.duty_u16(int(g * 65535 / 255))
    led_b.duty_u16(int(b * 65535 / 255))

def blink_led(r, g, b, duration=0.5):
    set_led_color(r, g, b)
    time.sleep(duration)
    set_led_color(0, 0, 0)
    time.sleep(duration)

# Blinkt Blau, während die Verbindung hergestellt wird
while not wlan.isconnected():
    print("Verbinden...")
    blink_led(0, 0, 255, duration=0.5)

print("Verbunden, IP Adresse:", wlan.ifconfig()[0])

# Matrix-API Einstellungen
matrix_server = "https://matrix.org"  # Matrix-Server, Element als App installiert
access_token = "syt_aHNucmFuYmE_vSvbFHbibprhTxvJBBoD_4IRejw"  # Teilnehmer:in
room_id = "!FTmUTmQleJsspLegXD:matrix.org"  
# oder der Raum auf deinem Server https://matrix.to/#/#NotrufePicoW:matrix.org

# Nachricht senden
def send_message(message):
    url = f"{matrix_server}/_matrix/client/r0/rooms/{room_id}/send/m.room.message?access_token={access_token}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "msgtype": "m.text",
        "body": message
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Nachricht gesendet!")
    else:
        print(f"Fehler beim Senden der Nachricht: {response.status_code}, {response.text}")

# Nachricht senden
send_message("System gestartet und verbunden")
set_led_color(0, 255, 0)  # Grün ohne Blinken

# Setup für Notfallknopf
button = Pin(14, Pin.IN, Pin.PULL_UP)

# Setup für den Beschleunigungssensor MPU6050
i2c = I2C(0, scl=Pin(2), sda=Pin(3))
accelerometer = MPU6050(i2c)

# Funktion zum Erkennen eines Sturzes
def detect_fall():
    threshold = 15
    acceleration = accelerometer.get_accel_data()
    total_acc = sum([abs(acceleration['x']), abs(acceleration['y']), abs(acceleration['z'])])
    return total_acc > threshold

def wait_for_button_press(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        if button.value():
            return False
        time.sleep(0.1)
    return True

try:
    while True:
        if not button.value():
            set_led_color(255, 0, 0)  # Rot
            for _ in range(20):  # Blinkt 20 mal
                set_led_color(255, 0, 0)
                time.sleep(0.1)
                set_led_color(0, 0, 0)
                time.sleep(0.1)
            send_message("Notfallknopf gedrückt!")
            
            # Blink LED rot bis der Knopf für 5 Sekunden gedrückt wird
            while True:
                blink_led(255, 0, 0, duration=0.5)
                if not button.value():
                    if wait_for_button_press(5):
                        break
            
            # Nach 5 Sekunden drücken wechselt die LED zu Grün und Schleife ist wieder aktiv
            set_led_color(0, 255, 0)  # Grün ohne Blinken
            send_message("Patient A erhielt Hilfe")

        if detect_fall():
            set_led_color(255, 0, 0)  # Rot
            for _ in range(20):  # Blinkt 20 mal
                set_led_color(255, 0, 0)
                time.sleep(0.1)
                set_led_color(0, 0, 0)
                time.sleep(0.1)
            send_message("Patient A gestürzt, dringend Hilfe benötigt!")
            
            # Blink LED rot bis der Knopf für 5 Sekunden gedrückt wird
            while True:
                blink_led(255, 0, 0, duration=0.5)
                if not button.value():
                    if wait_for_button_press(5):
                        break
            
            # Nach 5 Sekunden drücken wechselt die LED zu Grün und Schleife ist wieder aktiv
            set_led_color(0, 255, 0)  # Grün ohne Blinken
            send_message("Patient A gestürzt, dringend Hilfe benötigt!")

        time.sleep(0.1)
finally:
    # GPIO-Pins freigeben
    led_r.deinit()
    led_g.deinit()
    led_b.deinit()
    button.init(Pin.IN)  # Setzt den Knopf-Pin auf den Standard-Eingangsmodus
    wlan.active(False)  # WLAN deaktivieren
    print("GPIOs freigegeben und WLAN deaktiviert")
