from flask_restx import Resource
from server.instance import run

# dados = [
#     {'id':1, 'Name': 'Naruto book', 'Value': 20},
#     {'id':2, 'Name': 'Dragon Ball Z book', 'Value': 50},
#     {'id':3, 'Name': 'Dragon Ball GT book', 'Value': 38}
# ]

dados = []

app, api = run.app, run.api

@api.route('/productlist')

class ProductList (Resource):

    def get(self,):
        return (dados)
    
    def post(self,):
        response = api.payload
        dados.append(response)
        return response , 200 