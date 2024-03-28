""" 1. Открыть страницу http://google.com/ncr
2. Выполнить поиск слова “selenide”
3. Проверить, что первый результат – ссылка на сайт selenide.org.
4. Перейти в раздел поиска изображений
5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
6. Вернуться в раздел поиска Все
7. Проверить, что первый результат такой же, как и на шаге 3.

Если с гуглом будут проблемы, можно выбрать любой другой поисковик. Браузер - по своему выбору.

Свежий вэбдрайвер для Chrome можно скачать по следующей ссылке: https://chromedriver.chromium.org/downloads
"""

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
#Импорт команд управления с клавиатуры
from selenium.webdriver.common.keys import Keys
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# импортируем для паузы
import time
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
time.sleep(2)

# 1. Открыть страницу http://google.com/ncr (Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке)
driver.get("http://google.com/ncr")
time.sleep(2)

# 2. Выполнить поиск слова “selenide”
search_field = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
search_field.send_keys("Selenide")
time.sleep(2)
search_button = driver.find_element(By.XPATH, "//input[@class='gNO89b']")
search_button.click()
time.sleep(2)

# 3.проверяем что первая ссылка - selenide.org
find_urls = driver.find_elements(By.TAG_NAME, "cite")[0]
find_url = find_urls.text
assert "selenide.org" in find_url, "ссылка НЕ на selenide.org"
time.sleep(5)

# 4.Перейти в раздел поиска изображений
search_picture = driver.find_element(By.XPATH, "//span[@class='FMKtTb UqcIvb']")
time.sleep(5)

# 5.Проверить, что первое изображение неким образом связано с сайтом selenide.org(на этом шаге я получаю ошибку, но не понимаю почему, все кажется правильным)
find_pictures = driver.find_elements(By.XPATH,  "//div[@class='LAA3yd']")[0]
find_pict = find_pictures.text
assert "selenide.org" in find_pict, "картинка никак не связана с selenide.org"
time.sleep(5)

# 6.Вернуться в раздел поиска Все
driver.back()

# 7.Проверить, что первый результат такой же, как и на шаге 3
find_urls_new = driver.find_elements(By.TAG_NAME, "cite")[0]
find_url_new = find_urls_new.text
assert find_url_new == find_url, "первый результат НЕ такой же, как и на шаге 3"
time.sleep(5)

driver.close()
driver.quit()

"""
В будущем командой time.sleep(...) лучше не злоупотреблять, 
им на замену использовать явное ожидание WebDriverWait (ссылка: https://www.geeksforgeeks.org/waits-in-selenium-python/)
"""
