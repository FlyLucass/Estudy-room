import random

class Pessoa():
    def __init__(self,nome,informacao):
        self.nome=nome
        self.informacao=informacao
         
    def exibir_dados(self):
        return f"Olá {self.nome} você é um {self.informacao}"
        
        
class Aluno(Pessoa):
    def __init__(self,nome,matricula,curso,notas=[],informacao="Aluno"):
        Pessoa.__init__(self,nome,informacao)
        self._matricula=matricula #atributo protegido
        self.__curso=curso #atributo privado
        self.__notas=notas
    
    
    def media(self):
        return sum(self.__notas)/len(self.__notas)
    
    def situacao(self):
        if self.media()>=7:
            return "Aprovado"
        else:
            return "Reprovado"
    
    def exibir_dados(self):   
        return f"{'-'*50}\n{Pessoa.exibir_dados(self)} \nSeu curso é {self.__curso} \nSuas notas do semestre é {self.__notas}\nSua média é {self.media()}\nPor isso, sua situação é {self.situacao()}\n{'-'*50}"
        
        
    def trocar_curso(self,novo_curso):
        self.__curso=novo_curso
        
    def trocar_notas(self,novas_notas=[]):
        self.__notas=novas_notas
    
    def trocar_matricula(self,nova_matricula):
        self._matricula=nova_matricula
        
class Visitante(Pessoa):
    def __init__(self, nome, informacao="Visitante",id=None):
        Pessoa.__init__(self, nome, informacao)
        
        if id==None:id=random.randint(1,1000)
        self.__id=id
        
    def exibir_dados(self):
       return f"{'-'*50}\n{Pessoa.exibir_dados(self)}\nPrescrito sobre indetificação: {self.__id}\n{'-'*50}"
   
class Educador(Pessoa):
    def __init__(self, nome,area,informacao="Professor",identificador=None):
        Pessoa.__init__(self,nome, informacao)
        self.__area=area
        
        if identificador==None: identificador=random.randint(1000,2000)
        self.__identificador=identificador
        
    def exibir_dados(self):
        return f"{'-'*50} \n{Pessoa.exibir_dados(self)} \nSobre indeficação: {self.__identificador} \nSua aréa de atuação é: {self.__area} \n{'-'*50}"
        
        

pessoa1=Aluno("Lucas","202401","ADS",[10,10,10,10])
print(pessoa1.exibir_dados())
pessoa2=Visitante("Luan")
print(pessoa2.exibir_dados())
pessoa3=Educador("J","Medicina")
print(pessoa3.exibir_dados())
pesssoa4=Visitante("Kaio")
print(pesssoa4.exibir_dados())

