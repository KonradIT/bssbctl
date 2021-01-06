import requests
from enum import Enum
class Platforms(Enum):
	OCULUS = 1
	STEAM = 2
LobbyStates = [
	"In Lobby",
	"In Lobby",
	"Playing",
	"Playing"
]

DifficultyLevels = [
	"Easy",
	"Normal",
	"Hard",
	"Expert",
	"Expert+",
	"In Lobby"
]
    
def error(request) -> bool:
	if request.text == "Bad Request! Naughty!":
		return True
	if request.status_code != 200:
		return True
	return False
class BeatSaberBrowserServerAPI:
	def __init__(self):
		self.base_uri = "https://bssb.app/api/v1"
		
		self.session = requests.Session()
		self.session.headers["User-Agent"] = "ServerBrowser/1.0 (BeatSaber/1.13.0) (BSSBCTL/@KonradIT)"
		self.session.headers["X-BSSB"] = "\u2714".encode("utf-8")
		
	def browse(self,**kwargs) -> dict:
		
		params = ()
		for k, v in kwargs.items():
			if k == "platform":
				params = params + (("platform", "oculus" if v == Platforms.OCULUS else "steam"),)
			else:
   				params = params + ((k, v),)
		
		r = self.session.get(self.base_uri + "/browse", params=params)
		if error(r):
			return {
				"success": False,
				"error": r.text
			}
		return {
			"success":True,
			"error": None,
			"data": r.json()
		}