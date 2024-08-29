import requests

arquivo_caminhos = 'c:/Users/Renata/Documents/python/pardal/cp/wordlistnew.txt'
extensoes = [".php", ".bak", ".orig", ".inc"]
url_base = "http://testphp.vulnweb.com"

def verificar_status(url):
    try:
        resposta = requests.get(url)
        return resposta.status_code
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return None

def brute_force_status_code_200(url_base, arquivo_caminhos, extensoes):
    try:
        with open(arquivo_caminhos, "r") as file:
            caminhos = file.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo {arquivo_caminhos} não encontrado.")
        

    for caminho in caminhos:
        for extensao in extensoes:
            url = f"{url_base}/{caminho}{extensao}"
            status_code = verificar_status(url)
            if status_code == 200:
                print(f"Status 200 encontrado para: {url}")

if __name__ == "__main__":
    brute_force_status_code_200(url_base, arquivo_caminhos, extensoes)
