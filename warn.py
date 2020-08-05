import requests
import json

url = 'https://oapi.dingtalk.com/robot/send?access_token=a0186307c2410ee62522cc2ff977bd1e4690cbceb8466c1cb56a2ebafc8f9612'
program = {
    "msgtype": "text",
    "text": {"content": "通知！"},
}
headers = {'Content-Type': 'application/json'}
f = requests.post(url, data=json.dumps(program), headers=headers)
