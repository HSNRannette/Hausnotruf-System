# Hausnotruf-System

# Einleitung
Die Projektidee entstammt einem Hausnotrufsystem der Amublanten Dienste für Senioren in betreuten Wohnformen oder Risikopatienten im häuslichen Umfeld.
Das Projekt „Hausnotrufsystem mit Raspberry Pi Pico W“ zielt auf ein zuverlässiges und effizientes Patientenüberwachungssystem, das Hilfesignale in Echtzeit erkennt und als Warnung oder Notruf klassifiziert. Insbesondere soll das System helfen, schnell auf stille Gefahren oder plötzliche Herzstillstände, die während des Schlafs auftreten können, zu reagieren und so Rettungs- und Pflegepersonal rechtzeitig zu informieren.

# Motivation

Patienten mit chronischen Erkrankungen oder Herzproblemen sind häufig auf ein zuverlässiges Überwachungssystem angewiesen. Herkömmliche Notrufsysteme erfordern jedoch oft eine manuelle Aktivierung durch den Patienten. Dies ist bei einem plötzlichen Herzstillstand oder im Schlaf nicht möglich. Dieses Projekt soll diese Lücke schließen, indem es ein automatisiertes System bereitstellt, das kritische Gesundheitsdaten überwacht und im Notfall automatisch einen Alarm auslöst.

# Zielsetzung
Das Hauptziel des Projekts ist die Verbesserung der Sicherheit und des Wohlbefindens der Patienten durch eine kontinuierliche Überwachung der Herzfrequenz und der körperlichen Aktivität. Die Hauptkomponenten des Systems umfassen

-Raspberry Pi Pico W: als zentrale Steuereinheit zur Erfassung und Verarbeitung aller Sensordaten.
-MAX30102 Herzfrequenz-Sensor: Für die Überwachung der Herzfrequenz und der Sauerstoffsättigung.
-ADXL345 Beschleunigungssensor: Wird zur Erkennung eines möglichen Sturzes verwendet.
-Notfallknopf: Kann vom Patienten manuell betätigt werden. Damit wird sofortige Hilfe angefordert.
-RGB-LED: Zeigt deutlich die Signalwirkung der Notsituation oder den Zustand des Patienten an.


Die Grundidee besteht darin, den Pico W als Steuer- und Kontrollelement zu verwenden. Er verwaltet alle Sensoren und empfängt die Vitalwerte des Patienten. Es hat die Aufgabe zu beurteilen, ob die Werte innerhalb der definierten Intervalle sind und bei Überschreitung der Intervalle Meldungen zu versenden. Dabei kann zwischen einem Notruf und einer Warnmeldung unterschieden werden.
Die Meldungen gehen an die Endgeräte wie Smartphone oder Desktop des Pflegepersonals.

Die Anwendung Element wurde auf die Endgeräte Raspberry Pi 400, Laptop sowie Smartphone heruntergeladen. Auf Matrix.org wurde ein Home-Server "https://matrix-client.matrix.org" und ein 
Identitätsserver "https://vector.im", sowie eine eindeutige Teilnehmer:innen ID und Zugriffstoken generiert. Für dieses Projekt wurde eine Raum-ID für eine Personengruppe wie z.B. "Pflegeteam" eingerichtet. Notrufe werden von Pico W mit der Hauptsteuerung der Sensoren an die Endgeräte des Pflegepersonals in Form von mobilen Geräten oder Desktop weitergeleitet.

# Fazit

Exceptions Python
