import network
import urequests as requests
import time
from machine import Pin, PWM

# Netzwerk einrichten/ WLAN-Verbindung
ssid = "AndroidAP25A5"
password = "gjht7545"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# RGB-LED Setup
led_r = PWM(Pin(24))
led_g = PWM(Pin(25))
led_b = PWM(Pin(26))

led_r.freq(1000)
led_g.freq(1000)
led_b.freq(1000)

def set_led_color(r, g, b):
    led_r.duty_u16(int(r * 65535 / 255))
    led_g.duty_u16(int(g * 65535 / 255))
    led_b.duty_u16(int(b * 65535 / 255))

def blink_led(r, g, b, duration=0.5):
    while not wlan.isconnected():
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
room_id = "!FTmUTmQleJsspLegXD:matrix.org"  # oder der Raum auf deinem Server https://matrix.to/#/#NotrufePicoW:matrix.org

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
button = Pin(19, Pin.IN, Pin.PULL_UP)

try:
    while True:
        if not button.value():
            set_led_color(255, 0, 0)  # Rot
            for _ in range(10):  # Blinkt 10 mal
                set_led_color(255, 0, 0)
                time.sleep(0.1)
                set_led_color(0, 0, 0)
                time.sleep(0.1)
            send_message("Notfallknopf gedrückt!")
            break
        time.sleep(0.1)
finally:
    # GPIO-Pins freigeben
    led_r.deinit()
    led_g.deinit()
    led_b.deinit()
    button.init(Pin.IN)  # Setzt den Knopf-Pin auf den Standard-Eingangsmodus
    wlan.active(False)  # WLAN deaktivieren
    print("GPIOs freigegeben und WLAN deaktiviert")
