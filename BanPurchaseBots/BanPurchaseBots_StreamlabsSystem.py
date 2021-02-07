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

SettingsFile = ""
ScriptSettings = MySettings()

def Init():
    global SettingsFile
    SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
    global ScriptSettings
    ScriptSettings = MySettings(SettingsFile)
    return

def Execute(data):
    if data.IsChatMessage() != True or data.IsFromTwitch() != True: 
        return

    originalMessage = data.Message
    message = unidecode(data.Message).replace('[?]', '')
    if originalMessage != message:
        message = message.lower()
        if isBannedMessage(message):
            Parent.Log("AntiSpamBot", "Banning user: \"" + data.UserName + "\" for message \"" + message + "\"")
            Parent.SendStreamMessage("/ban " + data.UserName)
            sendToDiscord(data.UserName, message)
    return

def Tick():
    return

def isBannedMessage(message):
    for line in ScriptSettings.BannedLineContains:
        if line != '':
            if line in message:
                return True
    return False

def ReloadSettings(jsonData):
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

def sendToDiscord(username, reason):
    if ScriptSettings.PublishToDiscord != 'No':
        if ScriptSettings.PublishToDiscord == 'DM to User':
            if ScriptSettings.PublishToDiscordUsername != '':
                Parent.SendDiscordDM(ScriptSettings.PublishToDiscordUsername, formatDiscordMessage(username, reason))
        if ScriptSettings.PublishToDiscord == 'Bot Channel':
            Parent.SendDiscordMessage(formatDiscordMessage(username, reason))

def formatDiscordMessage(username, reason):
    if ScriptSettings.PublishToDiscordFormat == 'Just the username':
        return username
    if ScriptSettings.PublishToDiscordFormat == 'Username and reason':
        return "Banned user: \"" + username + "\" for message \"" + reason + "\""
    if ScriptSettings.PublishToDiscordFormat == 'Format as Twitch ban command':
        return "/ban " + username
