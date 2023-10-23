from selenium.webdriver.chrome.options import Options
from Select import formats
from xpath import xpaths
from optarg import arguments
from selenium import webdriver

class Selsen(formats, xpaths, arguments):
    def __init__(self, browser, *args):
        self.browser = browser.lower()
        self.options = Options() 
        opt_args = ["current_session"]    
        for argument in args:
            if argument in opt_args:
                if argument == "current_session":
                    self.current_session()
            else:
                try:
                    if argument == "headless":
                        self.options.add_argument("--headless")
                    else:
                        self.options.add_argument(argument)
                except Exception as error:
                    print(f"argument not accepted: {error}")

        if self.browser == 'chrome': 
            self.driver = webdriver.Chrome(options = self.options)
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox(options = self.options)
        elif self.browser == "safari":
            self.driver = webdriver.Safari(options = self.options)
        elif self.browser == "ie" or self.browser == "internet explorer":
            self.driver = webdriver.Ie(options = self.options)
        else:
            raise ValueError("Unsupported browser")

    def open(self, url): 
        try:
            print(self.driver)
            if url.startswith("https://"):
                self.driver.get(url)
            else:
                self.driver.get(f"https://{url}")
        except Exception as error:
            print(f"error:{error}")

    def returnDriver(self): 
        return self.driver
    
    def close(self): 
        self.driver.quit()

