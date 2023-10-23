Selenium-Sensei: Functions 
------------------------------------
all functions must be called off a Selsen object

or specified directly from the class

Instantiation:
--------
The class can be instantiated as normal with arguments being passed in string format:

.. code:: python

  wrapper = Selsen("chrome","headless","another argument")


arguments:
--------
- "current_session"
- "headless"
- "another one"

Input and output:
--------
- .Open(url)

  Function dedicated to opening url given a web driver:
  wrapper for the .get() method

- .Close()

  Closes current browser session
  wrapper for .quit() method

- .returnDriver()

  Returns the current base Selenium web driver from the Selsen object
  therefore removing SeleniumSensei functionality:

    

Raw Selenium Usage:
--------
To escape the wrapper and use traditional selenium functions the web driver is included inside class attributes
this can be called from the class and then used to run functions:

.. code:: python

    wrapper = Selsen("chrome")
    type(wrapper.driver)
    # <class 'selenium.webdriver.chrome.webdriver.WebDriver'>

    wrapper.driver.back()
    # calling selenium function to return to the previous page

    wrapper.driver.quit()
    # quit the webdriver therefore also ending the Selsen browser session


Selectors:
--------
All selectors include the ability to select multiple elements using the selection parameter: 

- .find(type, value, selection="single")

      Given a valid Selenium locator will return any or a single element that matches the given value:
      for a list of valid Locators refer to `Select.py <Select.py>`_

      wrapper.find("id","32","m")

- .xpath(value, selection="single")

      Given a Valid XPath expression will return one or more matches:

      wrapper.xpath("//div","m")
    
- .css(value, selection="single")

    Given a Valid CSS Selector expression will return one or more matches:
  
    wrapper.css("name")

- .class_name(value, selection = "single")

    Given a Valid Class name will return one or more matches:
      
    wrapper.class_name("row", "many")

- .id(value, selection="single")

    Given a Valid ID will return one or more matches:
      
    wrapper.id("name")

- .name(value,selection="single")

    Given a Valid name will return one or more matches:
      
    wrapper.name("name")

- .ltext(value,selection="single")

    Given link text expression will return one or more matches:
      
    wrapper.ltext("Welcome")

- .pltext(value,selection="single")

    Given Partial link text will return one or more matches:
      
    wrapper.pltext("come")

- .tag(value, selection="single")

    Given a Valid tag @ will return one or more matches:
      
    wrapper.tag("type")

- .find_input(name="submit", selection="single",tag="Name")

    Given a Valid tag and value pair within an input will return one or more matches:

    the default value for the tag is assumed to be "name" if none is given
    
    wrapper.find_input("name")



XPath Selectors:
--------
- .xpath_tag(tag,value,selection="single")

    Matches a tag and value pair for a web element:

    wrapper.xpath_tag("name","box")

- .text_match_any(text,selection="single")

    Matches any occurrence of text within an element:

    wrapper.text_match_any("walking")

- .text_match(text,selection="single")

    Matches the exact text value in an element:

    wrapper.text_match_any("He was walking")

- .link_endingwith(text,selection="single")

    Matches the end of a link in a web element

    wrapper.link_endingwith(".pdf")

- .startingwith(self,tag,text,selection="single")

    Matches the start of a link in a web element:

    wrapper.link_startswith("important")

- .endingwith(tag,text,selection="single")

    Matches the end of a tag in a web element

    wrapper.endingwith("name")

- .id_from_class(cls, id, selection="single")

    Matches a specific id from a class, useful when many similar id's exist

    wrapper.id_from_class("row_14","3")

- .xpath_and(res1, res2, selection="single")

    AND operation on two XPath expressions returning any elements that are in both

    wrapper.xpath_and("//div","[@id='8192']")
  



