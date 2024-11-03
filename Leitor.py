import os
import csv
import sys


def ler_arquivos_csv(diretorio, filtrar_por=''):
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            try:
                with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
                    leitor_csv = csv.reader(file)
                    print(f"Conteúdo do arquivo {arquivo}:")
                    for linha in leitor_csv:
                        # Exibe apenas linhas que contêm o termo filtrado, se houver
                        if filtrar_por.lower() in (str(item).lower()for item in linha):
                            print(linha)
                        elif not filtrar_por:
                            print(linha)
                    print("\n")
            except Exception as e:
                print(f"Erro ao ler o arquivo {arquivo}: {e}")


#Caminho do diretório onde estão os arquivos CSV
diretorio = r'C:\Users\alexa\Downloads\CrawlerProjeto\crawlerProjeto-1\banco de dados CSV'

while True:
    print("Escolha uma opção:")
    print("1 - UCL")
    print("2 - FUCAPE")
    print("3 - IFES")
    print("4 - Mostrar todo o conteúdo")
    print("5 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        ler_arquivos_csv(diretorio, filtrar_por='UCL')
    elif opcao == '2':
        ler_arquivos_csv(diretorio, filtrar_por='FUCAPE')
    elif opcao == '3':
        ler_arquivos_csv(diretorio, filtrar_por='IFES')
    elif opcao == '4':
        ler_arquivos_csv(diretorio)
    elif opcao == '5':
        print("Encerrando o programa.")
        sys.exit()
    else:
        print("Opção inválida! Tente novamente.")
