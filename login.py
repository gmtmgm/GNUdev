from selenium import webdriver

user_id = " "
user_pw = " "

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://e-campus.gnu.ac.kr/main/MainView.dunet')

id_elem = driver.find_element_by_name('id')
pw_elem = driver.find_element_by_name('pass')

driver.find_element_by_id('pop_login').click()
id_elem.send_keys(user_id)
pw_elem.send_keys(user_pw)
driver.find_element_by_id('login_img').click()

driver.implicitly_wait(3)
driver.get('https://e-campus.gnu.ac.kr/lms/myLecture/doListView.dunet')