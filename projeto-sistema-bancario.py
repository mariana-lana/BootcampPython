menu = '''
MENU
    [d] DEPÓSITO
    [s] SAQUE
    [e] EXTRATO
    [q] SAIR
'''

saldo = 0
saques = 0
limite = 500
LIMITE_SAQUES = 3
extrato_depositos = []
extrato_saques = []

while True:
    print(menu)
    opcao_escolhida = input('Escolha uma opção: ').lower()

    if opcao_escolhida == 'd':
        print('DEPÓSITO')

        try:
            valor_a_depositar = float(input('Quanto deseja depositar? R$'))
            if valor_a_depositar <= 0:
                raise ValueError
        except ValueError:
            print('ERRO. Por favor, digite um valor válido e positivo.')  
            continue 

        saldo += valor_a_depositar
        print(f'Depósito de R${valor_a_depositar:.2f} efetuado com sucesso.')
        print(f'Saldo atual: R${saldo:.2f}')
        extrato_depositos.append(valor_a_depositar)

    elif opcao_escolhida == 's':
        print('SAQUE')

        try:
            valor_a_sacar = float(input('Quanto deseja sacar? R$'))
            if valor_a_sacar <= 0:
                raise ValueError
        except ValueError:
            print('ERRO. Por favor, digite um valor válido e positivo.')
            continue

        if saques >= LIMITE_SAQUES:
            print('ERRO. Você já alcançou o limite de saques diários.')
            continue

        if valor_a_sacar > limite:
            print(f'ERRO. Não é possível realizar saques de valores maiores que R${limite:.2f}')
            continue

        if saldo < valor_a_sacar:
            print('ERRO. Saldo insuficiente para essa operação.')
            continue

        saldo -= valor_a_sacar
        saques += 1 
        extrato_saques.append(valor_a_sacar)
        print(f'Saque de R${valor_a_sacar:.2f} realizado com sucesso.')
        print(f'Saldo atual: {saldo:.2f}')

    elif opcao_escolhida == 'e':
        print('-' * 30)
        print('EXTRATO')
        print('-' * 30)

        if not extrato_depositos and not extrato_saques:
            print('Nenhuma operação realizada.')
        else:
            if extrato_saques:
                for saque in extrato_saques:
                    print(f'- R${saque:.2f}')      

            if extrato_depositos:
                for deposito in extrato_depositos:
                    print(f'+ R${deposito:.2f}')     

        print('-' * 30)
        print(f'SALDO: R${saldo:.2f}')
        print('-' * 30)          

    elif opcao_escolhida == 'q':
        print('Encerrando o sistema...')
        break

    else:
        print('Opção inválida. Por favor, digite uma opção válida.')



