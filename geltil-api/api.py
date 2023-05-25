from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def db_connect():
    conn = psycopg2.connect(
        host="172.20.0.2",
        database="gentil_db",
        user="postgres",
        password="pg123"
    )
    cur = conn.cursor()
    return conn, cur

# Rota para criar um novo registro na tabela Pessoas
@app.route('/pessoas', methods=['POST'])
def criar_pessoa():
    conn, cur = db_connect();
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
        "CALL inserir_pessoa(%s, %s, %s, %s, %s, %s, %s, %s)",
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

# Rota para atualizar registros na tabela de Pessoas
@app.route('/pessoas', methods=['PUT'])
def atualizar_pessoa():
    data = request.json
    id_pessoa = data['idPessoa']
    objetivo = data['objetivo']
    nome = data['nome']
    data_nascimento = data['dataNascimento']
    salario = data['salario']
    observacoes = data['observacoes']
    nome_mae = data['nomeMae']
    nome_pai = data['nomePai']
    cpf = data['cpf']

    conn, cur = db_connect()

    try:
        cur = conn.cursor()

        # Chamar a procedure de atualização de pessoa
        cur.execute("CALL atualizar_pessoa(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (id_pessoa, objetivo, nome, data_nascimento, salario, observacoes, nome_mae, nome_pai, cpf))

        # Recuperar o texto retornado pela procedure
        resultado = cur.fetchone()

        # Imprimir o texto no console
        print(resultado)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        conn.close()

    return 'Registro atualizado com sucesso'

@app.route('/pessoas/<int:id>', methods=['DELETE'])
def remover_pessoa(id):
    conn, cur = db_connect()

    try:
        cur = conn.cursor()

        # Chamar a procedure de remoção passando o id do registro a ser removido
        # cur.callproc('remover_pessoa', [id])

         # Call the procedure to remove a person
        cur.execute("CALL remover_pessoa(%s)", (id,))
       
        # Recuperar o texto retornado pela procedure
        resultado = cur.fetchone()[0]

        # Imprimir o texto no console
        print(resultado)

        cur.close()
        conn.commit()
        return "Registro removido com sucesso"

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Erro ao remover registro"

    finally:
        conn.close()

# Rota para obter todos os registros da tabela Pessoas
@app.route('/pessoas2', methods=['GET'])
def get_pessoas():
    conn, cur = db_connect()
    #cur = conn.cursor()

    cur.execute("SELECT * FROM Pessoas")
    rows = cur.fetchall()

    # Converter os resultados em um formato JSON
    pessoas = []
    for row in rows:
        pessoa = {
            'idPessoa': row[0],
            'objetivo': row[1],
            'nome': row[2],
            'dataNascimento': str(row[3]),
            'salario': float(row[4]),
            'observacoes': row[5],
            'cpf': row[6],
            'nomeMae': row[7],
            'nomePai': row[8]
        }
        pessoas.append(pessoa)

    cur.close()
    conn.close()

    return jsonify(pessoas)

@app.route('/pessoas', methods=['GET'])
def selecionar_pessoas():
    conn, cur = db_connect()

    try:
        cur = conn.cursor()

        # Chamar a procedure de seleção de pessoas
        cur.execute("CALL selecionar_todas_pessoas()")

        # Recuperar os dados retornados pela procedure
        resultado = cur.fetchall()

        # Imprimir os dados no console
        for row in resultado:
            print(row)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        conn.close()

    return 'Registros selecionados com sucesso'

# Rota para selecionar um registro da tabela Pessoas
@app.route('/pessoas/<int:id>', methods=['GET'])
def obter_pessoa(id):
    conn, cur = db_connect()

    try:
        cur = conn.cursor()

        # Chamar a procedure de obter um registro por ID usando CALL
        cur.execute("CALL obter_pessoa_por_id(%s::INTEGER)", (id,))
        # Recuperar os dados do registro retornado pela procedure
        resultado = cur.fetchone()

        # Imprimir os dados no console
        print(resultado)

        cur.close()
        conn.commit()

        # Retornar os dados como resposta para a API
        return "Registro obtido com sucesso"

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return "Erro ao obter registro"

    finally:
        conn.close()

if __name__ == '__main__':
    app.run()
