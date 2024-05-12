import requests
import time

def fazer_requisicao():
    url = "http://localhost:8080/transfer"

    payload = {'amount': '200'}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Requisicao deu bom")
    else:
        print("Requisicao deu ruim")

    
interfavlo_de_tempo = 10

while True:
    fazer_requisicao()
    time.sleep(interfavlo_de_tempo)