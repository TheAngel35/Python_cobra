from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO
fernandez= Pessoa(1,"Angel Santiago")
print (fernandez)
print("Daqui pra frente é acesso ao banco.")
db = Database()
pessoaDAO=PessoaDAO(db.conexao, db.cursor)
pessoas= pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)
  