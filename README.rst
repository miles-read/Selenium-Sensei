
Selenium-Sensei
------------------------------------

|PY ver|


SeleniumSensei is a simple Selenium wrapper using python built to simplify and speed up the web automation process. 

The latest documentation for Selenium is available at:
`https://www.selenium.dev <https://www.selenium.dev/selenium/docs/api/py/api.html>`_.

.. |PY ver| image:: https://raw.githubusercontent.com/gist/miles-read/5dfaba045278dcd7759301f9f6cdf502/raw/bad7260ff6ff4ddbd222724f96eca3eddb01b06a/PY%20ver.svg

Features
--------
- Simple and easy to use with all functions callable from a single class
- Full access to Selenium web drivers
- Simplified XPATH execution through templates
- Automatic configuration of experimental arguments
- Code is easily adaptible for custom use-cases
- Lightweight and efficient

Example Setup
-----------------

An example browser session:

.. code:: python

   from SeleniumSensei import wrapper
   browser = Selsen("chrome")
   browser.open('www.google.com')
   browser.close()

Using the "current_session" argument to load a logged-in session:

.. code:: python

   from SeleniumSensei import wrapper

   browser = Selsen("chrome","current_session")
   browser.open('www.office.com/?auth=2')
   browser.text_match(self,"Welcome to Microsoft 365",selection="single")
   browser.close()

   type(browser.driver)
   #<class 'selenium.webdriver.chrome.webdriver.WebDriver'>

General
-------

* `Installation <INSTALLATION.rst>`_

* `Functions <FUNCTIONS.rst>`_

* `Arguments <ARGUMENTS.rst>`_

* `License <LICENSE>`_

If you have any questions you can contact me via:
readmiles00@gmail.com
