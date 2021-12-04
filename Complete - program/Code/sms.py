import requests
class Sms():
    def sendtxt(self, number,name,party):
        
        url = "https://www.fast2sms.com/dev/bulk"
        payload = "sender_id=FSTSMS&message=Your({}) Vote has been REGISTERED. You Voted for {}. Thank You :)&language=english&route=p&numbers={}".format(name,party,number)
        headers = {
            'authorization': "TK1kNbDAi06fwCHB7ZYjyPthzds8g3xvmcFeJSuLlGqa4onrIU4FIWbPrjU3XQYT6qGvwDp2ZkHx8f90",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        

