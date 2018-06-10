import base64
import requests
import json
from Crypto.Cipher import AES

IV = "YC'2bmK=b%#NQ?9j"
KEY = "KCH@LQj#>6VCqqLg"
URL = "http://lh58.hotgram.ir/v1/proxy"

def get_proxy(IV, KEY, URL):
    response = requests.get(URL).text
    b64_encrypted_proxy = json.loads(response).get("data")[0]
    enc = base64.b64decode(b64_encrypted_proxy)
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    s = cipher.decrypt(enc)
    return s[:-ord(s[len(s)-1:])]

if __name__ == "__main__":
    decoded_proxy = get_proxy(IV, KEY, URL)
    parsed_output = json.loads(decoded_proxy)
    print(json.dumps(parsed_output, indent=4))

