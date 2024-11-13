import os
os.system('cls')

# criando uma conta para o usuário

class Conta:
    def __init__(self, numero, titular, senha, saldo=0):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo

# verificar o saldo (extrato)

    def verificar_saldo(self):
        return self.saldo

# fazer depósito

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'\033[32mDepósito de R${valor:.2f} realizado com sucesso!\033[0m')
        else:
            print('\033[91mO valor do depósito deve ser positivo.\033[0m')

# sistema de saque

    def sacar(self, valor):
        if valor <= 0:
            print('\033[91mO valor do saque deve ser positivo.\033[0m')
        elif valor > self.saldo:
            print('\033[91mSaldo insuficiente para realizar o saque.\033[0m')
        else:
            self.saldo -= valor
            print(f'\033[92mSaque de R${valor:.2f} realizado com sucesso.\033[0m')

class CaixaEletronico:
    def __init__(self):
        self.contas = {}

# criação de conta

    def criar_conta(self, numero, titular, senha):
        if numero not in self.contas:
            self.contas[numero] = Conta(numero, titular, senha)
            print(f'\n\033[32mUma Conta foi criada com sucesso para {titular}! \033[0m')
        else:
            print('\n\033[91mO número da conta digitado já existe.\033[0m')

# acessar a conta do usuário (verifica senha)
    
    def acessar_conta(self, numero, senha):
        conta = self.contas.get(numero, None)
        if conta and conta.senha == senha:
            return conta
        else:
            return None

def main():
    caixa = CaixaEletronico()

    while True:
        print("=" * 30)
        print("{:^30}".format("WALLIS BANK"))
        print("=" * 30)
        print("\n1 --------> criar uma conta")
        print("2 --------> acessar uma conta")
        print("3 --------> para sair do sistema")
        opcao_inicial = input("\nDigite a opção: ")

        if opcao_inicial == '1':
            titular = input("\nInforme o seu nome completo: ")

# validação do número da conta ter 5 dígitos
            
            while True:
                numero = input("\nDigite o número da sua conta com cinco dígitos: ")
                if numero.isdigit() and len(numero) == 5:
                    break
                else:
                    print("\033[91mO número da conta deve conter exatamente 5 dígitos. Tente novamente.\033[0m")

# validação da senha com quatro dígitos

            while True:
                senha = input("\nCrie uma senha de 4 dígitos numéricos: ")
                if senha.isdigit() and len(senha) == 4:
                    break
                else:
                    print("\033[91mA senha deve conter exatamente 4 dígitos. Tente novamente.\033[0m")

            caixa.criar_conta(numero, titular, senha)

        elif opcao_inicial == '2':
            numero = input("Digite o número da sua conta: ")
            senha = input("Digite a sua senha (4 dígitos): ")
            conta = caixa.acessar_conta(numero, senha)

            if conta:
                while True:
                    print(f"\n\033[32mBem-vindo, {conta.titular}!\033[0m")
                    print("\nDigite 1 para verificar seu saldo")
                    print("Digite 2 para depositar")
                    print("Digite 3 para sacar")
                    print("Digite 4 para sair")
                    opcao = input("\nEscolha uma opção: ")

                    if opcao == '1':
                        saldo = conta.verificar_saldo()
                        print(f'\033[33mSeu saldo é de: R${saldo:.2f}\033[0m')
                    elif opcao == '2':
                        valor = float(input("Digite o valor que irá depositar: "))
                        conta.depositar(valor)
                    elif opcao == '3':
                        valor = float(input("Digite o valor que irá sacar: "))
                        conta.sacar(valor)
                    elif opcao == '4':
                        print('\033[32mObrigado por usar o Wallis Bank. Volte sempre!\033[0m')
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
            else:
                print("\033[91mConta não encontrada ou senha incorreta. Por favor, tente novamente.\033[0m")

        elif opcao_inicial == '3':
            print('\n\033[33mObrigado por usar o Wallis Bank. Volte sempre!\033[0m')
            break
        else:
            print('\033[91mOpção inválida. Tente novamente.\033[0m')

if __name__ == '__main__':
    main()