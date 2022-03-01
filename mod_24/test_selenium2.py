import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def set_array(i, array):
   return array[i::4]

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome("chromedriver.exe")
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   #Неявное ожидание
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('sss1@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('123456789')

   # Нажимаем на кнопку входа в аккаунт
   login = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located
                                                  ((By.CSS_SELECTOR, 'button[type="submit"]')))
   login.click()

   #Нажимаем на выпадающий список
   dropdown = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located
                                                           ((By.CSS_SELECTOR, 'span.navbar-toggler-icon')))
   dropdown.click()

   #В выпадающем меню нажимаем на кнопку мои питомцы
   button_my_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located
                                                           ((By.LINK_TEXT, 'Мои питомцы')))
   button_my_pets.click()

   #Получаем кол-во питомцев из статистики
   pets = pytest.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]').text.split()
   pets = int(pets[3])
   #Получаем количество карточек питомцев
   pets_cards = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr')
   number_pets_cards = len(pets_cards)
   #1)Проверка то, что присутствуют все питомцы.
   assert pets == number_pets_cards

   #2)Проверка то, что хотябы у половины питомцев есть фото
   images = pytest.driver.find_elements_by_xpath('.//*[@id="all_my_pets"]/table/tbody/tr/th/img')
   with_images = 0
   for i in range(len(images)):
      no_imges = images[i].get_attribute('src')
      if no_imges != '':
         with_images += 1
   assert pets/2 <= with_images

   #3) Проверка то, что у всех питомцев есть имя, возраст и порода
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td')
   name_true = []
   for i in names:
      name_true.append(i.text)
   column_count = 4
   for i in range(column_count):
      if i == 0:
         name = set_array(i, name_true)
      elif i == 1:
         bread = set_array(i, name_true)
      elif i == 2:
         age = set_array(i, name_true)
      else:
         continue

   assert name.count('') == 0
   assert bread.count('') == 0
   assert age.count('') == 0

   #4-5)Проверка то, что у всех питомцев имя, возраст и порода разные
   assert len(list(name)) ==len(set(name))
   assert len(list(bread)) ==len(set(bread))
   assert len(list(age)) ==len(set(age))
