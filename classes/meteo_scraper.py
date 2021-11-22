"""
instance of scraper configured to scrape the page www.srf.ch/meteo
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MeteoScraper:
    #Todo @IrisAmrein change variable names to reflect their content better (e.g. day_delay, delay)
    """
    instances a Chrome Driver configured to scrape the page www.srf.ch/meteo
    """
    def __init__(self, headless=False) -> None:
        """
        initializes driver

        :headless: boolean - default = False - should the browser be shown
        """
        drivopt = webdriver.ChromeOptions()
        if headless:
            drivopt.add_argument('headless')
        self.driver = webdriver.Chrome(options = drivopt)

    def find_weather(self,loc, day_index=0):
        """
        launch webdriver and search for weather information for plz
        :plz: int/str - PLZ or Name of location to search weather for
        :day_index: int - no of days from today for day that weather should be forecasted

        :return: weather values (location, text, high, low)
        """
        self.driver.get("https://www.srf.ch/meteo")
        search = self.driver.find_element(By.ID, "search__input")
        search.send_keys(loc)

        optlist = self.find_element_by_class("search-result__link")
        optlist[0].click()
        location = self.get_location()

        day = self.get_day(day_index)
        high, low = self.get_temperature(day)
        weather = day.find_element(By.TAG_NAME, "img").get_attribute("alt")

        self.driver.quit()

        #todo #7 Transform day_index into human understandable text (0 = "heute", 1= "morgen", etc.)

        text = "In "+location+" ist das Wetter "+weather+". Tagsüber wird es "+high+" Grad. Nachts wird es "+low+" Grad."
        return text

    def find_element_by_class(self,classname):
        """
        finds and returns all elements with a certain classname.
        :classname: str - classname of desired elements

        :return: list - all elements with the given classname
        """
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,classname))
            )
            result = self.driver.find_elements(By.CLASS_NAME, classname)
            elements = result
            return elements
        except:
            print("did not find element of class", classname)
            self.driver.quit()
            return False

    def get_location(self):
        """
        returns location

        :return: str - location of weather forecast
        """
        title = self.driver.title
        title_words = title.split(" ")
        del title_words[0:1]
        del title_words[len(title_words)-4:len(title_words)]
        title = ' '.join(title_words)
        return title

    def get_day(self, delay=0):
        """
        dwe
        """
        daylist = self.driver.find_element(By.CLASS_NAME, "weather-week")
        items = daylist.find_elements(By.TAG_NAME,"li")
        day = items[delay].find_element(By.TAG_NAME, "button")

        return day

    def get_temperature(self, day):
        """
        :return: (high, low)
        """
        low = day.find_element(By.CLASS_NAME, "weather-day__tmp--low")
        lowtmp = low.find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
        high = day.find_element(By.CLASS_NAME, "weather-day__tmp--hi")
        hightmp = high.find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
        return lowtmp, hightmp

loc_input = input("Für welche PLZ möchtest du das Wetter wissen? ")
delay = input("Für wie viele Tage von heute aus?")

scraper = MeteoScraper()
weather_forecast = scraper.find_weather(loc_input, int(delay))

print(weather_forecast)
