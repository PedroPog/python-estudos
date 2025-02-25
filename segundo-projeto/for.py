lista_npcs = [
    {"name": "Goblin", "hp": 100,"level": 1},
    {"name": "Orc", "hp": 200, "level": 2},
    {"name": "Troll", "hp": 300, "level": 3},
    {"name": "Dragon", "hp": 400, "level": 4}
]


for npc in lista_npcs:
    print(f"NPC: ",npc["name"]," HP: ",npc["hp"]," Level: ",npc["level"])