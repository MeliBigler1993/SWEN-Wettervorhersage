import unittest
from meteo_scraper import MeteoScraper

class TestScrape(unittest.TestCase):

    def setUp(self):
        self.scraper = MeteoScraper(True)

    def test_weathertext(self):
        """
        tests the main function
        initiates a new MeteoScraper before every test because otherwise there will be a timeout. (time.sleep did not help)
        """
    #     Die resultierenden Texte müssen je nach Datum an dem getestet wird erst angepasst werden bevor getestet werden kann
    #     self.scraper = MeteoScraper(True)
    #     self.assertEqual(self.scraper.find_weather('6005', 0),
    #     "In Luzern ist das Wetter heute Sonne und Wolken im Wechsel. Tagsüber wird es 5 Grad. Nachts wird es 4 Grad.") #dieser Test hat geholfen zu identifizieren dass die Temperaturen verkehr gespeichert wurden!
    #     self.scraper = MeteoScraper(True)
    #     self.assertEqual(self.scraper.find_weather('6005', 1),"In Luzern ist das Wetter morgen Sonne und Wolken im Wechsel. Tagsüber wird es 4 Grad. Nachts wird es 2 Grad.")
    #     self.scraper = MeteoScraper(True)
    #     self.assertEqual(self.scraper.find_weather('6005', 2),"In Luzern ist das Wetter am Donnerstag Sonne und Nebelbänke. Tagsüber wird es 3 Grad. Nachts wird es 1 Grad.")

    def test_daytext(self):
        self.assertEqual(self.scraper.get_reldate(0), "heute")
        self.assertEqual(self.scraper.get_reldate(1), "morgen")
    #     self.assertEqual(self.scraper.get_reldate(2), "am Donnerstag")#Muss je nach Zeitpunkt des Tests angepasst werden. Hier wurde am Dienstag getestet

    def test_location(self):
        self.scraper.driver.get("https://www.srf.ch/meteo/wetter/Affoltern-am-Albis/47.2761,8.4466")
        self.assertEqual(self.scraper.get_location_name(), "Affoltern am Albis")
        self.scraper.driver.get("https://www.srf.ch/meteo/wetter/Dufourspitze/45.9369,7.8668")
        self.assertEqual(self.scraper.get_location_name(), "Dufourspitze")

    # test that the script ends if an invalid location is called
    def test_invalid_loc(self):
        with self.assertRaises(SystemExit) as cm:
            self.scraper.driver.get("https://www.srf.ch/meteo")
            self.scraper.nav_to_loc_meteo_page('80005')
            self.assertEqual(cm.exception,"")

    def tearDown(self):
        self.scraper.driver.quit()

if __name__ == '__main__':
    unittest.main()
