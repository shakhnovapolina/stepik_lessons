from selenium import webdriver
from sys import argv
import time

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//div[@class='first_block']/div/input[contains(@class, 'first')]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//div[@class='first_block']/div/input[contains(@class, 'second')]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//div[@class='first_block']/div/input[contains(@class, 'third')]")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_xpath("//div[@class='second_block']/div/input[contains(@class, 'first')]")
    input4.send_keys("Russia")
    input5 = browser.find_element_by_xpath("//div[@class='second_block']/div/input[contains(@class, 'second')]")
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()