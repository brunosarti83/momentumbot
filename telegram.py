
#SI SE ROMPE, TUTORIAL: https://www.youtube.com/watch?v=ps1yeWwd6iA
from telegram import TELE_BOT, CHAT_ID, ERROR_ID

def sendTelegram(message):
    import requests
    chatId = CHAT_ID
    url = 'https://api.telegram.org/'+TELE_BOT+'/sendMessage?chat_id='+chatId+'&text="{}"'.format(message)
    requests.get(url)
    return

def sendErrorTelegram(message):
    import requests
    chatId = ERROR_ID
    url = 'https://api.telegram.org/'+TELE_BOT+'/sendMessage?chat_id='+chatId+'&text="{}"'.format(message)
    requests.get(url)
    return

