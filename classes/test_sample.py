from meteo_scraper import MeteoScraper
import unittest

class TestScrape(unittest.TestCase):

    def setUp(self):
        self.scraper = MeteoScraper(True)

    def test_daytext(self):
        self.assertEqual(self.scraper.get_reldate(0), "heute")
        self.assertEqual(self.scraper.get_reldate(1), "morgen")
        self.assertEqual(self.scraper.get_reldate(2), "am Donnerstag")
    
    def test_weathertext(self):
        self.scraper = MeteoScraper(True)
        self.assertEqual(self.scraper.find_weather('6005', 0),"In Luzern ist das Wetter heute Sonne und Wolken im Wechsel. Tagsüber wird es 5 Grad. Nachts wird es 4 Grad.") #dieser Test hat geholfen zu identifizieren dass die Temperaturen verkehr gespeichert wurden!
        self.scraper = MeteoScraper(True)
        self.assertEqual(self.scraper.find_weather('6005', 1),"In Luzern ist das Wetter morgen Sonne und Wolken im Wechsel. Tagsüber wird es 4 Grad. Nachts wird es 2 Grad.")
        self.scraper = MeteoScraper(True)
        self.assertEqual(self.scraper.find_weather('6005', 2),"In Luzern ist das Wetter am Donnerstag Sonne und Nebelbänke. Tagsüber wird es 3 Grad. Nachts wird es 1 Grad.")

if __name__ == '__main__':
    unittest.main()