def todo_list():
    tasks = []

    while True:
        print("\n--- LISTA DE SARCINI ---")
        print("1. Vezi sarcinile")
        print("2. Adauga sarcina")
        print("3. Sterge sarcina")
        print("4. Iesire")

        choice = input("Alege o optiune (1-4): ")  
        
        if choice == '1':
            if not tasks:
                print("Nu exista sarcini in lista.")
            else:
                print("Sarcini:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == '2':
            task = input("Introdu o noua sarcina: ")
            tasks.append(task)
            print(f'Sarcina "{task}" a fost adaugata.')

        elif choice == '3':
            if not tasks:
                print("Nu exista sarcini de sters.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                num = int(input("Introdu numarul sarcinii de sters: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Sarcina '{removed}' a fost stearsa!")
                else:
                    print("Numar de sarcina invalid.")

        elif choice == '4':
            print("Iesire din aplicatia lista de sarcini.")
            break

        else:
            print("Optiune invalida. Te rog alege o optiune valida.")

todo_list()