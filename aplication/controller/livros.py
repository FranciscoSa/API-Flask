from flask_restx import Resource
from server.instance import run
import json
from model.crud import *

dados = []

app, api = run.app, run.api

@api.route('/livros')

class ProductList (Resource):
    
    def get(self,):
        #teste crud remover e criar arquivo separado depois para listar os livros
        crud = Crud()
        dados = crud.read("SELECT * FROM livros")
        if dados == "Erro": 
            return ("Ocorreu um erro interno, já estamos trabalhando para corrigir",500)
        else:
            return(dados)
    
    def post(self,):
        response = api.payload
        dados.append(response)
        return response , 200 