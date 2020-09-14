import requests
import json

def sendASMS(contactno = "8919961080",message="Sorry Message not Available"):

    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno


    headers = {
        'authorization': "uls2KAIQcNg9jWPnteLiSx4vVzb87orRX01kTaOfmYG53CwyUBgBbMdUQHryZi1I96wR7O8NDP0CszvV",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)

    return json.loads(response.text)
