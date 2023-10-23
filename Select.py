
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import time
## dependancy 
class formats():

    def find(self, type, value, selection="single"): #cz
            type, selection = type.lower(), selection.lower()
            if selection == "all" or selection == "many" or selection == "m":
                selection = True
            else:
                selection = False

            if type == "class_name" or type == "class":
                if selection:
                    return self.driver.find_elements(by=By.CLASS_NAME, value=value)
                else:
                    return self.driver.find_element(by=By.CLASS_NAME, value=value)
            elif type == "id":
                if selection:
                    return self.driver.find_elements(by=By.ID, value=value)
                else:
                    return self.driver.find_element(by=By.ID, value=value)
            elif type == "xpath" or type == "xp":
                if selection:
                    return self.driver.find_elements(by=By.XPATH, value=value)
                else:
                    return self.driver.find_element(by=By.XPATH, value=value)
            elif type == "link_text" or type == "ltext":
                if selection:
                    return self.driver.find_elements(by=By.LINK_TEXT, value=value)
                else:
                    return self.driver.find_elements(by=By.LINK_TEXT, value=value)
            elif type == "partial_link_text" or type == "pltext":
                if selection:
                    return self.driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=value)
                else:
                    return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=value)
            elif type == "tag_name" or type == "tag":
                if selection:
                    return self.driver.find_elements(by=By.TAG_NAME, value=value)
                else:
                    return self.driver.find_element(by=By.TAG_NAME, value=value)
            elif type == "class" or type == "class_name":
                if selection:
                    return self.driver.find_elements(by=By.CLASS_NAME, value=value)
                else:
                    return self.driver.find_element(by=By.CLASS_NAME, value=value)
            elif type == "css_selector" or type == "css":
                if selection:
                    return self.driver.find_elements(by=By.CSS_SELECTOR, value=value)
                else:
                    return self.driver.find_element(by=By.CSS_SELECTOR, value=value)
            else:
                print(f"{type} is not a valid selenium selector")
                return False
        
    def xpath(self, value, selection="single"): #cz
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.XPATH, value=value)
        else:
            return self.driver.find_element(by=By.XPATH, value=value)

    def css(self, value, selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.CSS_SELECTOR, value=value)
        else:
            return self.driver.find_element(by=By.CSS_SELECTOR, value=value)
        
    def class_name(self, value, selection = "single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.CLASS_NAME, value=value)
        else:
            return self.driver.find_element(by=By.CLASS_NAME, value=value)
        
    def id(self, value, selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.ID, value=value)
        else:
            return self.driver.find_element(by=By.ID, value=value)
        
    def name(self, value, selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.NAME, value=value)
        else:
            return self.driver.find_element(by=By.NAME, value=value)
        
    def ltext(self, value, selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.LINK_TEXT, value=value)
        else:
            return self.driver.find_element(by=By.LINK_TEXT, value=value)
        
    def pltext(self, value,selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.LINK_TEXT, value=value)
        else:
            return self.driver.find_element(by=By.LINK_TEXT, value=value)
        
    def tag(self, value, selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.TAG_NAME, value=value)
        else:
            return self.driver.find_element(by=By.TAG_NAME, value=value)
    
    def find_input(self, name="submit", selection="single",tag="Name"): #cz
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            if tag == "name":
                return self.driver.find_elements(by=By.XPATH, value=f"//input[@name='{name}']")
            else:
                return self.driver.find_elements(by=By.XPATH, value=f"//input[@{tag}='{name}']")

        else:
            if tag == "name":
                return self.driver.find_element(by=By.XPATH, value=f"//input[@name='{name}']")
            else:
                return self.driver.find_element(by=By.XPATH, value=f"//input[@{tag}='{name}']")



