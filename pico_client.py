# Main.py läuft automatisch, sobald Pico W eine Energieverbindung hat.
import network # Für die Mobile Hotspotverbindung
import urequests as requests
import time
from machine import Pin # to be able to work with the hardware
from time import sleep # to add delays in the program

# Netwerk einrichten
ssid = "AndroidAP25A5"
password = "gjht7545"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Verbinden...")
    time.sleep(1)

print("Verbunden, IP Adresse:", wlan.ifconfig()[0])


# Matrix-API Einstellungen
matrix_server = "https://matrix.org"  # Matrix-Server, Element als App installiert
access_token = "syt_aHNucmFuYmE_vSvbFHbibprhTxvJBBoD_4IRejw" # Teilnehmer:in
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

# Beispielnachricht senden
send_message("HILFE! Brauche ein Notarzt. Patient A!")


