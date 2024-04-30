from models import Pessoas, db_session

# Insere os dados
def insert_data():
    pessoa = Pessoas(nome="Tomas", idade=26)
    print(pessoa)
    pessoa.save()

# Consulta a tabela
def query():
    pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Alex').first()
    print(pessoas)
    #print(pessoa.idade)


# Atualiza os dados
def update_data():
    pessoa = Pessoas.query.filter_by(nome='Alex').first()
    pessoa.idade = 21
    pessoa.save()

# Exclui registro
def exclude():
    pessoa = Pessoas.query.filter_by(nome='Tomas').first()
    pessoa.delete()

if __name__ == '__main__':
    #insert_data()
    #update_data()
    #exclude()
    # query()
    # insert_data()
    query()