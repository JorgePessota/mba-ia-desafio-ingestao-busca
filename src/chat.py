from search import search_prompt

def main():
    while True:
        try:
            user_input = input("Faça sua pergunta (digite \"sair\" para encerrar): ")

            if user_input.lower() in ["sair"]:
                print("Até logo!")
                break 
          
            chain = search_prompt(user_input)

            if not chain:
                print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
                return 
            else:
                print(chain) 

        except Exception as e:
            print(f"Ocorreu um erro {e}") 

    

if __name__ == "__main__":
    main()