import requests

class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        response = requests.get(f"https://restcountries.eu/rest/v2/region/{object_instance.nombre}")
        print(f"Status code: {response.status_code}")
        print(response.content)
        if response == "europa":
            print("proxy actuando... Europe")
            return True

        elif object_instance.nombre == "asia":
            print("proxy actuando... Asia")
            return True

        elif object_instance.nombre == "americas":
            print("proxy actuando... Americas")
            return True

        return False

