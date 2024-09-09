#NOTE: construtor: criar uma classe
#metodo cuja acao dele é criar o objeto
#pra fazer o objeto nascer

#nunca se define atributo assim: 'nome: Juana', sempre use o construtor

class Pessoa:
    #os atributos sao sempre definidos dentro do metodo construtor
    #NOTE: metodo construtor, sempre recebe parametro
    def __init__(self,nome, idade, cpf, email):
        self.nome   = nome
        self.idade  = idade
        self.cpf    = cpf
        self.email  = email

#NOTE: Programa principal
if __name__=='__main__':
    #entrada de dados
    nome    = input('Informe o nome do usuário: ')
    idade   = int(input('Informe a idade do usuário: '))
    cpf     = input('Informe o CPF do usuário: ')
    email   = input('Informe o email do usuário: ')

    #instanciar objeto 
    usuario = Pessoa(nome, idade, cpf, email) #intanciar os parametros na ordem, se deixar um fora ele retorna nulo

    #saida de dados
    print(f'Nome: {usuario.nome}')
    print(f'Idade: {usuario.idade}')
    print(f'CPF: {usuario.cpf}')
    print(f'Email: {usuario.email}')