class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome
    def cumprimentar(self):
        return 'Olá'

if __name__ == "__main__":
    p = Pessoa('Maria')
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'José'
    print(p.nome)