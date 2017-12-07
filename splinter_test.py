from splinter import Browser
from selenium.webdriver.common.keys import Keys

browser = Browser("firefox")

browser.visit("https://duckduckgo.com")
browser.fill("q", "the biggest python software house" + Keys.ENTER)
browser.is_element_present_by_css("a.result__a", wait_time=10)
browser.find_by_css("a.result__a")[1].click()
if browser.is_text_present:
    print "Yes"
else:
    print "No"