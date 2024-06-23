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

while not wlan.isconnected():
    print("Verbinden...")
    

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

