import requests
import json


class SendDingDingMsg():
    def __init__(self):
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=a0186307c2410ee62522cc2ff977bd1e4690cbceb8466c1cb56a2ebafc8f9612'

    def sendMsg(self,msg):
        program = {
            "msgtype": "text",
            "text": {"content": "???"+msg},
        }
        headers = {'Content-Type': 'application/json'}
        f = requests.post(self.url, data=json.dumps(program), headers=headers)
