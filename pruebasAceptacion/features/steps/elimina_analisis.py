import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given('que el administrador ha iniciado sesión y accede a la página de análisis de suelo')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/login")
    wait = WebDriverWait(context.driver, 10)

    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = context.driver.find_element(By.NAME, "password")
    username_input.send_keys("jaime")
    password_input.send_keys("Mr2liedt")
    time.sleep(2)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    login_button.click()
    time.sleep(2)

    wait.until(EC.url_changes("http://localhost:8000/login"))
    time.sleep(3)

@when('selecciona la muestra "Muestra 3" para eliminar')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        
        select_element = wait.until(EC.presence_of_element_located((By.ID, "eliminarMuestraSelect")))
        time.sleep(3)  

        select = Select(select_element)
        select.select_by_visible_text("Muestra 3")
        time.sleep(3)  

        
        alert = context.driver.switch_to.alert
        alert.accept()
        time.sleep(5)  
    except TimeoutException:
        raise AssertionError("No se encontró el select 'eliminarMuestraSelect' o no apareció la alerta.")

@then('el sistema elimina el análisis')
def step_impl(context):
    try:
        assert context.driver.current_url.endswith("/analisis/"), \
            f"La URL final esperada era /analisis/, pero fue: {context.driver.current_url}"
        time.sleep(3)  
    finally:
        context.driver.quit()
