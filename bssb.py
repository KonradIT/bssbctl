import lib
from termcolor import colored
from datetime import datetime
from prettytable import PrettyTable

bssbAPI = lib.BeatSaberBrowserServerAPI()
lobbies = bssbAPI.browse(offset=0, limit=10)
if not lobbies.get("success"):
	print(colored("Error in getting active lobbies: " + lobbies.get("error"), "red"))
	exit()

x = PrettyTable()

x.field_names = [
	colored("Index", "magenta", attrs=['bold']),
	colored("Level Name", "red", attrs=['bold']),
	colored("Server Code", "magenta", attrs=['bold']),
	colored("Players", "red", attrs=['bold']),
	colored("Modded", "magenta", attrs=['bold']),
	colored("Lobby State", "red", attrs=['bold']),
	colored("Song Name", "magenta", attrs=['bold']),
	colored("Difficulty", "red", attrs=['bold'])
]

for index, t in enumerate(lobbies.get("data").get("Lobbies")):
		x.add_row([
			colored(index, "green"), 
			t.get("levelName") or colored("In Lobby", "green"), 
			colored(t.get("serverCode", ""), "yellow"), 
			str(t.get("playerCount","")) + "/" + str(t.get("playerLimit","")), 
			colored(t.get("isModded",""), "green"), 
			colored(lib.LobbyStates[t.get("lobbyState","")], "cyan"),
			colored(t.get("songName",""), "magenta"),
			colored(lib.DifficultyLevels[t.get("difficulty","") or 5], "blue")
		])

x.align = "l"
print(x)