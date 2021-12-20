from flask import Flask
from flask_restx import Api

class Start():
    
    def __init__(self,):

        self.app = Flask(__name__)
        
        self.api = Api(
            app = self.app,
            version='1.0',
            title='restFlask',
            description='Simple API rest python/Flask',
            doc='/doc',
            contact_email='fsantanagy@gmail.com'
        )
    
    def start(self,):
        self.app.run(
            debug= True
        )

run = Start()