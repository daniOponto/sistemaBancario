class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.limite_saque = 500.00
        self.saques_diarios = 3
        self.saques_realizados = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Tente novamente.")

    def sacar(self, valor):
        if self.saques_realizados >= self.saques_diarios:
            print("Limite de saques diários atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor > self.limite_saque:
            print(f"O valor máximo para saque é R$ {self.limite_saque:.2f}.")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Exemplo de uso do sistema bancário
banco = SistemaBancario()

# Depósitos
banco.depositar(1000.45)
banco.depositar(500)

# Saques
banco.sacar(300)
banco.sacar(200)
banco.sacar(100)

# Exibir extrato
banco.exibir_extrato()

# Tentativa de saque sem saldo suficiente
banco.sacar(600)

# Tentativa de saque após atingir o limite de 3 saques
banco.sacar(50)

# Exibir extrato final
banco.exibir_extrato()
