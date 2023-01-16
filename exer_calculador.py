while True:
    num_1 = int(input('Digite um numero '))
    num_2 = int(input('Digite outro numero '))
    sinal = input('Digite o operador ')

    if sinal == '/':
        print (num_1 / num_2)    
    elif sinal == '*':
        print (num_1 * num_2)    
    elif sinal == '+':
        print (num_1 + num_2)    
    elif sinal == '-':
        print (num_1 - num_2)    
    print('Digite "sair" se quiser fechar o programa')    


    '''
     sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    '''