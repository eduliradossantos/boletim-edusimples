#Lista onde serão armazenados os dicionários com dados de cada aluno. A matrícula começa com 0001.

alunos = [
    {"matricula": "0001", "nome": "Ana Souza", "n1": 8.5, "n2": 7.0},
    {"matricula": "0002", "nome": "Bruno Lima", "n1": 5.0, "n2": 6.0},
    {"matricula": "0003", "nome": "Carlos Mendes", "n1": 9.0, "n2": 8.5},
    {"matricula": "0004", "nome": "Daniela Castro", "n1": 4.0, "n2": 3.5},
    {"matricula": "0005", "nome": "Eduardo Lira", "n1": 8.0, "n2": 9.0}
]


#Funções para que haja funcionalidades CRUD

def cadastrar():
    try:
       matricula = input("Digite a matrícula: ").strip() #a função .strip() removerá espaços inúteis
       nome = input("Digite o nome: ").strip()
       n1 = float(input("Digite a primeira nota: "))
       n2 = float(input("Digite a segunda nota: "))
       
       aluno = {
           "matricula": matricula,
           "nome": nome,
           "n1": n1,
           "n2": n2
       }
       alunos.append(aluno)
       print("\nAluno cadastrado com sucesso\n")
    except ValueError:
        print("\nFavor digitar notas válidas (números)\n")
        

def media(aluno):
    return (aluno["n1"] + aluno["n2"]) / 2


def situacao(aluno):
    m = media(aluno)
    if m >= 7:
        return "Aprovado"
    elif m >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def listar():
    if alunos:
        print("\n=== Lista de Alunos ===")
        for aluno in alunos:
            print(f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | "
                  f"Notas: {aluno['n1']}, {aluno['n2']} | "
                  f"Média: {media(aluno):.2f} | Situação: {situacao(aluno)}")
    else:
        print("\nNenhum aluno cadastrado.\n")


def alterar():
    matricula = input("Digite a matrícula do aluno: ").strip()
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            try:
                while True:  # mantém o menu até o usuário escolher sair
                    print("\nEscolha o que você quer alterar: ")
                    print("1 - Nome")
                    print("2 - Primeira Nota")
                    print("3 - Segunda Nota")
                    print("4 - Voltar ao menu principal")
                    
                    opcao_alterar = input("Digite a opção: ").strip()
                    
                    if opcao_alterar == "1":
                        aluno["nome"] = input("Novo nome: ").strip()
                        print("\nDado alterado com sucesso!\n")
                    elif opcao_alterar == "2":
                        aluno["n1"] = float(input("Nova nota 1: "))
                        print("\nDado alterado com sucesso!\n")
                    elif opcao_alterar == "3":
                        aluno["n2"] = float(input("Nova nota 2: "))
                        print("\nDado alterado com sucesso!\n")
                    elif opcao_alterar == "4":
                        print("\nVoltando ao menu principal...\n")
                        break
                    else:
                        print("\nOpção inválida! Tente novamente.\n")
            except ValueError:
                print("\nDigite notas válidas (números).\n")
            return
    print("\nAluno não encontrado\n")2
    
    

def excluir():
    matricula = input("Digite a matrícula do aluno: ").strip()
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print("\nAluno removido com sucesso!\n")
            return
    print("\nAluno não encontrado!\n")
    
    
def menu():
    
    while True:
        print("\n------- Boletim EduSimples -------")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Alterar aluno")
        print("4 - Excluir aluno")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            alterar()
        elif opcao == "4":
            excluir()
        elif opcao == "5":
            print("\nVocê saiu do sistema.\n")
            break
        else:
            print("\Opção inválida! Tente novamente.\n")


#Rodar o programa

menu()

    