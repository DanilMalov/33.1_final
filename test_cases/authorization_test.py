import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
from locators.authorization_conf import AuthorizationPage
from time import sleep


@pytest.fixture
def open_page(driver,config):
    # Открыть ссылку логина
    driver.get(config["url"]["page_auth"])

# Авторизация клиента по вкладке "Почта"

# 1. Авторизация с корректными данными
def test_authorization_mail_valid_data(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["email"])
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    sleep(0)
    # Проверяем, что мы перешли в личный кабинет с учетными данными
    assert driver.find_element(By.CLASS_NAME, 'card-title').text == "Учетные данные"

# 2. Авторизация с некорректным паролем
def test_authorization_mail_invalid_data(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["email"])
    # Вводим невалидный password в поле password
    ap.password.send_keys(config["auth"]["invalid_data"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"

# 3. Авторизация с пустыми полями ввода
def test_empty_lines_email(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Пропускаем ввод данных
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"


# 4. Авторизация с пустым полем Пароля
def test_empty_password(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["email"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
    

# 5. Авторизация с 260 символами в полем Почта
def test_260_symbols_email(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["email260"])
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"

# 6. Авторизация с спецсимволами в полем Почта
def test_special_characters_email(driver, open_page, config):
    # Ожидаем появления вкладки почта
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку email
    ap.email_btn.click()
    # Вводим email в поле username
    ap.username.send_keys(config["auth"]["symbols"])
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"


# ---------------------------------------------------
# Авторизация клиента по вкладке 'Телефон'

# 7. Авторизация с корректными данными
def test_authorization_phone_valid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку телефон
    ap.phone_btn.click()
    # Вводим телефон
    ap.username.send_keys(config.get("auth", "phone2"))
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверяем, что мы перешли в личный кабинет с учетными данными
    assert driver.find_element(By.CLASS_NAME, 'card-title').text == "Учетные данные"


# 8. Авторизация с сиволами в поле Номер
def test_symbols_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку телефон
    ap.phone_btn.click()
    # Вводим телефон
    ap.username.send_keys(config["auth"]["invalid_data"])
    # Вводим password в поле password
    ap.password.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"


# 9. Авторизация с пустыми полями ввода
def test_empty_lines_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    # Создаём объект класса AuthorizationPage с описанием всех локаторов
    ap = AuthorizationPage(driver)
    # Нажимаем на вкладку телефон
    ap.phone_btn.click()
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем на кнопку Войти
    ap.login_btn.click()
    # Проверка того мы остались на странице авторизации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Авторизация"
