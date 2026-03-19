def saludar(nombre):
    return f"Hola, {nombre}"


def autenticar_usuario(username, password, ms):
    hardcoded_username = "admin"
    hardcoded_password = "1234"


    result = { "success": False, "error_id": "", "response_time_ms": 0 }
    result["response_time_ms"] = ms

    if (username == "" or password == "")
        result["error_id"] = "empty-fields"

        return result

    if (username != hardcoded_username):
        result["error_id"] = "user-not-exist"
        return result

    if (password != hardcoded_password):
        result["error_id"] = "incorrect-password"
        return result

    result["success"] = True
    return result
