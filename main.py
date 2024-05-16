from teacher_crud import TeacherCRUD

class CLI:
    def __init__(self):
        self.teacher_crud = TeacherCRUD("bolt://localhost:7687", "neo4j", "password")

    def menu(self):
        print("\n--- Teacher CRUD CLI ---")
        print("1. Criar novo professor")
        print("2. Buscar professor por nome")
        print("3. Atualizar CPF de professor")
        print("4. Deletar professor por nome")
        print("5. Sair")

    def run(self):
        while True:
            self.menu()
            choice = input("Escolha uma opção: ")

            if choice == "1":
                name = input("Nome do professor: ")
                ano_nasc = int(input("Ano de nascimento: "))
                cpf = input("CPF: ")
                self.teacher_crud.create(name, ano_nasc, cpf)
                print("Professor criado com sucesso!")

            elif choice == "2":
                name = input("Nome do professor: ")
                result = self.teacher_crud.read(name)
                print("Resultado da busca:")
                for record in result:
                    print(record)

            elif choice == "3":
                name = input("Nome do professor: ")
                new_cpf = input("Novo CPF: ")
                self.teacher_crud.update(name, new_cpf)
                print("CPF atualizado com sucesso!")

            elif choice == "4":
                name = input("Nome do professor a ser deletado: ")
                self.teacher_crud.delete(name)
                print("Professor deletado com sucesso!")

            elif choice == "5":
                print("Encerrando o programa...")
                break

            else:
                print("Opção inválida! Escolha novamente.")


if __name__ == "__main__":
    cli = CLI()
    cli.run()
