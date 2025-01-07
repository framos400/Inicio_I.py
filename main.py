from flask import Flask, jsonify

app = Flask(__name__)

class Estado:
    def __init__(self, nome, populacao, recursos):
        self.nome = nome
        self.populacao = populacao
        self.recursos = recursos

class Municipio:
    def __init__(self, nome, populacao, economia):
        self.nome = nome
        self.populacao = populacao
        self.economia = economia

# Dados fictícios
sao_paulo = Estado("São Paulo", 45000000, ["Água", "Minérios"])
fortaleza = Estado("Fortaleza", 2687000, ["Turismo", "Petróleo"])

municipios = [
    Municipio("São Paulo - Capital", 12300000, "Indústria"),
    Municipio("Fortaleza - Capital", 2687000, "Turismo"),
]

@app.route('/simular', methods=['GET'])
def simular():
    # Exemplo de simulação: aumentar população em 1%
    sao_paulo.populacao = int(sao_paulo.populacao * 1.01)
    fortaleza.populacao = int(fortaleza.populacao * 1.02)

    resultados = {
        "estados": [
            {"nome": sao_paulo.nome, "populacao": sao_paulo.populacao, "recursos": sao_paulo.recursos},
            {"nome": fortaleza.nome, "populacao": fortaleza.populacao, "recursos": fortaleza.recursos},
        ],
        "municipios": [
            {"nome": m.nome, "populacao": m.populacao, "economia": m.economia} for m in municipios
        ]
    }
    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)
