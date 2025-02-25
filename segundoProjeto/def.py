from random import randint

lista_npcs = []

player = {
    "nome": "Jogador",
    "level": 1,
    "exp": 0,
    "exp_max": 100,
    "hp": 100,
    "hp_max": 100
}

def criar_monstro():
    
    level = randint(1, 50)

    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dado": 5 * level,
        "hp": 100 * level,
    }

    return novo_npc

def gerar_monstros(n_npcs):
    for x in range(n_npcs):
        new_npc = criar_monstro()
        lista_npcs.append(new_npc)

def exibir_npc():
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']}, Level: {npc['level']}, Dano: {npc['dado']}, HP: {npc['hp']}")


gerar_monstros(10)
exibir_npc()

