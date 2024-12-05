import json
from mimetypes import inited


max_level = 20
max_xp = 100


character_classes = {
    "warrior":{
        "health": 100,
        "attack":15,
        "defense":5,
        },
    "mage":{
        "health": 80,
        "attack": 20,
        "defense": 5,
        },
    "archer":{
        "health": 90,
        "attack": 18,
        "defense": 5,
        },
    }
character_name = input("What is your name? ")

cls = input(f"Choose a class ({", ".join(character_classes.keys())}) : ").lower().strip()
while cls not in character_classes.keys():
    cls = input(f"Class doesn't exist. Please choose a proper class ({", ".join(character_classes.keys())}): ").lower().strip()
print(f"You have chosen the class: {cls}")

health_points = character_classes[cls]["health"]
attack_power = character_classes[cls]["attack"]
defense_power = character_classes[cls]["defense"]

player = {
    "name": character_name ,
    "class" : cls,
    "health_points":health_points,
    "attack_power":attack_power,
    "defense_power":defense_power,
    "initial_gold":100,
    "initial_level": 1,
    "xp":0,
    "inventory":[]
}

enemy = {"name": "Goblin",
    "health": 50,
    "attack": 12,
    "defense": 4,
    "experience": 30  # XP gained by defeating the enemy
    }
battle = True

# if battle:
#     while player["health_points"] > 0:
#         print("Attacks")
#         print("Attacked")
#         player["health_points"] -= 10
#         print(player["health_points"])
#     battle = False

world_data = {
    "locations": [
        {
        "name":"Village",
        "description":{
            "first_visit": "You enter the bustling village filled with chatter and activity.",
            "return_visit": "You return to the village, familiar faces greet you amidst the usual hustle."
        },
        "action":{},
        "visited":False,
    },
        {
        "name":"Forest",
        "description":{
            "first_visit": "You enter the bustling village filled with chatter and activity.",
            "return_visit": "You return to the village, familiar faces greet you amidst the usual hustle."
        },
        "action":{},
        "visited":False,
    },
    ]
}

i = 0
while i < 3:
    for location in world_data["locations"]:
        if location["name"] == "Village":
            print(location)
            if location["visited"]:
                print(location["description"]["return_visit"])
            else:
                print(location["description"]["first_visit"])
                location["visited"] = True
    i += 1
# to create save gamestate and load game state