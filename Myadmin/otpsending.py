import requests
import json

def sendASMS(contactno = "7008460372",message="Sorry Message not Available"):

    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno


    headers = {
        'authorization': "kG4rxPlIpbajsKJhfnt2S9vA8O6TedYyuQ5MWBDNRwVgHCcU3LCDwYMJ0FdKfikslj5O9cx3ZNugP7tn",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)

    return json.loads(response.text)

# d=sendASMS()
# print(d)
