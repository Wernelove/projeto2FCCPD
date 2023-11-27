# Passo a passo para executar o container

Os seguintes comandos devem ser executados em sequencia, aguardando serem 100% finalizados antes de inserir o próximo:

docker-compose up
docker-compose down
docker-compose up
docker compose create
docker compose start
docker compose exec -t pythonapp sh
python aplicacao.py

# Operações CRUD

- É possivel acessar o sistema de gerenciamento como usuário padrão(1) ou administrador(2); Além disso também pode ser selecionado a opção de sair do CRUD(3)
  
- Usuário padrão:
  - Alugar livro(1)
  - Devolver livro(2)
  - Ver livros disponiveis(3)
  - Sair(4)

- Administrador:
  - Adicionar livro(1)
  - Remover livro(2)
  - Sair(3)
