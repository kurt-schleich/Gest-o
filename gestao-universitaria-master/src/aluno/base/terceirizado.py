from funcionario import Funcionario


class Terceirizado(Funcionario):

    def __init__(self, cpf: str, nome: str, insalubre: bool):
        super().__init__(cpf, nome)
        self.insalubridades = insalubre
        self.sal = 0

    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self) -> float:
        return self.sal + (self.diarias * 100) + self.lucros
