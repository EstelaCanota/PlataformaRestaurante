import os
import unicodedata

def normalizar(texto: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) !="Mn"
    ).lower()



restaurantes = [{"Nome" : "Praça", "Categoria":"Japonesa", "Ativo": False}, 
                {"Nome" : "Bk", "Categoria":"Lanches", "Ativo": True},
                {"Nome": "Nidos", "Categoria":"Italiano", "Ativo": False}]


def exibir_nome():
    print(""" 
𝑺𝒂𝒃𝒐𝒓 𝑬𝒙𝒑𝒓𝒆𝒔𝒔
""")


def exibir_opções():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def finalizar_app():
    exibir_subtitulo("Finalizando app")

def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal :)")
    main()

def opção_inválida():
    print("Opção inválida\n")
    
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")
    
    dados_do_restaurante = {
        "Nome": nome_restaurante,
        "Categoria": categoria,
        "Ativo": False
    }
    
    restaurantes.append(dados_do_restaurante)  # <-- sempre adiciona dicionário
    print(f"Restaurante {nome_restaurante} foi cadastrado com sucesso!\n")
    
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")

    for restaurante in restaurantes:
        if isinstance(restaurante, dict):  # garante que é dicionário
            nome_restaurante = restaurante["Nome"]
            categoria = restaurante["Categoria"]
            ativo = "Ativo" if restaurante["Ativo"] else "Inativo"
            print(f"- {nome_restaurante} | {categoria} | {ativo}")
        else:
            print(f"- {restaurante} (inválido)")  # debug pra ver se ficou string solta

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if normalizar(nome_restaurante) == normalizar(restaurante["Nome"]):
            restaurante_encontrado = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            mensagem = (
                f"O restaurante {restaurante['Nome']} foi ativado com sucesso!"
                if restaurante["Ativo"]
                else f"O restaurante {restaurante['Nome']} foi desativado com sucesso!"
            )
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")
        
    voltar_ao_menu_principal()



def escolher_opção():
    try:
        op_escolhida = int(input("Escolha uma opção: "))

        if op_escolhida == 1:
            cadastrar_restaurante()
        elif op_escolhida == 2:
            listar_restaurantes()
        elif op_escolhida == 3:
            alternar_estado_restaurante()
        elif op_escolhida == 4:
            finalizar_app()
        else:
            opção_inválida()
    except:
        opção_inválida()


def main():
    os.system("cls")
    exibir_nome()
    exibir_opções()
    escolher_opção()


if __name__ == "__main__":
    main()
