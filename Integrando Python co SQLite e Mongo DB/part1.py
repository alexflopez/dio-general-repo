import pprint

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, Float, LargeBinary
from sqlalchemy.orm import declarative_base, relationship, Session


Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    # Método de representação da própria classe
    def __repr__(self):
        return f'User(id=({self.id}), name=({self.name}), cpf=({self.cpf}), endereço=({self.endereco}))'


class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(10), nullable=False) # NOT NULL
    agencia = Column(String(10), nullable=False)  # NOT NULL
    num = Column(Integer, nullable=False)  # NOT NULL
    #id_cliente = Column(Integer, nullable=False)  # NOT NULL
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    saldo = Column(Float(10), nullable=False)  # NOT NULL

    # Criando o relacionamento entre as classes User e Address
    cliente = relationship("Cliente", back_populates="conta")

    # Método de representação da própria classe
    def __repr__(self):
        return f'User(id=({self.id}), tipo=({self.tipo}), agencia=({self.agencia}), num=({self.num}), id_cliente=({self.id_cliente}), saldo=({self.saldo}))'


# Connection
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Recuperando as tabelas (investigando o esquema de banco de dados)
inspector_engine = inspect(engine)
#res = inspector_engine.has_table("cliente")
#print(inspector_engine.get_table_names())


with Session(engine) as session:
    alex = Cliente(
        id=423422,
        nome="Alex Lopez",
        cpf='123422444',
        endereco='Calle Independencia, 111 - San José - Tierra'
    )

    trevor = Cliente(
        id=124332,
        nome="Trevor Belomont",
        cpf='999852465',
        endereco="Comte d'Français, 111 - Saint Rémy - Villeneuve"
    )

    c1 = Conta(
        #id=100,
        tipo="Corrente",
        agencia="123-1",
        num=1231442,
        id_cliente=423422,
        saldo=100.0
    )

    c2 = Conta(
        #id=101,
        tipo="Poupança",
        agencia="342-x",
        num=1231442,
        id_cliente=124332,
        saldo=120.0
    )


    # Enviando para a persistência de dados
    session.add_all([alex, trevor, c1, c2])

    # commit (Validando o comando)
    session.commit()


stmt = select(*Cliente.__table__.columns)
rows = session.execute(stmt)

for item in rows:
    pprint.pp(item)

stmt = select(*Conta.__table__.columns)
rows = session.execute(stmt)

for item in rows:
    pprint.pp(item)
    