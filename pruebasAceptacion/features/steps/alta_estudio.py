import time
import os
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



@given('que el administrador ha iniciado sesión en el sistema')
def step_impl(context):
    context.driver = webdriver.Chrome()  
    context.driver.get("http://localhost:8000/login")  

    
    wait = WebDriverWait(context.driver, 10)
    
    
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = context.driver.find_element(By.NAME, "password")
    
    
    username_input.send_keys("admin")  
    password_input.send_keys("Mr2liedt")  
    time.sleep(2)
    
    
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    login_button.click()
    time.sleep(2)

    
    wait.until(EC.url_changes("http://localhost:8000/login"))
    time.sleep(3)

    
    try:
        
        insert_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Insertar Análisis')]")))
        assert insert_button.is_displayed(), "El botón 'Insertar Análisis' no está visible. Redirección fallida."
        insert_button.click()
        time.sleep(2)  
    except TimeoutException:
        raise AssertionError(f"No se encontró el botón de 'Insertar Análisis' en la URL: {context.driver.current_url}")


@when('completa el formulario de análisis de suelo con datos válidos')
def step_impl(context):
    time.sleep(2)
    d = context.driver
    time.sleep(2)
    
    
    wait = WebDriverWait(d, 10)
    time.sleep(2)
    
    
    d.find_element(By.ID, "id_fRec").send_keys("08-05-2025")
    d.find_element(By.ID, "id_fEje").send_keys("08-05-2025")
    d.find_element(By.ID, "id_fEmi").send_keys("08-05-2025")
    d.find_element(By.ID, "id_tipoCultivo").send_keys("Maíz")
    d.find_element(By.ID, "id_peso").send_keys("1.5")
    d.find_element(By.ID, "id_profundidad").send_keys("20")
    d.find_element(By.ID, "id_localidad").send_keys("Valle")
    d.find_element(By.ID, "id_coordenadas").send_keys("12.34,56.78")
    d.find_element(By.ID, "id_predio").send_keys("Predio A")
    d.find_element(By.ID, "id_tipoAgri").send_keys("Orgánica")
    d.find_element(By.ID, "id_claseTex").send_keys("Franco")
    d.find_element(By.ID, "id_sat").send_keys("50")
    d.find_element(By.ID, "id_capCampo").send_keys("45")
    d.find_element(By.ID, "id_pmp").send_keys("30")
    d.find_element(By.ID, "id_conHidra").send_keys("1.2")
    d.find_element(By.ID, "id_densApa").send_keys("1.3")
    d.find_element(By.ID, "id_ph").send_keys("6.5")
    d.find_element(By.ID, "id_phB").send_keys("6.8")
    d.find_element(By.ID, "id_salinidad").send_keys("0.5")
    d.find_element(By.ID, "id_reqYeso").send_keys("Ninguno")
    d.find_element(By.ID, "id_reqCal").send_keys("Moderado")
    d.find_element(By.ID, "id_carbtotal").send_keys("2.1")
    d.find_element(By.ID, "id_det").send_keys("Nitrógeno")
    d.find_element(By.ID, "id_res").send_keys("15")
    d.find_element(By.ID, "id_unidad").send_keys("mg/kg")
    d.find_element(By.ID, "id_cation").send_keys("Calcio")
    d.find_element(By.ID, "id_cons").send_keys("1.5")
    d.find_element(By.ID, "id_porcentaje").send_keys("20")
    time.sleep(2)


@when('envía el formulario')
def step_impl(context):
    
    save_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Guardar Datos']"))
    )
    
    
    context.driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
    time.sleep(3)  

    
    save_button.click()
    time.sleep(5)  


@then('el sistema guarda los datos del análisis')
def step_impl(context):
    
    assert "analisis" in context.driver.current_url, f"URL inesperada después de guardar los datos: {context.driver.current_url}"
    time.sleep(5)

    
    context.driver.quit()