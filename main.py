from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Classes básicas
class Estado:
    def __init__(self, nome, populacao, recursos_naturais):
        self.nome = nome
        self.populacao = populacao
        self.recursos_naturais = recursos_naturais

    def simular_crescimento_populacional(self, taxa_crescimento):
        self.populacao = int(self.populacao * (1 + taxa_crescimento))

class Municipio:
    def __init__(self, nome, populacao, economia):
        self.nome = nome
        self.populacao = populacao
        self.economia = economia

# Criando dados fictícios
sao_paulo = Estado("São Paulo", 45000000, ["Minérios", "Água"])
fortaleza = Estado("Fortaleza", 2687000, ["Petróleo", "Turismo"])

municipios = [
    Municipio("São Paulo - Capital", 12300000, "Indústria e Serviços"),
    Municipio("Fortaleza - Capital", 2687000, "Turismo e Comércio"),
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simular', methods=['GET'])
def simular():
    # Simula crescimento populacional em 1%
    sao_paulo.simular_crescimento_populacional(0.01)
    fortaleza.simular_crescimento_populacional(0.02)

    resultados = {
        "estados": [
            {"nome": sao_paulo.nome, "populacao": sao_paulo.populacao, "recursos": sao_paulo.recursos_naturais},
            {"nome": fortaleza.nome, "populacao": fortaleza.populacao, "recursos": fortaleza.recursos_naturais},
        ],
        "municipios": [
            {"nome": m.nome, "populacao": m.populacao, "economia": m.economia} for m in municipios
        ]
    }

    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)
