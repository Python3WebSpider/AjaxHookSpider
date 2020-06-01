from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://dynamic6.scrape.center/')
browser.execute_script(open('hook.js').read())
time.sleep(2)

for index in range(10):
    print('current page', index)
    btn_next = browser.find_element_by_css_selector('.btn-next')
    btn_next.click()
    time.sleep(2)
