import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given('que el administrador ha iniciado sesión y accede a la página de actualización de análisis')
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

    try:
        select_element = wait.until(EC.presence_of_element_located((By.ID, "muestraSelect")))
        select = Select(select_element)
        select.select_by_visible_text("Muestra 3")
        time.sleep(2)
    except TimeoutException:
        raise AssertionError(f"No se encontró el select 'muestraSelect' en la URL: {context.driver.current_url}")

@when('completa el formulario de actualización de análisis de suelo con datos válidos')
def step_impl(context):
    time.sleep(2)
    d = context.driver

    def clear_and_fill(element_id, value):
        elem = d.find_element(By.ID, element_id)
        elem.clear()
        elem.send_keys(value)

    clear_and_fill("id_fRec", "08-06-2025")
    clear_and_fill("id_fEje", "08-06-2025")
    clear_and_fill("id_fEmi", "08-06-2025")
    clear_and_fill("id_tipoCultivo", "Trigo")

    time.sleep(2)

@when('envía el formulario de actualización')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    try:
        save_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Guardar cambios')]"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", save_button)
        time.sleep(1)
        save_button.click()
        time.sleep(5)
    except TimeoutException:
        raise AssertionError("No se encontró el botón 'Guardar cambios' en la página.")

@then('el sistema guarda los datos del análisis actualizado')
def step_impl(context):
    assert "analisis" in context.driver.current_url, f"URL inesperada después de guardar los datos: {context.driver.current_url}"
    time.sleep(5)
    context.driver.quit()
