import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Variável global para armazenar os logs dos cursos
logs = []


def salvar_csv(logs):
    # Pegar a data e hora atuais para o nome do arquivo
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Nome do arquivo CSV incluindo a data e hora
    filename = f"cursos_log_{now}.csv"
    # Criar o arquivo CSV e escrever os dados
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escrever o cabeçalho
        writer.writerow(["Data", "Instituição", "Curso"])
        # Escrever os dados dos cursos da lista de logs
        for log in logs:
            writer.writerow([log["data"], log["instituicao"], log["curso"]])
    print(f"\nOs cursos foram salvos em '{filename}'\n")


def get_fucape_courses():
    url_fucape = "https://fucape.br/graduacao/"
    response = requests.get(url_fucape)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        div_cursos = soup.find('div', {'data-id': '3a5acb3'})
        if div_cursos:
            cursos_fucape = div_cursos.find_all('h3')
            courses_list = [curso.get_text(strip=True)
                            for curso in cursos_fucape]
            return courses_list
        else:
            return ["Div com o ID '3a5acb3' não encontrada."]
    else:
        return [f"Falha ao acessar a página da Fucape. Status Code: {response.status_code}"]


def get_ucl_courses():
    url_ucl = "https://www.ucl.br/graduacao/"
    response = requests.get(url_ucl)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        cursos_ul = soup.find('ul', id='menu-graduacao-manguinhos')
        if cursos_ul:
            cursos_ucl = cursos_ul.find_all('li')
            courses_list = [curso.get_text(strip=True) for curso in cursos_ucl]
            return courses_list
        else:
            return ["Nenhuma lista com o id 'menu-graduacao-manguinhos' foi encontrada."]
    else:
        return [f"Falha ao acessar a página da UCL. Status Code: {response.status_code}"]


def get_ifes_courses():
    url_ifes = "https://serra.ifes.edu.br/cursos/graduacao?view=default"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    response = requests.get(url_ifes, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        div_cursos = soup.find('div', class_='listagem-chamadas-secundarias')
        if div_cursos:
            cursos_ifes = div_cursos.find_all('h3')
            courses_list = [curso.get_text(strip=True)
                            for curso in cursos_ifes]
            return courses_list
        else:
            return ["Div com a classe 'listagem-chamadas-secundarias' não encontrada."]
    else:
        return [f"Falha ao acessar a página da IFES. Status Code: {response.status_code}"]


def adicionar_log(instituicao, cursos):
    # Função para adicionar cursos à variável de logs
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Data e hora atual
    for curso in cursos:
        logs.append({"data": now, "instituicao": instituicao, "curso": curso})


def main():
    print("Iniciando coleta automática dos cursos...")

    # Fucape
    print("\nBuscando cursos da Fucape...")
    courses_fucape = get_fucape_courses()
    print("Cursos da Fucape capturados:")
    print("\n".join(courses_fucape))
    adicionar_log("Fucape", courses_fucape)

    # UCL
    print("\nBuscando cursos da UCL...")
    courses_ucl = get_ucl_courses()
    print("Cursos da UCL capturados:")
    print("\n".join(courses_ucl))
    adicionar_log("UCL", courses_ucl)

    # IFES
    print("\nBuscando cursos da IFES...")
    courses_ifes = get_ifes_courses()
    print("Cursos da IFES capturados:")
    print("\n".join(courses_ifes))
    adicionar_log("IFES", courses_ifes)

    # Salvar os logs no CSV ao finalizar todas as buscas
    print("\nFinalizando e salvando os logs no arquivo CSV...")
    salvar_csv(logs)


if __name__ == "__main__":
    main()
