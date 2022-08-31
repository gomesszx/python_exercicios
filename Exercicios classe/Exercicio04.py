class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario 

    def aumentar_salario(self):
        percentual = int(input('Digite o percentual'))
        valor_aumento = ((percentual / 100) * self.salario)
        salario_atual = valor_aumento + self.salario
        return salario_atual


nome = input('Digite seu nome')
salario = float(input('Digite seu salário'))
percentual = 0
funcionario_01 = Funcionario(nome,salario)
print(funcionario_01.aumentar_salario())