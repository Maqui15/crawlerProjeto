from prettytable import PrettyTable
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
        import requests


# Função para buscar dados do site da Fucape


def scrape_fucape():
    url = 'https://www.fucape.br/vestibular/'

    try:
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site Fucape: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Imprime o conteúdo HTML da página para verificar a estrutura
    print(soup.prettify())

    cursos = []
    for curso in soup.find_all('div', class_='course-info'):
        try:
            nome = curso.find('h2').text.strip()
            data_inicio = curso.find('span', class_='start-date').text.strip()
            data_fim = curso.find('span', class_='end-date').text.strip()
            horario = curso.find('span', class_='course-time').text.strip()
            publico = curso.find('span', class_='public').text.strip()
            cursos.append([nome, data_inicio, data_fim, horario, publico])
        except AttributeError:
            print('Fucape: Alguma informação não pôde ser encontrada para este curso.')

    print_results(cursos, "Fucape")

# Função para buscar dados do site do VIX Cursos


def scrape_vixcursos():
    url = 'https://vixcursos.vitoria.es.gov.br/'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site VIX Cursos: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    cursos = []
    for curso in soup.find_all('div', class_='course-list'):
        try:
            nome = curso.find('h3').text.strip()
            data_inicio = curso.find('span', class_='start-date').text.strip()
            data_fim = curso.find('span', class_='end-date').text.strip()
            horario = curso.find('span', class_='course-time').text.strip()
            publico = curso.find('span', class_='target-public').text.strip()
            cursos.append([nome, data_inicio, data_fim, horario, publico])
        except AttributeError:
            print(
                'VIX Cursos: Alguma informação não pôde ser encontrada para este curso.')

    print_results(cursos, "VIX Cursos")

# Função para buscar dados do site Qualificar ES


def scrape_qualificar():
    url = 'https://qualificar.es.gov.br/'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site Qualificar ES: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    cursos = []
    for curso in soup.find_all('div', class_='course-container'):
        try:
            nome = curso.find('h3').text.strip()
            data_inicio = curso.find('span', class_='start-date').text.strip()
            data_fim = curso.find('span', class_='end-date').text.strip()
            horario = curso.find('span', class_='course-time').text.strip()
            publico = curso.find('span', class_='target-public').text.strip()
            cursos.append([nome, data_inicio, data_fim, horario, publico])
        except AttributeError:
            print(
                'Qualificar ES: Alguma informação não pôde ser encontrada para este curso.')

    print_results(cursos, "Qualificar ES")

# Função para buscar dados do site SENAI ES


def scrape_senai():
    url = 'https://senaies.com.br/'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site SENAI ES: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    cursos = []
    for curso in soup.find_all('div', class_='course-block'):
        try:
            nome = curso.find('h4').text.strip()
            data_inicio = curso.find('span', class_='start-date').text.strip()
            data_fim = curso.find('span', class_='end-date').text.strip()
            horario = curso.find('span', class_='course-time').text.strip()
            publico = curso.find('span', class_='course-audience').text.strip()
            cursos.append([nome, data_inicio, data_fim, horario, publico])
        except AttributeError:
            print('SENAI ES: Alguma informação não pôde ser encontrada para este curso.')

    print_results(cursos, "SENAI ES")

# Função para apresentar resultados em formato de tabela


def print_results(cursos, instituicao):
    table = PrettyTable()
    table.field_names = ["Curso", "Início", "Fim", "Horário", "Público"]

    for curso in cursos:
        table.add_row(curso)

    print(f"\nResultados para {instituicao}:\n")
    print(table)

# Função principal para executar a raspagem


def main_menu():
    while True:
        print("\nMenu de Raspagem de Cursos")
        print("1. Buscar Fucape")
        print("2. Buscar VIX Cursos")
        print("3. Buscar Qualificar ES")
        print("4. Buscar SENAI ES")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            scrape_fucape()
        elif escolha == "2":
            scrape_vixcursos()
        elif escolha == "3":
            scrape_qualificar()
        elif escolha == "4":
            scrape_senai()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Chamada para executar a função principal
main_menu()


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
