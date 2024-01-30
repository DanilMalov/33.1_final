import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
from locators.registr_conf import Registration, BtnReg

from time import sleep
import configparser


@pytest.fixture
def open_page(driver, config):
    # Открыть ссылку логина
    driver.get(config["url"]["page_auth"])


# 14 Регистрация с корректными данными
def test_registration_valid_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["name"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["surname"])
    # Вводим почту
    reg.address.send_keys("maksim.malov1095@mail.ru")
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем что мы перешли на страницу c надписью Подтверждение email
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Подтверждение email"


# 15 Регестрация с пустыми полями личных данных
def test_registration_lines_data(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Пропускаем все поля ввода
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"


# 16 Регестрация с пустыми полями Имени и Фамилии
def test_registration_lines_name(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект классs BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Пропускаем ввод Имени и Фамилии
    # Вводим почту
    reg.address.send_keys(config["auth"]["email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"


# 17 Регестрация с некрректной почтой
def test_registration_invalid_email(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["name"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["surname"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["invalid_email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем что мы перешли на страницу c надписью Подтверждение email
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Подтверждение email"
    # Тест проходит такого быть не должно БАГ


# 18 Регистрация с вводом цифор поле Имя и Фамилия
def test_registration_numbers_name(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["phone1"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["phone1"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"


# 19 Регистрация с вводом 260 символов в поля Имя и Фамилия
def test_registration_260_name(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["email260"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["email260"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"


# 20 Регистрация с вводом спецсимволов в поля Имя и Фамилия
def test_registration_special_characters_name(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["symbols"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["symbols"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["email"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем, что мы остались на странице регистрации
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"


# Регестрация по телефону
# 21 Регистрация с корректными данными
def test_recovery_mail_valid_phone(driver, open_page, config):
    wdw(driver, 8).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    # Создаём объект класса BtnReg с описанием всех локаторов
    br = BtnReg(driver)
    # Нажимаем Зарегестрироватся
    br.regist.click()
    # Создаём объект класса Registration с описанием всех локаторов
    reg = Registration(driver)
    # Вводим Имя
    reg.name_first.send_keys(config["auth"]["name"])
    # Вводим фамилию
    reg.surname_last.send_keys(config["auth"]["surname"])
    # Вводим почту
    reg.address.send_keys(config["auth"]["phone1"])
    # Вводим пароль
    reg.password.send_keys(config["auth"]["password"])
    # Вводим пароль повторно
    reg.password_confirm.send_keys(config["auth"]["password"])
    # Время для ввода символов с картинки
    sleep(0)
    # Нажимаем кнопку Зарегестрироватся
    reg.register_btn.click()
    # Проверяем что мы перешли на страницу c надписью Подтверждение email
    assert driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Подтверждение телефона"