"""
instance of scraper configured to scrape the page www.srf.ch/meteo
"""
# to import in another file call from .classes.meteo_scraper import ...

import sys
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class MeteoScraper:
    #Todo @IrisAmrein change variable names to reflect their content better (e.g. day_delay, delay)
    """
    initiates a Chrome Driver configured to scrape the page www.srf.ch/meteo

    :headless: boolean  - should the browser be shown | default = False
    """
    def __init__(self, headless=False):
        drivopt = webdriver.ChromeOptions()
        if headless:
            drivopt.add_argument('headless')
        self.driver = webdriver.Chrome(options = drivopt)

    def find_weather(self,loc, day_index=0):
        """
        launch webdriver and search for weather information for plz
        :plz: str - PLZ or Name of location to search weather for
        :day_index: int - no of days from today for day that weather should be forecasted

        :return: str (text) - a text that describes the weather and temp at the given day
        """
        if day_index>6:
            self.driver.quit()
            return "Please enter a valid day index (0 - 6) and run the script again."

        self.nav_to_loc_meteo_page(loc)
        location = self.get_location_name()

        day_element = self.get_day_element(day_index)
        low, high = self.get_temperature(day_element)
        weather = day_element.find_element(By.TAG_NAME, "img").get_attribute("alt") # Get the weather by looking at the "alt" Attribute of the weather icon

        day_text = self.get_reldate(day_index)

        self.driver.quit()

        text = "In "+location+" ist das Wetter "+day_text+" "+weather+". \nTagsüber wird es "+high+" Grad. Nachts wird es "+low+" Grad."
        return text

    ########################
    ### HELPER FUNCTIONS ###
    ########################

    def nav_to_loc_meteo_page(self, loc):
        """
        enters a PLZ or location in the searchbar on the webpage www.srf.ch/meteo
        and clicks on the first result.
        :loc: str - location to navigate to
        """
        self.driver.get("https://www.srf.ch/meteo")
        search = self.driver.find_element(By.ID, "search__input")
        search.send_keys(loc)

        optlist = self.find_elements_by_class("search-result__link")

        #select the first element of the searchbox dropdown if there are results, else exit script
        if optlist == False:
            self.driver.quit()
            sys.exit()
        else:
            optlist[0].click()

    def find_elements_by_class(self,classname):
        """
        finds and returns all elements with a certain classname.
        Makes sure to wait to get the element until the element has loaded.
        :classname: str - classname of desired elements

        :return: list - all elements with the given classname
        """

        try:
            WebDriverWait(self.driver,3).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,classname)),
            )
            result = self.driver.find_elements(By.CLASS_NAME, classname)
            elements = result
            return elements
        except:
            print("No results for the given location. Please try again")
            return False

    def get_location_name(self):
        """
        gets location from web

        :return: str - location of weather forecast
        """
        title = self.driver.title
        title_words = title.split(" ")
        del title_words[0:1]
        del title_words[len(title_words)-4:len(title_words)]
        title = ' '.join(title_words)
        return title

    def get_day_element(self, delay=0):
        """
        get element of the given day on the website
        :return: WebElement - element that contains weather of the given day
        """
        daylist = self.driver.find_element(By.CLASS_NAME, "weather-week")
        items = daylist.find_elements(By.TAG_NAME,"li")
        day_element = items[delay].find_element(By.TAG_NAME, "button")

        return day_element

    def get_temperature(self, day):
        """
        gets temperature of a specific day from the site
        :day: int - the index of the day to get (0 = today, 1 = tomorrow, etc.)

        :return: (high, low)
        """
        low = day.find_element(By.CLASS_NAME, "weather-day__tmp--low")
        lowtmp = low.find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
        high = day.find_element(By.CLASS_NAME, "weather-day__tmp--hi")
        hightmp = high.find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
        return lowtmp, hightmp

    def get_reldate(self,delay):
        """
        :delay: int - number of days after today

        :return: (day_text) - a string that indicates which day is targeted ("heute", "morgen", "am Montag", ...)
        """
        #define a dict of weekdays to use for identification later
        weekdays = {
                0: 'Montag',
                1: 'Dienstag',
                2: 'Mittwoch',
                3: 'Donnerstag',
                4: 'Freitag',
                5: 'Samstag',
                6: 'Sonntag',
            }
        if int(delay) == 0:
            return "heute"
        elif int(delay) == 1:
            return "morgen"
        else:
            today = int(date.today().weekday())
            weekday = today + delay
            if weekday > 6:
                weekday = weekday-7
            word = weekdays[weekday]
            return "am " + word

#INFO: Wenn PyQt Ready muss alles unter dieser Linie gelöscht werden.

# loc_input = input("Für welche PLZ möchtest du das Wetter wissen? ")
# delay = input("Für wie viele Tage von heute aus?")

# scraper = MeteoScraper()
# weather_forecast = scraper.find_weather(loc_input, int(delay))

# print(weather_forecast)
