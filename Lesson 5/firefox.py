from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

"""Задание 3. Клик по кнопке
Шаги:
1. Откройте страницу: http://the-internet.herokuapp.com/add_remove_elements/.
2. Пять раз кликните на кнопку:`Add Element`.
3. Соберите со страницы список кнопок:`Delete`.
4. Выведите на экран размер списка."""
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    driver.find_element(By.CSS_SELECTOR, "[onclick='addElement()']").click()
    delete = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    print(len(delete))
driver.quit()


"""Задание 4. Клик по кнопке без ID
Шаги:
1. Откройте страницу: http://uitestingplayground.com/dynamicid.
2. Кликните на синюю кнопку.
3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково."""
for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

driver.quit()


"""Задание 5. Клик по кнопке с CSS-классом
Шаги:
1. Откройте страницу: http://uitestingplayground.com/classattr.
2. Кликните на **синюю** кнопку.
3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково."""
for i in range(3):
    driver.get("http://uitestingplayground.com/classattr")
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

driver.quit()


"""Задание 6. Модальное окно
Шаги:
1. Откройте страницу: http://the-internet.herokuapp.com/entry_ad.
2. В модальном окне нажмите на кнопку: `Сlose`."""
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)
driver.find_element(By.CSS_SELECTOR, '#modal .modal-footer p').click()

driver.quit()


"""Задание 7. Поле ввода
Шаги:
1. Откройте страницу: http://the-internet.herokuapp.com/inputs.
2. Введите в поле текст: `1000`.
3. Очистите это поле (метод `clear`).
4. Введите в это же поле текст:`999`."""
driver.get("http://the-internet.herokuapp.com/inputs")
text = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
text.send_keys("1000")
sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[type='number']").clear()
sleep(5)
text.send_keys("999")
driver.quit()


"""Задание 8. Форма авторизации
Шаги:
1. Откройте страницу: http://the-internet.herokuapp.com/login.
2. В поле username введите значение: `tomsmith`.
3. В поле password введите значение: `SuperSecretPassword!`.
4. Нажмите кнопку: `Login`."""
driver.get("http://the-internet.herokuapp.com/login")
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
username.send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
driver.quit()
