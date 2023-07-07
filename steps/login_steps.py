from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('el usuario está registrado')
def step_impl(context):
   pass

@when('cuando introduce un nombre de usuario')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://the-internet.herokuapp.com/login")
    context.driver.find_element(By.ID, "username").send_keys("tomsmith")

@when('cuando introduce su password')
def step_impl(context):
    context.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

@when('el usuario pulsa "Go"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#login > button").click()

@then('el usuario accede al portal')
def step_impl(context):
   assert context.driver.find_element(By.CSS_SELECTOR, "#content > div > a:nth-child(3)").is_displayed()
   context.driver.quit()