from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.elinsolheim.dk/blog/blog/glade-og-staerke-foedder")

nav = browser.find_element_by_class_name("learnworlds-section-content")

print(nav.text)
