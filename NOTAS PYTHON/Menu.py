from RepositorioAluno import RepositorioAluno
    
numero = int(input("__MENU__\n 1. Adicionar Aluno\n 2. Verificar Alunos\n 0. Sair\n"))
aluno = RepositorioAluno()
while numero!=0:
    
    if numero == 1:    
        
        aluno.nome((input("Digite o nome do Aluno: ")))
        aluno.notas((float(input("Digite a nota do Aluno: "))))

    if numero == 2:
        aluno.mostraAlunos()
    numero = int(input("__MENU__\n 1. Adicionar Aluno\n 2. Verificar Alunos\n 0. Sair\n"))