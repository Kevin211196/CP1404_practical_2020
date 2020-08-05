name = input('Enter name: ')
while True:
    print('(H)ello')
    print('(G)oodbye')
    print('(Q)uit')

    choice = input()

    if choice.upper() == 'H':
        print('Hello', name)
    elif choice.upper() == 'G':
        print('Goodbye', name)
    elif choice.upper() == 'Q':
        break
    else:
        print('Invalid choice')