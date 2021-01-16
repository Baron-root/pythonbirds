class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    soares = Pessoa(nome='soares')
    vando = Pessoa(soares, nome='vando')
    print(Pessoa.cumprimentar(vando))
    print(id(vando))
    print(vando.cumprimentar())
    print(vando.nome)
    print(vando.idade)
    for filhos in vando.filhos:
        print(filhos.nome)
    vando.sobrenome = 'Dantas'
    del vando.filhos
    vando.olhos = 1
    print(vando.__dict__)
    print(soares.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(vando.olhos)
    print(soares.olhos)
    print(id(Pessoa.olhos), id(soares.olhos), id(vando.olhos))

