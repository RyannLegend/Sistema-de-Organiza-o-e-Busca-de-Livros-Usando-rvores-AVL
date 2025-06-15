import json

def carregar_livros():
    try:
        with open('livros.json', 'r', encoding='utf-8') as file:
            livros = json.load(file)  
    except FileNotFoundError: 
        livros = []
    return livros

def salvar_livros(livros):
    with open('livros.json', 'w', encoding='utf-8') as file:
        json.dump(livros, file, indent=4, ensure_ascii=False)
