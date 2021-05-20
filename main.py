try:
    import requests, json
    from blessed import Terminal
except:
    import os
    os.system('pip3 install requests')
    os.system('pip3 install json')
    os.system('pip3 install blessed')
    import requests, json
    from blessed import Terminal

term = Terminal()

print("Made by: bicxter#9999")

def Answers():
    id = str(input('Game id - '))
    gameData = json.loads(requests.put("https://api.blooket.com/api/firebase/join", data={"id":id,"name":"ans"}, headers={"Referer" : "https://www.blooket.com"}).text)
    if "host" not in gameData:
        print(f"Couldn't find game with id : {id}")
    else:
        set = gameData["host"]["set"]
        removeBot = requests.delete(f"https://api.blooket.com/api/firebase/client?id={id}&name=ans",headers={"Referer":"https://www.blooket.com/"})
        Ans = json.loads(requests.get(f"https://api.blooket.com/api/games?gameId={set}", headers={"Referer" : "https://www.blooket.com"}).text)
        for i in Ans["questions"]:
            for a in i["correctAnswers"]:
                print(f'Q: {i["question"]} A: {a}')
            
def blooksUnlocked():
    name = input('Blooket username - ')
    userData = json.loads(requests.get(f"https://api.blooket.com/api/users?name={name}", headers={"Referer": "https://www.blooket.com"}).text)
    print(f'Unlocked {userData["numUnlocks"]} blooks')
    for i in userData["unlocks"]:
        print(userData["unlocks"][i], i)

def flood():
    id = str(input('Game id - '))
    name = input('Name of bots - ')
    amount = int(input('Amount of bots - '))

    for i in range(amount):
        addBot = requests.put("https://api.blooket.com/api/firebase/join", headers={"Referer" : "https://www.blooket.com"}, data={"id":id,"name":f"{name} {i+1}"})

def kick():
    id = str(input('Game id - '))
    name = input('Name of person - ')

    kicker = requests.delete(f"https://api.blooket.com/api/firebase/client?id={id}&name={name}", headers={"referer" : "https://www.blooket.com"})

def kickAll():
    id = str(input('Game id - '))

    join = requests.put("https://api.blooket.com/api/firebase/join",data={"id":id,"name":"kicker"},headers={"Referer":"https://www.blooket.com/"}).text

    leave = requests.delete(f"https://api.blooket.com/api/firebase/client?id={id}&name=kicker",headers={"Referer":"https://www.blooket.com/"})

    players=json.loads(join)["host"]["c"].keys()

    for player in players:
        remover = requests.delete(f"https://api.blooket.com/api/firebase/client?id={id}&name={player}",headers={"Referer":"https://www.blooket.com/"})


while True:
    print(term.home, term.clear_eos)
    b = input('What would you like to do - ')
    print(term.home, term.clear_eos)
    if b == "ans":
        Answers()
    elif b == "blooks":
        blooksUnlocked()
    elif b == "flood":
        flood()
    elif b == "kick":
        kick()
    elif b == "kickall":
        kickAll()
    input()
