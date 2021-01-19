import os
import codecs
import json

class MySettings(object):
	def __init__(self, settingsfile=None):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
				self.__dict__ = json.load(f, encoding="utf-8")
		except:
			self.BannedLineContains1 = "wanna become famous? buy followers, primes and viewers on"
			self.BannedLineContains2 = ""
			self.BannedLineContains3 = ""
			self.BannedLineContains4 = ""
			self.BannedLineContains5 = ""
			self.BannedLineContains6 = ""
			self.BannedLineContains7 = ""
			self.BannedLineContains8 = ""
			self.BannedLineContains9 = ""

		self.BannedLineContains = [
			self.BannedLineContains1,
			self.BannedLineContains2,
			self.BannedLineContains3,
			self.BannedLineContains4,
			self.BannedLineContains5,
			self.BannedLineContains6,
			self.BannedLineContains7,
			self.BannedLineContains8,
			self.BannedLineContains9
		]

	def Reload(self, jsondata):
		self.__dict__ = json.loads(jsondata, encoding="utf-8")
		return

	def Save(self, settingsfile):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
				json.dump(self.__dict__, f, encoding="utf-8")
			with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
				f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
		except:
			Parent.Log(ScriptName, "Failed to save settings to file.")
		return