from Pessoa import Pessoa
class Aluno(Pessoa):
    
    #Tem nome e NOta
    def __init__(self, nome):
        self.nome = nome
    
    def notas (self, nota):
        self.nota = nota
    
    