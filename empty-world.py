import time

while True:
    print(8*'-', 'empty world(demo)', 8*'-')
    print('''jogar(1)
monstros(2)
sair(3)''')
    
    menu = input("Escolha: ")
    
    if menu == '1':
        print('vc acorda!')
        time.sleep(1.5)
        print('\nvc sai de casa')
        time.sleep(1.5)
        print('\nvc percebe que está só')
        time.sleep(1.5)
        print('\npor enquanto')
        time.sleep(1)
        
        print('''\nmansao(1)
bueiro(2)
hospital(3)''')
        
        escolha2 = input("Para onde ir? ")
        
        if escolha2 == '1': 
            print('\nvc entra na mansao')
            time.sleep(1)
            print('''\ntem 2 portas
porta1(1)
porta2(2)''')
            escolha3 = input("Qual porta? ")
            if escolha3 == '1': 
                print('\ndemo completa')
            elif escolha3 == '2':
                print('\ndemo completa')
                
        elif escolha2 == '2':
            print('\nestá muito escuro')
            time.sleep(1)
            print('\nvc decide explorar')
            time.sleep(1)
            print('\ne acha uma lanterna')
            time.sleep(1)
            print('\ndemo completa')
            
        elif escolha2 == '3':
            print('\ntem uma gaveta')
            time.sleep(1)
            print('\nvc acha uma lanterna')
            time.sleep(1)
            print('\ndemo completa')	
            
    elif menu == '2':
        print('1-uburu, 2-trico, 3-gordli (mais em breve)')
        
    elif menu == '3':
        print('saindo...')
        time.sleep(0.5)
        break
    else:
        print('opcao invalida')
