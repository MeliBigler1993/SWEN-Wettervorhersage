# SWEN-Wettervorhersage
Das Projekt erlaubt es dem User / der Userin eine Wettervorhersage für einen gewünschten Ort (und evtl. eine gewünschte Zeitdauer) zu erhalten. Die Funktion wird über ein GUI angeboten. 

## Installationsanleitung / Dependencies
Installiere die folgenden Pakete über pip: 
* PyQt5 `pip install PyQt5`: https://pypi.org/project/PyQt5/
* Selenium `pip install selenium`: https://pypi.org/project/selenium/ 
* Text-to-speech library `pip install pyttsx3`: https://pypi.org/project/pyttsx3/
* PyAudio (to use Mic as VoiceInput) `pip install PyAudio`: https://pypi.org/project/PyAudio/ 
* Speech Recognition `pip install SpeechRecognition`: https://pypi.org/project/SpeechRecognition/
* Chromedriver: https://chromedriver.chromium.org/downloads

Um die App zu starten muss das File "wetter_app.py" im Root-Folder gestartet werden. 
Beispielsweise mit `python3 wetter_app.py`

## Projekt Ziele
* User soll eine Wettervorhersage für einen von ihm/ihr bestimmten Ort und Tag erhalten
* User soll wählen können, ob die Ein-/Ausgabe über Tastatur oder Sprache geschieht 
* Code soll schlussendlich auf einer Mobile App laufen (inkl. Speech Recognition & Text to Speech) 

## Qualität & Prozess Ziele
* Der Code soll den Prinzipien von Clean Code entsprechen  
* Wir verwenden Version Control via GitHub 
* Wir testen den Code via Unittesting

## Weitere Entwicklungsmöglichkeiten
* In der aktuellen Version wird in der Voice-Steuerung nur das Wetter für den heutigen Tag ausgegeben. Es müsste noch eine Funktion eingebaut werden, die es erlaubt den Tag zu nennen
* Die Anwendung ist aktuell nur für das Nutzen auf einem Laptop oder Desktop konfiguriert. Mobile Deployment wäre ein nächster Schritt

## Kontakt
* Bei Fragen oder nicht-funktionieren des Codes kann gerne auf das Projektteam zugegangen werden
* Die Kontaktmöglichkeiten finden sich auf den Github Profilen