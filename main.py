import requests
from bs4 import BeautifulSoup


def get_fucape_courses():
    # URL da Fucape
    url_fucape = "https://fucape.br/graduacao/"
    response = requests.get(url_fucape)

    # Verifica se a resposta é válida
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Busca pela div com o ID específico
        div_cursos = soup.find('div', {'data-id': '3a5acb3'})
        if div_cursos:
            # Dentro dessa div, busca todos os elementos <h3> para obter os cursos
            # Supondo que os cursos estão em tags <h3>
            cursos_fucape = div_cursos.find_all('h3')
            courses_list = [curso.get_text(strip=True)
                            for curso in cursos_fucape]
            return courses_list
        else:
            return ["Div com o ID '3a5acb3' não encontrada."]
    else:
        return [f"Falha ao acessar a página da Fucape. Status Code: {response.status_code}"]


def get_ucl_courses():
    # URL da UCL
    url_ucl = "https://www.ucl.br/graduacao/"
    response = requests.get(url_ucl)

    # Verifica se a resposta é válida
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extrai apenas os cursos dentro da ul com id="menu-graduacao-manguinhos"
        cursos_ul = soup.find('ul', id='menu-graduacao-manguinhos')
        if cursos_ul:
            # Os cursos estão listados em <li>
            cursos_ucl = cursos_ul.find_all('li')
            courses_list = [curso.get_text(strip=True) for curso in cursos_ucl]
            return courses_list
        else:
            return ["Nenhuma lista com o id 'menu-graduacao-manguinhos' foi encontrada."]
    else:
        return [f"Falha ao acessar a página da UCL. Status Code: {response.status_code}"]


def get_ifes_courses():
    # URL da IFES
    url_ifes = "https://serra.ifes.edu.br/cursos/graduacao?view=default"
    # Definindo um cabeçalho User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    response = requests.get(url_ifes, headers=headers)

    # Verifica se a resposta é válida
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Busca pela div que contém os cursos
        div_cursos = soup.find('div', class_='listagem-chamadas-secundarias')
        if div_cursos:
            # Os cursos estão listados em <h3>
            cursos_ifes = div_cursos.find_all('h3')
            courses_list = [curso.get_text(strip=True)
                            for curso in cursos_ifes]
            return courses_list
        else:
            return ["Div com a classe 'listagem-chamadas-secundarias' não encontrada."]
    else:
        return [f"Falha ao acessar a página da IFES. Status Code: {response.status_code}"]


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Buscar cursos da Fucape")
        print("2. Buscar cursos da UCL")
        print("3. Buscar cursos da IFES")
        print("4. Sair")

        choice = input("\nDigite sua escolha (1/2/3/4): ")

        if choice == '1':
            print("\nBuscando cursos da Fucape...\n")
            courses = get_fucape_courses()
            print("\nCursos capturados da Fucape:\n")
            print("\n".join(courses))

        elif choice == '2':
            print("\nBuscando cursos da UCL...\n")
            courses = get_ucl_courses()
            print("\nCursos capturados da UCL:\n")
            print("\n".join(courses))

        elif choice == '3':
            print("\nBuscando cursos da IFES...\n")
            courses = get_ifes_courses()
            print("\nCursos capturados da IFES:\n")
            print("\n".join(courses))

        elif choice == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
