from RepositorioAluno import RepositorioAluno


def possui_numeros(texto):
    return any(caractere.isdigit() for caractere in texto)


try:
    aluno = RepositorioAluno()

    while True:
        try:
            numero = int(input("__MENU__\n 1. Adicionar Aluno\n 2. Verificar Alunos\n 0. Sair\n"))

            if numero == 1:
                nome_aluno = input("Digite o nome do Aluno: ")
                if possui_numeros(nome_aluno):
                    print("Erro: O nome do aluno não deve conter números.")
                    continue
                nota_aluno = float(input("Digite a nota do Aluno: "))
                aluno.nome(nome_aluno)
                aluno.notas(nota_aluno)

            elif numero == 2:
                aluno.mostraAlunos()

            elif numero == 0:
                print("Programa interrompido! Saindo do programa...")
                break
            else:
                print("Opção inválida. Escolha uma opção válida.")

        except ValueError:
            print("Erro: Digite um valor numérico válido.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
