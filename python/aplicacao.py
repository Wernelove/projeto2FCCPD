import mysql.connector
from enum import Enum
import os

class E(Enum):
    OPCAO_INVALIDA = 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tipoUsuario():
    print("[1] - Usuário")
    print("[2] - Administrador")
    print("[3] - Sair")

    option = int(input("Opção: "))
    clear_screen()
    return option


def crudPannel(option):
    match option:
        case 1:
            print("[1] - Alugar livro")
            print("[2] - Devolver livro")
            print("[3] - Livros disponiveis")
            print("[4] - Sair")
            option = int(input("Opção: "))
            clear_screen()
            return option

        case 2:
            print("[1] - Adicionar livro")
            print("[2] - Remover livro")
            print("[3] - Sair")
            option = int(input("Opção: "))
            clear_screen()
            return option

        case 3:
            exit()

        case default:
            print("Opção Inválida")
            return E.OPCAO_INVALIDA

def alugarLivro():

    try:
        livro_id = int(input("Digite o ID do livro que deseja alugar: "))
        # SQL para marcar o livro como alugado 
        sql_alugar = "UPDATE livros SET status = 'Alugado' WHERE id = %s"
        cursor.execute(sql_alugar, (livro_id,))
        conexao.commit()
        print("Livro alugado com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao alugar o livro: {str(e)}")

def devolverLivro():

    try:
        livro_id = int(input("Digite o ID do livro que deseja devolver: "))
        # SQL para marcar o livro como disponível  
        sql_devolver = "UPDATE livros SET status = 'Disponível' WHERE id = %s"
        cursor.execute(sql_devolver, (livro_id,))
        conexao.commit()
        print("Livro devolvido com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao devolver o livro: {str(e)}")

def livrosDisponiveis():
   
    try:
        # SQL para selecionar livros disponíveis 
        sql_disponiveis = "SELECT * FROM livros WHERE status = 'Disponível'"
        cursor.execute(sql_disponiveis)
        livros = cursor.fetchall()

        print("Livros disponíveis:")
        for livro in livros:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}")

    except Exception as e:
        print(f"Erro ao verificar livros disponíveis: {str(e)}")

def adicionarLivro():

    try:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        # Adapte conforme sua tabela de livros
        sql_adicionar = "INSERT INTO livros (titulo, autor, status) VALUES (%s, %s, %s)"
        cursor.execute(sql_adicionar, (titulo, autor, 'Disponível'))
        conexao.commit()
        print("Livro adicionado com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao adicionar o livro: {str(e)}")

def removerLivro():

    try:
        livro_id = int(input("Digite o ID do livro que deseja remover: "))
        # Adapte conforme sua tabela de livros
        sql_remover = "DELETE FROM livros WHERE id = %s"
        cursor.execute(sql_remover, (livro_id,))
        conexao.commit()
        print("Livro removido com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao remover o livro: {str(e)}")




# -------------------------- banco --------------------------
"""conexao = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

cursor = conexao.cursor()"""

# -------------------------- banco --------------------------


# -------------------------- crud --------------------------
user_type = tipoUsuario()
crud_pannel = crudPannel(user_type)

if(user_type == 2):
    if(crud_pannel == 1):
        adicionarLivro()
    elif(crud_pannel == 2):
        removerLivro()
    else:
        exit()

elif(user_type == 1):
    if(crud_pannel == 1):
        alugarLivro()
    elif(crud_pannel == 2):
        devolverLivro()
    elif(crud_pannel == 3):
        livrosDisponiveis()
    else:
        exit()


try:
    sql_inserting = "INSERT INTO nome_tabela (coluna1, coluna2, coluna3) VALUES (%s, %s, %s)"
    data = ("valor_coluna1", "valor_coluna2", "valor_coluna3")
    cursor.execute(sql_inserting, data)
    conexao.commit()

    print("Dados inseridos com sucesso")

except Exception as instancia:
    conexao.rollback()
    print(f"Dados não inseridos. Erro {type(instancia)}")

finally:
    print("fim de operação")