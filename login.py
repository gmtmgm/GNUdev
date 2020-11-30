from selenium import webdriver
import requests

user_id = " "
user_pw = " "

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.implicitly_wait(2)
driver.get('https://e-campus.gnu.ac.kr/main/MainView.dunet')

id_elem = driver.find_element_by_name('id')
pw_elem = driver.find_element_by_name('pass')

driver.find_element_by_id('pop_login').click()
id_elem.send_keys(user_id)
pw_elem.send_keys(user_pw)
driver.find_element_by_id('login_img').click()

s = requests.Session()

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
s.headers.update(headers)

for cookie in driver.get_cookies():
    c = {cookie['name'] : cookie['value']}
    s.cookies.update(c)

menu = driver.find_element_by_xpath('//*[@id="gnbmenu"]/ul/li[3]/a')

actions = webdriver.ActionChains(driver).move_to_element(menu)
actions.perform()

driver.implicitly_wait(1)

driver.get('https://e-campus.gnu.ac.kr/lms/myLecture/doListView.dunet')
