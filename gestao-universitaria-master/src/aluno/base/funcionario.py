class Funcionario:
    def __init__(self, cpf, nome):
        self.nome = nome
        self.cpf = cpf
        self.diarias = 0
        self.lucros = 0

    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self) -> float:
        pass
