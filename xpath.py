from selenium.webdriver.common.by import By



## dependancy 
class xpaths():
    def xpath_tag(self,tag,value,selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m": 
            return self.driver.find_elements(by=By.XPATH, value=f"//*[contains(@{tag},'{value}')]")
        else:
            return self.driver.find_element(by=By.XPATH, value=f"//*[contains(@{tag},'{value}')]")
    
    def text_match_any(self,text,selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m": 
            return self.driver.find_elements(by=By.XPATH, value=f"//*[contains(text(), '{text}')]")
        else:
            return self.driver.find_element(by=By.XPATH, value=f"//*[contains(text(), '{text}')]")

    def text_match(self,text,selection="single"): #cz
        if selection == "all" or selection == "many" or selection == "m": 
            return self.driver.find_elements(by=By.XPATH, value=f"//*[text()='{text}']")
        else:
            return self.driver.find_element(by=By.XPATH, value=f"//*[text()='{text}']")
    
    def link_endingwith(self,text,selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.XPATH, value=f"//*[ends-with(@href, '{text}')]")
        else:
            return self.driver.find_element(by=By.XPATH, value=f"//*[ends-with(@href, '{text}')]")
    
    def startingwith(self,tag,text,selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.XPATH, value=f"//div[starts-with(@{tag}, '{text}')]")
        else:
            return self.driver.find_element(by=By.XPATH, value=f"//div[starts-with(@{tag}, '{text}')]")
    
    def endingwith(self,tag,text,selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.XPATH, value=f"//*[ends-with(@{tag}, '{text}')]")
        else:
            return self.driver.find_element(by=By.XPATH, value=f"//*[ends-with(@{tag}, '{text}')]")

    def id_from_class(self, cls, id,selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.XPATH, value=f"//*[@class='{cls}'][@id='{id}']")
        else:
            return self.driver.find_element(by=By.XPATH, value=f"//*[@class='{cls}'][@id='{id}']")

    def xpath_and(self,res1,res2,selection="single"):
        selection = selection.lower()
        if selection == "all" or selection == "many" or selection == "m":
            return self.driver.find_elements(by=By.XPATH, value=f"//*[{res1}][{res2}]")
        else:
            return self.driver.find_element(by=By.XPATH, value=f"//*[{res1}][{res2}]")

