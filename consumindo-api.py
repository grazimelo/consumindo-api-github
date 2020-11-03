import pandas as pd
import requests
import json

class ListaDeRepositorios():

    def __init__(self, usuario):
        self._usuario = usuario

    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/grazimelo/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def lista_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)
            
repositorio_to_list = ListaDeRepositorios('grazimelo')
repositorio_to_list.lista_repositorios()