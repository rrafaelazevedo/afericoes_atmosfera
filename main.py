# API, Application Programming Interface -> Local para disponibilizar recursos e/ou funcionalidades. UMA PONTE
# 1. Objetivo - Criar uma API que diisponibiliza a consulta, criacao, edicao e exclusao
# 2. URL base - localhost
# 3. Endpoints -
# localhost/carros(POST)
# localhost/carros(GET)
# localhost/carros(PUT)
# localhost/carros(DELETE)

from flask import Flask, jsonify, make_response, request
# importa o database
from bd import afericoes_atmosfera

# instanciar o módulo flask na nossa variável app
app = Flask('afericoes_atmosfera')

# primeiro método 1.0 - visualizar dados (GET)
# def get_carros  -> funcao def para retornar a lista de carros
# app.route -> definir que essa função é uma rota para que o flask entenda que aquilo é um método que precisa ser executado
@app.route('/afericoes', methods=['GET'])
def get_afericoes():
    return afericoes_atmosfera

# primeiro método 1.1 - visualizar dados por id (GET / ID)
@app.route('/afericoes/<int:id>', methods=['GET'])
def get_afericoes_id(id):
    for afericao in afericoes_atmosfera:
        if afericao.get('id') == id:
            return jsonify(afericao)

# segundo método 2.0 -  criar novos dados (POST)
@app.route('/afericoes', methods=['POST'])
def criar_afericao():
    afericao = request.json
    afericoes_atmosfera.append(afericao)
    return make_response(jsonify(mensagem=' Aferição cadastrada com sucesso! ', afericao=afericao))

# terceiro método 3.0 - editar dados (PUT)
@app.route('/afericoes/<int:id>', methods=['PUT'])
def editar_afericao_id(id):
    afericao_alterada = request.get_json()
    for indice, afericao in enumerate(afericoes_atmosfera):
        if afericao.get('id') == id:
            afericoes_atmosfera[indice].update(afericao_alterada)
            return jsonify(afericoes_atmosfera[indice])
        
# quarto método 4.0 - deletar dados (DELETE)
@app.route('/afericoes/<int:id>', methods=['DELETE'])
def excluir_afericao(id):
    for indice, afericao in enumerate(afericoes_atmosfera):
        if afericao.get('id') == id:
            del afericao[indice]
            return jsonify({'mensagem: ': 'Registro excluído com sucesso!'})
        

app.run(port=5001, host='localhost')