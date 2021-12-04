# Testing
* Hatte Mühe Exceptions zu testen -> also wie kann ich den Test so einrichten, dass er "OK" ist wenn ein SystemExit erzeugt wird
* Es ist mühsam die Funktion "find_weather" zu testen, weil davor der Value wert immer zuerst nachgeschaut und angepasst werden muss 

# Coding MeteoScraper
* Ich wollte mehr und genauere Exceptions einbauen, aber das wurde recht kompliziert, da die .until funktion bereits eine exception raised
* Daher musste ich die SystemExit exception eine Ebene höher einbauen 
* Das könnte man bestimmt noch sauberer machens

# Coding Speech_rec
* Das war eher einfach
* Die Klassen liessen sich hier viel besser trennen

# Verbesserungs / Ausweitungspotenzial
* Weitere Sprachen einbauen
* Input day_delay als Optionenlist einbauen statt als reiner Tasteninput
* 