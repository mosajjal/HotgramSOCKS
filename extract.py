# THIS FILE IS NOT MINE. IT'S JUST COPY AND PASTE ;)
import base64
import requests
import json
from random import randint
from Crypto.Cipher import AES

IV = "YC'2bmK=b%#NQ?9j"
KEY = "KCH@LQj#>6VCqqLg"
HOST = f"lh{randint(1,80)}.hotgram.ir"
URL = f"http://{HOST}/v1/proxy"

headers = {
    "X-SLS-GPRS": "false",
    "X-SLS-Carrier": "",
    "X-SLS-UID": "0",
    "X-SLS-AppId": "3",
    "X-SLS-VersionCode": "135",
    "Authorization": "Custom QWxhZGRpbjpPcGVuU2VzYW1l",
    "Content-Type": "application/json",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.0; dolphin Build/NRD91N)",
    "Host": HOST,
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
}

def get_proxy(IV, KEY, URL):
    response = requests.post(URL, headers=headers).text
    b64_encrypted_proxy = json.loads(response).get("data")[0]
    enc = base64.b64decode(b64_encrypted_proxy)
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    s = cipher.decrypt(enc)
    return s[:-ord(s[len(s)-1:])]

if __name__ == "__main__":
    decoded_proxy = get_proxy(IV, KEY, URL)
    parsed_output = json.loads(decoded_proxy)
    print(json.dumps(parsed_output, indent=4))

