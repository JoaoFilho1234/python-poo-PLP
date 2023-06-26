class RepositorioAluno():
    def __init__(self):
        self.nomeAluno = []
        self.notaAluno = []

    def nome(self,nome):
        self.nomeAluno.append(nome)
           
    def notas(self, nota ):
        self.notaAluno.append(nota)
        
      
    def mostraAlunos(self):
        print("LISTA DE ALUNOS")
        
        for aluno, nota in zip(self.nomeAluno , self.notaAluno):
            print("Nome: ",aluno)
            print("Nota: ",nota)
            print("\n")
        