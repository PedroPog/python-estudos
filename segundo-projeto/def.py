from random import randint

lista_npcs = []

player = {
    "nome": "Jogador",
    "level": 1,
    "exp": 0,
    "exp_max": 100,
    "hp": 100,
    "hp_max": 100,
    "dano": 25
}

def criar_monstro(level):
    
    #level = randint(0, 50)

    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 50 * level
    }

    return novo_npc

def gerar_monstros(n_npcs):
    for x in range(n_npcs):
        new_npc = criar_monstro(x+1)
        lista_npcs.append(new_npc)

def exibir_npc():
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']}, Level: {npc['level']}, Dano: {npc['dado']}, HP: {npc['hp']}, EXP: {npc['exp']}")

def exibir_npc(npc):
    print(f"Nome: {npc['nome']}, Level: {npc['level']}, Dano: {npc['dado']}, HP: {npc['hp']}, EXP: {npc['exp']}");
    
def exibir_player():
    print(f"Nome: {player['nome']}, Level: {player['level']}, HP: {player['hp']}/{player['hp_max']}, EXP: {player['exp']}/{player['exp_max']}")    

def resetar_npc(npc):
    npc["hp"] = npc["hp_max"]

def resetar_player():
    player["hp"] = player["hp_max"]

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1    
        print(f"O {player['nome']} subiu de level! Agora é level {player['level']}!")
        player["exp"] = 0
        player["exp_max"] = player["exp_max"] * 2   
        player["hp_max"] += 20

def iniciar_batalha(npc):
    while player["hp"] > 0 and npc["hp"] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
    if(player["hp"] <= 0):
        print(f"O {npc['nome']} venceu!")
        exibir_npc(npc)
    else:
        print(f"O {player['nome']} venceu! e ganhou {npc['exp']} de EXP!")
        player["exp"] += npc["exp"]
        exibir_player()
    level_up()
    resetar_player()
    resetar_npc(npc)    
    

def atacar_npc(npc):
    npc["hp"] -= player["dano"]

def atacar_player(npc):
    player["hp"] -= npc["dano"]

def exibir_info_batalha(npc):
    print(f"Player HP: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']} HP: {npc['hp']}/{npc['hp_max']}")
    print("____________________________________________________\n")


gerar_monstros(5)
#exibir_npc()

npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
