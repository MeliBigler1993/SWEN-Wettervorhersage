import unittest
from meteo_scraper import MeteoScraper

class TestScrape(unittest.TestCase):

    def setUp(self):
        self.scraper = MeteoScraper(True)

    # def test_weathertext(self):
    #     """
    #     tests the main function 
    #     initiates a new MeteoScraper before every test because otherwise there will be a timeout. (time.sleep did not help)
    #     """
    #     self.scraper = MeteoScraper(True)
    #     self.assertEqual(self.scraper.find_weather('6005', 0),
    #     "In Luzern ist das Wetter heute Sonne und Wolken im Wechsel. Tagsüber wird es 5 Grad. Nachts wird es 4 Grad.") #dieser Test hat geholfen zu identifizieren dass die Temperaturen verkehr gespeichert wurden!
    #     self.scraper = MeteoScraper(True)
    #     self.assertEqual(self.scraper.find_weather('6005', 1),"In Luzern ist das Wetter morgen Sonne und Wolken im Wechsel. Tagsüber wird es 4 Grad. Nachts wird es 2 Grad.")
    #     self.scraper = MeteoScraper(True)
    #     self.assertEqual(self.scraper.find_weather('6005', 2),"In Luzern ist das Wetter am Donnerstag Sonne und Nebelbänke. Tagsüber wird es 3 Grad. Nachts wird es 1 Grad.")

    # def test_daytext(self):
        self.assertEqual(self.scraper.get_reldate(0), "heute")
        self.assertEqual(self.scraper.get_reldate(1), "morgen")
    #     self.assertEqual(self.scraper.get_reldate(2), "am Donnerstag")#Muss je nach Zeitpunkt des Tests angepasst werden. Hier wurde am Dienstag getestet

    def test_location(self):
        self.scraper.driver.get("https://www.srf.ch/meteo/wetter/Affoltern-am-Albis/47.2761,8.4466")
        self.assertEqual(self.scraper.get_location_name(), "Affoltern am Albis")
        self.scraper.driver.get("https://www.srf.ch/meteo/wetter/Dufourspitze/45.9369,7.8668")
        self.assertEqual(self.scraper.get_location_name(), "Dufourspitze")

    # test find_weather for a PLZ that does not exist
    # test error handling if element not loaded "find element by class name"
    # test get_day_element & get_temparature with disclaimer that assert Value must be changed depending on day

    def tearDown(self):
        self.scraper.driver.quit()

if __name__ == '__main__':
    unittest.main()
