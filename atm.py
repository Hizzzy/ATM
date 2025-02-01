while True:  
    password = 1234
    qui = 0
    balance = 1000000

    print('====WELCOME TO HIZZY TELLER MACHINE====')
    print('')
    print('Enter 0 to terminate')
    print('')
    ps = int(input('Enter Password: '))


    if ps == password:
       
        print('A for deposit')
        print('B for balance')
        print('C for withdraw')
        print('D for transfer ')

        choice = input('Enter your choice: ')
        if choice == 'A':
            amout = int(input('Enter your Amount: '))
            bal = amout + balance
            print(f"Your current balance is ${bal}")
        

        elif choice == 'B':
            print(f'You currently have {balance}')
            
        elif choice == 'C':
            withd = int(input('Enter the amount you want to collect: '))
            if withd > balance: 
                print('You have insufficient funds')
            else:
                print(f"You've comot your money")
        if choice != ['A', 'B', 'C']:
            print('Enter valid choice')
    elif ps == qui:
        break
    elif ps == ValueError: 
        print('Enter somethimg')
            
    else:
        print('')
        print(' Your password is incorrect')