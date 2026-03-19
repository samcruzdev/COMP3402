from app import autenticar_usuario, saludar


def test_saludar():
    assert saludar("Ana") == "Hola, Ana"


def test_login_exitoso():
    resultado = autenticar_usuario("admin", "1234", 2.14)
    assert resultado["success"] == True
    assert resultado["error_id"] == ""
    assert resultado["response_time_ms"] < 500


def test_usuario_inexistente():
    resultado = autenticar_usuario("pedro", "1234", 3.05)
    assert resultado["success"] == False
    assert resultado["error_id"] == "user-not-exist"
    assert resultado["response_time_ms"] < 500


def test_contrasena_incorrecta():
    resultado = autenticar_usuario("pedro", "1234", 620)
    assert resultado["success"] == False
    assert resultado["error_id"] == "user-not-exist"
    assert resultado["response_time_ms"] < 500


def test_empty_fields():
    resultado = autenticar_usuario("pedro", "1234", 1.90)
    assert resultado["success"] == False
    assert resultado["error_id"] == "empty-fields"
    assert resultado["response_time_ms"] < 500
