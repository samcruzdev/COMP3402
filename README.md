# COMP3402

## Actividad - Pruebas Funcionales de Software | Resultado de pruebas (`pytest`)

![Resultado](images/resultado#1.png)

- **Total:** 5 pruebas
- **Pasaron (3):**
  - `test_saludar`
  - `test_login_exitoso`
  - `test_usuario_inexistente`
- **Fallaron (2):**
  - `test_contrasena_incorrecta`: se esperaba `response_time_ms < 500`, pero llegó `620`.
  - `test_empty_fields`: se esperaba `error_id == "empty-fields"`, pero devolvió `"user-not-exist"`.

## Causa resumida

1. `test_contrasena_incorrecta` falla porque el tiempo de respuesta (`620`) supera el límite esperado (`< 500`).
2. `test_empty_fields` falla porque el test no envía campos vacíos (`"pedro"` y `"1234"` tienen contenido), por eso no retorna `"empty-fields"`.
