from flask_restx import Resource
from server.instance import run

dados = []

app, api = run.app, run.api

@api.route('/livros')

class ProductList (Resource):

    def get(self,):
        return (dados)
    
    def post(self,):
        response = api.payload
        dados.append(response)
        return response , 200 