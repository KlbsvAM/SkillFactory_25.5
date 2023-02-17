# Проверка карточек питомцев
#python -m pytest -v --driver Chrome --driver-path C:\python\chromedriver_win32\chromedriver.exe test_all_pets.py
import pytest
from settings import valid_email, valid_password

def test_all_pets():


    #  неявное ожидание
    pytest.driver.implicitly_wait(10)

   # Вводим email
    pytest.driver.find_element_by_id('email').send_keys(valid_email)

   # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys(valid_password)

   # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


#python -m pytest -v --driver Chrome --driver-path C:\python\chromedriver_win32\chromedriver.exe test_all_pets.py