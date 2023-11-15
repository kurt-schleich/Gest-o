from funcionario import Funcionario
from irh_service import IRHService
from professor import Professor
from sta import STA
from terceirizado import Terceirizado

class RHService(IRHService):
    def __init__(self):
        self.folha_pagamento = []

    def cadastrar(self, funcionario: Funcionario):
        if isinstance(funcionario, Terceirizado):
            if type(funcionario.insalubridades) is not bool:
                return False
        elif isinstance(funcionario, STA):
            if 0 > funcionario.xp or funcionario.xp > 30:
                return False
        elif isinstance(funcionario, Professor):
            if funcionario.classe != 'A':
                if funcionario.classe != 'B':
                    if funcionario.classe != 'C':
                        if funcionario.classe != 'D':
                            if funcionario.classe != 'E':
                                return False
        for funcionarios in self.folha_pagamento:
            if funcionario.getCpf() == funcionarios.getCpf():
                return False
        self.folha_pagamento.append(funcionario)
        return True

    def remover(self, cpf: str):
        for funcionarios in self.folha_pagamento:
            if funcionarios.getCpf() == cpf:
                self.folha_pagamento.remove(funcionarios)
                return True
        return False

    def obterFuncionario(self, cpf: str):
        for funcionario in self.folha_pagamento:
            if funcionario.getCpf() == cpf:
                return funcionario
        return None

    def getFuncionarios(self):
        organizando = []
        final = []
        for func in self.folha_pagamento:
            organizando.append(func.getNome())
        organizando = sorted(organizando)
        for nomes in organizando:
            for func in self.folha_pagamento:
                if func.getNome() == nomes:
                    final.append(func)
        return final

    def getFuncionariosPorCategorias(self, tipo):
        profs = []
        profos = []
        stas = []
        staos = []
        tercs = []
        tercos = []
        if tipo.value == 1:
            for funcionario in self.folha_pagamento:
                if isinstance(funcionario, Professor):
                    profs.append(funcionario)
            for func in profs:
                profos.append(func.getNome())
            organizando = sorted(profos)
            profos = []
            for nomes in organizando:
                for func in profs:
                    if func.getNome() == nomes:
                        profos.append(func)
            return profos
        elif tipo.value == 2:
            for funcionario in self.folha_pagamento:
                if isinstance(funcionario, STA):
                    stas.append(funcionario)
            for func in stas:
                staos.append(func.getNome())
            organizando = sorted(staos)
            staos = []
            for nomes in organizando:
                for func in stas:
                    if func.getNome() == nomes:
                        staos.append(func)
            return staos

        elif tipo.value == 3:
            for funcionario in self.folha_pagamento:
                if isinstance(funcionario, Terceirizado):
                    tercs.append(funcionario)
            for func in tercs:
                tercos.append(func.getNome())
            organizando = sorted(tercos)
            tercos = []
            for nomes in organizando:
                for func in tercs:
                    if func.getNome() == nomes:
                        tercos.append(func)
            return tercos

    def getTotalFuncionarios(self):
        return len(self.folha_pagamento)

    def solicitarDiaria(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if isinstance(funcionario, Professor):
            if funcionario.diarias < 3:
                funcionario.diarias += 1
                return True
            else:
                return False

        if isinstance(funcionario, STA):
            if funcionario.diarias < 1:
                funcionario.diarias += 1
                return True
            else:
                return False

        if isinstance(funcionario, Terceirizado):
            return False

    def partilharLucros(self, valor: float):
        if 0 >= len(self.folha_pagamento):
            return False

        val = valor/len(self.folha_pagamento)
        for func in self.folha_pagamento:
            func.lucros += val
        return True

    def iniciarMes(self):
        for func in self.folha_pagamento:
            func.diarias = 0
            func.lucros = 0

    def calcularSalarioDoFuncionario(self, cpf: str):
        for funcionario in self.folha_pagamento:
            if funcionario.getCpf() == cpf:
                if isinstance(funcionario, Professor):
                    if funcionario.classe == 'A':
                        funcionario.sal = 3000
                    elif funcionario.classe == 'B':
                        funcionario.sal = 5000
                    elif funcionario.classe == 'C':
                        funcionario.sal = 7000
                    elif funcionario.classe == 'D':
                        funcionario.sal = 9000
                    elif funcionario.classe == 'E':
                        funcionario.sal = 11000
                    return funcionario.getSalario()

                if isinstance(funcionario, STA):
                    funcionario.sal = 1000 + (funcionario.xp * 100)
                    return funcionario.getSalario()

                if isinstance(funcionario, Terceirizado):
                    if funcionario.insalubridades:
                        funcionario.sal = 1500
                        return funcionario.getSalario()
                    else:
                        funcionario.sal = 1000
                    return funcionario.getSalario()

    def calcularFolhaDePagamento(self):
        counter = 0
        for func in self.folha_pagamento:
            counter += self.calcularSalarioDoFuncionario(func.getCpf())
        return counter

    '''def calcularFolhaComPL(self):
        self.partilharLucros()'''
