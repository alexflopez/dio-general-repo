#NOTAS

- A pasta models é responsável por armazenar a lógica de conexão com o banco de dados da aplicação;
- A aplicação persiste os dados (arquivo 'atividades.db') utilizando sqlite para armazenar as entradas e atualizações/deleções de dados;
- O arquivo test.py simula os métodos restful, já que não é possível testar via Postman sem uma camada adicional de segurança;
- Para instalar as dependências, basta executar no terminal o comando: pip install -r requirements.txt
