import requests


class ListaDeRepositorios():

    def __init__(self, usuario):
        self.usuario = usuario

    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/{self.usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        return []

    def lista_repositorios(self):
        dados_api = self.requisicao_api()
        if dados_api:
            for i, item in enumerate(dados_api, 1):
                print(i, item.get('name'))


if __name__ == '__main__':
    repositorio_to_list = ListaDeRepositorios('grazimelo')
    repositorio_to_list.lista_repositorios()
