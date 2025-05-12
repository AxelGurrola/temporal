import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  


@given('que el administrador está en la página de inicio de sesión')
def step_open_login_page(context):
    context.browser = webdriver.Chrome()  
    context.browser.get("http://localhost:8000/login")  

@when('ingresa usuario y contraseña válidos')
def step_enter_valid_credentials(context):
    context.browser.get('http://localhost:8000/login/')  
    wait = WebDriverWait(context.browser, 10)

    
    usuario_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = context.browser.find_element(By.NAME, "password")
    
    usuario_input.send_keys("jaime")      
    password_input.send_keys("Mr2liedt")  

    
    boton_login = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    boton_login.click()


@then("el sistema permite el acceso al panel de administración")
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)  
    boton_insertar = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Insertar Análisis')]"))
    )
    assert boton_insertar.is_displayed(), "El botón 'Insertar Análisis' no está visible. Login fallido."
    
    time.sleep(30)



@when('ingresa usuario y contraseña inválidos')
def step_enter_invalid_credentials(context):
    wait = WebDriverWait(context.browser, 10)
    
    
    usuario_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = context.browser.find_element(By.NAME, "password")
    
    usuario_input.send_keys("usuario_incorrecto")  
    password_input.send_keys("contraseña_incorrecta")  

  
    boton_login = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    boton_login.click()


@then('el sistema sigue mostrando el formulario de inicio de sesión')
def step_verify_login_form(context):
    wait = WebDriverWait(context.browser, 10)

    
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    
    
    assert username_input.is_displayed(), "El campo de usuario no está visible."
    assert password_input.is_displayed(), "El campo de contraseña no está visible."
    
    
    current_url = context.browser.current_url
    assert "/login" in current_url, f"La URL cambió inesperadamente a {current_url}. Debería permanecer en /login."
    
    time.sleep(3)
    context.browser.quit()



@then('el sistema no permite el acceso al panel de administración')
def step_verify_no_admin_access(context):
    wait = WebDriverWait(context.browser, 10)
    
    
    try:
        current_url = context.browser.current_url
        assert "/login" in current_url, f"El sistema permitió el acceso al panel de administración. URL: {current_url}"
    except TimeoutException:
        raise AssertionError("La URL no se actualizó correctamente después de un intento de login fallido.")
    
    time.sleep(3)  
    context.browser.quit()
