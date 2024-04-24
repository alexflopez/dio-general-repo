import pprint

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://blablabla"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collection = db.test_collection

# payload
bank = [{
        "id": 423422,
        "nome": "Alex Lopez",
        "cpf": '123422444',
        "endereco": 'Calle Independencia, 111 - San José - Tierra',
        "id_conta": 100,
        "tipo": "Corrente",
        "agencia": "123-1",
        "num": 423422,
        "saldo": 100.0
        },
        {
        "id": 124332,
        "nome": "Trevor Belomont",
        "cpf": '999852465',
        "endereco": 'Comte dFrançais, 111 - Saint Rémy - Villeneuve',
        "id_conta": 101,
        "tipo": "Poupança",
        "agencia": "342-x",
        "num": 1231442,
        "saldo": 120.0
        }]


res = db.posts.insert_many(bank)

for data in bank.find():
    pprint.pp(data)

