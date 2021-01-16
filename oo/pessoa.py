class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico ():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f' {cls} - olhos {cls.olhos}'

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
    print(Pessoa.metodo_estatico(), vando.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), vando.nome_e_atributos_de_classe())

