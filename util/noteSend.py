import http.client
import urllib
import random

class HuyiEmail:
    def __init__(self, host, sms_send_uri, account, password):
        self.host = host
        self.sms_send_uri = sms_send_uri
        self.account = account
        self.password = password

    def send_sms(self, text, mobile):
        params = urllib.parse.urlencode({'account': self.account, 'password': self.password, 'content': text, 'mobile':mobile,'format':'json' })
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection(self.host, port=80, timeout=30)
        conn.request("POST", self.sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        return response_str

def noteSend(mobile):
    # 短信发送
    huyi = HuyiEmail('106.ihuyi.com', "/webservice/sms.php?method=Submit",
                     "C89353067", "357fcb72ce680752b12fea905293ceae")
    string = ''
    for _ in range(4):
        n = random.randrange(0, 10)
        string += str(n)
    text = "您的验证码是：" + string + "。请不要把验证码泄露给其他人。"
    huyi.send_sms(text, mobile)
    return string

if __name__ == '__main__':
    noteSend('13113121202')