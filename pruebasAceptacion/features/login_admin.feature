# language: es
Característica: Inicio de sesión del administrador

  El administrador puede iniciar sesión con credenciales válidas

  Escenario: Inicio de sesión exitoso del administrador
    Dado que el administrador está en la página de inicio de sesión
    Cuando ingresa usuario y contraseña válidos
    Entonces el sistema permite el acceso al panel de administración

  Escenario: Inicio de sesión con usuario inválido
    Dado que el administrador está en la página de inicio de sesión
    Cuando ingresa usuario y contraseña inválidos
    Entonces el sistema sigue mostrando el formulario de inicio de sesión

  Escenario: No acceso al panel con usuario inválido
    Dado que el administrador está en la página de inicio de sesión
    Cuando ingresa usuario y contraseña inválidos
    Entonces el sistema no permite el acceso al panel de administración
