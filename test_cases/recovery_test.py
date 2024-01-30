import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
from locators.recovery_conf import Recovery
from time import sleep



@pytest.fixture
def open_page(driver,config):
    # Открыть ссылку логина
    driver.get(config["url"]["page_activation"])



# 10 Восстановление пароля с корректными данными
def test_recovery_valid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса Recovery с описанием всех локаторов
    rec = Recovery(driver)
    # Нажимаем на вкладку телефон
    rec.phone_btn.click()
    # Вводим телефон
    rec.username.send_keys(config["auth"]["phone2"])
    # Время для ввода символов с картинки
    sleep(20)
    # Нажимаем на кнопку Продолжить
    rec.continue_btn.click()
    sleep(0)
    # Проверяем, что мы перешли на страницу активации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == ("Восстановление "
                                                                                "пароля")


# 11 Восстановление пароля с несуществующим номером телефона
def test_recovery_invalid_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса Recovery с описанием всех локаторов
    rec = Recovery(driver)
    # Нажимаем на вкладку телефон
    rec.phone_btn.click()
    # Вводим телефон
    rec.username.send_keys(config["auth"]["invalid_phone"])
    # Время для ввода символов с картинки
    sleep(20)
    # Нажимаем на кнопку Продолжить
    rec.continue_btn.click()
    # Проверяем, что мы перешли на страницу активации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == ("Восстановление "
                                                                                "пароля")
    # БАГ


# Восстановление пароля с помощью Почты

# 12 Восстановление пароля с корректными данными
def test_recovery_mail_valid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса Recovery с описанием всех локаторов
    rec = Recovery(driver)
    # Нажимаем на вкладку Почта
    rec.email_btn.click()
    # Вводим телефон
    rec.username.send_keys(config["auth"]["email"])
    # Время для ввода символов с картинки
    sleep(20)
    # Нажимаем на кнопку Продолжить
    rec.continue_btn.click()
    # Проверяем, что мы перешли на страницу активации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == ("Восстановление "
                                                                                "пароля")

# 13 Восстановление пароля с незарегестрированной почтой
def test_recovery_mail_invalid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса Recovery с описанием всех локаторов
    rec = Recovery(driver)
    # Нажимаем на вкладку Почта
    rec.email_btn.click()
    # Вводим телефон
    rec.username.send_keys(config["auth"]["invalid_email"])
    # Время для ввода символов с картинки
    sleep(20)
    # Нажимаем на кнопку Продолжить
    rec.continue_btn.click()
    # Проверяем, что мы перешли на страницу активации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == ("Восстановление "
                                                                                "пароля")

