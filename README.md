# Hausnotruf-System

# Einleitung
Die Projektidee entstammt einem Hausnotrufsystem der Amublanten Dienste für Senioren in betreuten Wohnformen oder Risikopatienten im häuslichen Umfeld.
Das Projekt „Hausnotrufsystem mit Raspberry Pi Pico W“ zielt auf ein zuverlässiges und effizientes Patientenüberwachungssystem, das Hilfesignale in Echtzeit erkennt und als Warnung oder Notruf klassifiziert. Insbesondere soll das System helfen, schnell auf Gefahren  auftreten können, zu reagieren und so Rettungs- und Pflegepersonal rechtzeitig zu informieren.

# Motivation

Patienten mit chronischen Erkrankungen oder Herzproblemen sind häufig auf ein zuverlässiges Überwachungssystem angewiesen. Herkömmliche Notrufsysteme erfordern jedoch oft eine manuelle Aktivierung durch den Patienten. Dieses Projekt soll diese Lücke schließen, indem es ein automatisiertes System bereitstellt, das kritische Gesundheitsdaten überwacht und im Notfall automatisch einen Alarm auslöst.

# Zielsetzung
Das Hauptziel des Projekts ist die Verbesserung der Sicherheit und des Wohlbefindens der Patienten durch eine kontinuierliche Überwachung der Herzfrequenz und der körperlichen Aktivität. Die Hauptkomponenten des Systems umfassen

-Raspberry Pi Pico W: als zentrale Steuereinheit zur Erfassung und Verarbeitung aller Sensordaten.
-ADXL345 Beschleunigungssensor: Wird zur Erkennung eines möglichen Sturzes verwendet.
-Notfallknopf: Kann vom Patienten manuell betätigt werden. Damit wird sofortige Hilfe angefordert.
-RGB-LED: Zeigt deutlich die Signalwirkung der Notsituation oder den Zustand des Patienten an.


Die Grundidee besteht darin, den Pico W als Steuer- und Kontrollelement zu verwenden. Er verwaltet alle Sensoren und empfängt die Vitalwerte des Patienten. Es hat die Aufgabe zu beurteilen, ob die Werte innerhalb der definierten Intervalle sind und bei Überschreitung der Intervalle Meldungen zu versenden. Die Meldungen gehen an die Endgeräte wie Smartphone oder Desktop des Pflegepersonals.

Die Anwendung Element wurde auf die Endgeräte Raspberry Pi 400, Laptop sowie Smartphone heruntergeladen. Auf Matrix.org wurde ein Home-Server "https://matrix-client.matrix.org" und ein 
Identitätsserver "https://vector.im", sowie eine eindeutige Teilnehmer:innen ID und Zugriffstoken generiert. Für dieses Projekt wurde eine Raum-ID für eine Personengruppe wie z.B. "Pflegeteam" eingerichtet. Notrufe werden von Pico W mit der Hauptsteuerung der Sensoren an die Endgeräte des Pflegepersonals in Form von mobilen Geräten oder Desktop weitergeleitet.

# Fazit

Das ursprüngliche Projekt kombiniert den Raspberry Pi Pico W mit einem Herzfrequenzsensor, einem Beschleunigungssensor und einem Notfallknopf und stellt damit eine wertvolle Lösung für die Überwachung des Gesundheitszustands von Patienten und die schnelle Alarmierung im Notfall dar. Die Implementierung nutzt das WLAN-Modul des Pico W zur Kommunikation mit einem Matrix-Server, was eine vielseitige Methode zur Benachrichtigung von Pflegepersonal oder Angehörigen darstellt.

Das Projekt ist in seiner jetzigen Form ausbaufähig und die Kommunikation mit dem Matrix-Server muss verbessert werden. Initialisierungsfehler: Neben allen Sensoren müssen auch die I2C-Schnittstellen korrekt initialisiert und kalibriert werden. Initialisierungsfehler können zu ungenauen Messungen oder Kommunikationsfehlern führen. Das ursprüngliche Projekt kombiniert den Raspberry Pi Pico W mit einem Herzfrequenzsensor, einem Beschleunigungssensor und einem Notfallknopf und stellt damit eine wertvolle Lösung für die Überwachung des Gesundheitszustands von Patienten und die schnelle Alarmierung im Notfall dar. Die Implementierung nutzt das WLAN-Modul des Pico W zur Kommunikation mit einem Matrix-Server, was eine vielseitige Methode zur Benachrichtigung von Pflegepersonal oder Angehörigen darstellt.

Das Projekt ist in seiner jetzigen Form ausbaufähig und die Kommunikation mit dem Matrix-Server muss verbessert werden. Initialisierungsfehler: Neben allen Sensoren müssen auch die I2C-Schnittstellen korrekt initialisiert und kalibriert werden. Initialisierungsfehler können zu ungenauen Messungen oder Kommunikationsfehlern führen.
Bei sorgfältiger Fehlerbehandlung kann dieses Projekt einen wichtigen Beitrag zur Patientenüberwachung und Notfallreaktion leisten.
