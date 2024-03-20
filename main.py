import requests

def getcd():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:
        return response.json()

cryptoresponse = getcd()
user_input = input("Enter Your Crypto Currency: ")
for crypto in cryptoresponse:
     if crypto["currency"] == user_input:
         print(crypto["price"])
         break