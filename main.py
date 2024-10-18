import requests
from bs4 import BeautifulSoup
 
# Função de busca para os cursos da Fucape
def scrape_fucape():
    url = 'https://www.fucape.br/vestibular/'
 
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site da Fucape: {e}")
        return
 
    soup = BeautifulSoup(response.text, 'html.parser')
 
    #busca pelos cursos na Fucape
    cursos = []
    for curso in soup.find_all('h3'):  
        nome_curso = curso.text.strip()
        cursos.append(nome_curso)
 
    if cursos:
        print("Cursos disponíveis na Fucape:")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}. {curso}")
    else:
        print("Nenhum curso encontrado na página da Fucape.")
 
#busca pelos nomes dos cursos na UCL
def scrape_ucl():
    url = 'https://www.ucl.br/graduacao/'
 
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site da UCL: {e}")
        return
 
    soup = BeautifulSoup(response.text, 'html.parser')
 
    # Procurar pela lista de cursos dentro do <ul> com id="menu-graduacao-manguinhos"
    cursos = []
    lista_cursos = soup.find('ul', id='menu-graduacao-manguinhos')
 
    if lista_cursos:
        # Procurar os itens da lista <li> dentro do <ul>
        for curso in lista_cursos.find_all('li'):
            nome_curso = curso.text.strip()
            cursos.append(nome_curso)
 
    if cursos:
        print("Cursos disponíveis na UCL:")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}. {curso}")
    else:
        print("Nenhum curso encontrado na página da UCL.")
 
# Função principal para exibir o menu e executar as funções de busca
def main_menu():
    while True:
        print("\nMenu de busca de cursos")
        print("1. Buscar cursos da Fucape")
        print("2. Buscar cursos da UCL")
        print("5. Sair")
 
        escolha = input("Escolha uma opção: ")
 
        if escolha == "1":
            scrape_fucape()
        elif escolha == "2":
            scrape_ucl()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
 
# Chamada para executar a função principal
main_menu()