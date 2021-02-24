import requests


def suma_fake(function):
    def wrapper(num):
        if num % 2 == 0:
            return function(num)
        else:
            num = 4
            return function(num)
    return wrapper


def consulta_continente(function):
    def wrapper(continente):
        if continente == "asia":
            response = requests.get(f"https://restcountries.eu/rest/v2/region/{continente}")
            print(
                response.content
            )
        else:
            return function()
    return wrapper

def formatear_base_de_datos(function):
    def wrapper(lista):
        if "base de datos" in lista:
            print("Base de datos formateada!")
            return function(lista)
        
        else:
            return function(lista)
    return wrapper
            
def formatear_sistema(function):
    def wrapper(lista):
        if "sistema" in lista:
            print("Solo se ha formateado el sistema")
        else:
            return function(lista)
    return wrapper