from zeep import Settings, Client

url = "https://speller.yandex.net/services/spellservice?WSDL"
settings = Settings(strict=False)
client = Client(wsdl=url, settings=settings)
print(client.service.checkText("Table"))