from funcionario import Funcionario


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        super().__init__(cpf, nome)
        self.classe = classe
        self.sal = 0

    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self) -> float:
        return self.sal + (self.diarias * 100) + self.lucros
