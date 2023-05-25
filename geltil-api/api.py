from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)
# Rota para criar um novo registro na tabela Pessoas
conn = psycopg2.connect(
        host="172.20.0.2",
        database="gentil_db",
        user="postgres",
        password="pg123"
    )

@app.route('/pessoas', methods=['POST'])
def criar_pessoa():
    conn = psycopg2.connect(
        host="localhost",
        database="nome_do_banco",
        user="seu_usuario",
        password="sua_senha"
    )
    cur = conn.cursor()

    # Recuperar os dados do JSON enviado na requisição
    data = request.get_json()
    objetivo = data['objetivo']
    nome = data['nome']
    data_nascimento = data['dataNascimento']
    salario = data['salario']
    observacoes = data['observacoes']
    nome_mae = data['nomeMae']
    nome_pai = data['nomePai']
    cpf = data['cpf']

    # Chamar a procedure de criação de registro
    cur.execute(
        "CALL criar_registro_pessoa(%s, %s, %s, %s, %s, %s, %s, %s)",
        (objetivo, nome, data_nascimento, salario,
         observacoes, nome_mae, nome_pai, cpf)
    )

    # Recuperar o valor de retorno da procedure (idPessoa)
    id_pessoa = cur.fetchone()[0]

    # Exibir o idPessoa no console
    print("ID Pessoa:", id_pessoa)

    # Confirmar as alterações no banco de dados
    conn.commit()

    cur.close()
    conn.close()

    return "Registro criado com sucesso"
# Rota para obter todos os registros da tabela Pessoas


@app.route('/pessoas', methods=['GET'])
def get_pessoas():
    
    cur = conn.cursor()

    cur.execute("SELECT * FROM Pessoas")
    rows = cur.fetchall()

    # Converter os resultados em um formato JSON
    pessoas = []
    for row in rows:
        pessoa = {
            'idPessoa': row[0],
            'Objetivo': row[1],
            'nome': row[2],
            'dataNascimento': str(row[3]),
            'salario': float(row[4]),
            'observacoes': row[5],
            'nomeMae': row[6],
            'nomePai': row[7],
            'cpf': row[8]
        }
        pessoas.append(pessoa)

    cur.close()
    conn.close()

    return jsonify(pessoas)


if __name__ == '__main__':
    app.run()
