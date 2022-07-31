import json

def registration(login, password):
    file_name = "AccountData.json"
    with open(f"database/{file_name}", "r") as fileJson:
        data = json.load(fileJson)

    error_autorisation = "Такой аккаунт уже существует!\nАвторизируйтесь или создайте новый аккаунт."

    if login == "" or password == "":
        return [False ,"Заполните ячейку!"]
    if login in data:
        return [False, error_autorisation]

    data[login] = {"password":password}

    with open(f"database/{file_name}", "w") as fileJson:
        json.dump(data, fileJson)

    return [True, ""]

def autorisation(login, password):
    file_name = "AccountData.json"
    with open(f"database/{file_name}") as fileJson:
        data = json.load(fileJson)

    try:
        if data[login]["password"] == password:
            return True
    except:
        return False

def addAccount(main_login, name, site, login, password):
    file_name = "AccountData.json"
    with open(f"database/{file_name}") as fileJson:
        data = json.load(fileJson)

    addInformation = {"site" : site, "login" : login, "password_" : password}

    data[main_login]["accounts"][name] = addInformation

    with open(f"database/{file_name}", "w") as fileJson:
        json.dump(data, fileJson)
