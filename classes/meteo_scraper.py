"""
instance of scraper configured to scrape the page www.srf.ch/meteo
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


class MeteoScraper:
    #Todo @IrisAmrein change variable names to reflect their content better (e.g. day_delay, delay)
    """
    instances a Chrome Driver configured to scrape the page www.srf.ch/meteo
    """
    def __init__(self, headless=False) -> None:
        """
        initialize new driver

        :headless: boolean  - should the browser be shown | default = False
        """
        PATH = './chromedriver'
        drivopt = webdriver.ChromeOptions()
        if headless:
            drivopt.add_argument('headless')
        self.driver = webdriver.Chrome(PATH, options = drivopt)

    # add a check to ask for input if day_index is higher than 6
    # catch errors if plz / location is not available
    def find_weather(self,loc, day_index=0):
        """
        launch webdriver and search for weather information for plz
        :plz: str - PLZ or Name of location to search weather for
        :day_index: int - no of days from today for day that weather should be forecasted

        :return: str (text) - a text that describes the weather and temp at the given day 
        """
        self.driver.get("https://www.srf.ch/meteo")
        search = self.driver.find_element(By.ID, "search__input")
        search.send_keys(loc)

        #select the first element of the searchbox dropdown
        optlist = self.find_element_by_class("search-result__link")
        optlist[0].click()
        location = self.get_location()

        day_element = self.get_day_element(day_index)
        high, low = self.get_temperature(day_element)
        weather = day_element.find_element(By.TAG_NAME, "img").get_attribute("alt")

        day_text = self.get_reldate(day_index)

        self.driver.quit()

        text = "In "+location+" ist das Wetter "+day_text+" "+weather+". Tagsüber wird es "+high+" Grad. Nachts wird es "+low+" Grad."
        return text

    ### HELPER FUNCTIONS ###

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
        weekdays = {
                0: 'Montag',
                1: 'Dienstag',
                2: 'Mittwoch',
                3: 'Donnerstag',
                4: 'Freitag',
                5: 'Samstag',
                6: 'Sonntag',
            }
        if(int(delay) == 0):
            return "heute"
        elif(int(delay) == 1):
            return "morgen"
        else:
            today = int(date.today().weekday())
            weekday = today + delay
            word = weekdays[weekday]
            return "am " + word

loc_input = input("Für welche PLZ möchtest du das Wetter wissen? ")
delay = input("Für wie viele Tage von heute aus?")

scraper = MeteoScraper()
weather_forecast = scraper.find_weather(loc_input, int(delay))

print(weather_forecast)
