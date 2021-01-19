import sys, os, json, re
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from unidecode import unidecode
from Settings_Module import MySettings

ScriptName = "BanPurchaseBots"
Website = "https://github.com/mfrankruijter/BanPurchaseBots"
Description = "Bans those annoying bots that want you to purchase followers and viewers."
Creator = "Marcel Frankruijter"
Version = "1.0.0"

ScriptSettings = MySettings()

def Init():
    return

def Execute(data):
    if data.IsChatMessage() != True: 
        return

    originalMessage = data.Message
    message = unidecode(data.Message).replace('[?]', '')
    if originalMessage != message:
        Parent.Log("AntiSpamBot", re.sub('\s+', ' ', message.lower()))
        if isBannedMessage(message.lower()):
            Parent.Log("AntiSpamBot", "Banning user: \"" + data.UserName + "\" for message \"" + message.lower() + "\"")
            Parent.SendStreamMessage("/ban " + data.UserName)
    return

def Tick():
    return

def isBannedMessage(message):
    for line in ScriptSettings.BannedLineContains:
        if line != '':
            if line in message:
                return True
    return False
