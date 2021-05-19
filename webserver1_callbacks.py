import json
from datetime import datetime

trackpad = op('trackpad')
feedback = op('feedback1')


def onHTTPRequest(webServerDAT, request, response):
    response['statusCode'] = 200  # OK
    response['statusReason'] = 'OK'
    response['data'] = op('clientHtml').text
    return response


def onWebSocketReceiveText(webServerDAT, client, data):
    timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-4]
    event = json.loads(data)

    if event['type'] == 'ctrl:1':
        op('change1').click()
    if event['type'] == 'ctrl:2':
        op('change2').click()
    if event['type'] == 'ctrl:3':
        op('change3').click()
    if event['type'] == 'ctrl:4':
        op('change4').click()
    if event['type'] == 'ctrl:5':
        op('change5').click()
    if event['type'] == 'ctrl:6':
        op('change6').click()
        
    return

