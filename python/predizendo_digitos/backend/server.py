from flask import Flask, jsonify, request
from flask_cors import CORS

import numpy as np
import pickle
import matplotlib.pyplot as plt

app = Flask(__name__) # criando a aplicação
CORS(app) # corrigir possíveis problemas de cross-origin

# como funciona o flask: crio funções e uso o magic decorator @app.route 
# para associar um url a ela

@app.route('/test')
def test():
    return "Server is up!"