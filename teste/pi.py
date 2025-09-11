import random

palavras = ["tabela" , "script", "chaves", "delete", "cedula"]

def jogo():
    print("======= ADIVINHE A PALAVRA! ======\n===== A palavra tem 6 letras =====")

    adivinhar = random.choice(palavras)
    #print(adivinhar)
    opcao = ""
    while True:
        tentativa = input("Digite sua tentativa: ").lower()

        if len(tentativa) != 6:
            print("A palavra deve ter exatamente 6 letras.")
            continue

        resultado = ""

        for i in range(6):
            if tentativa[i] == adivinhar[i]:
                resultado += f"{tentativa[i].upper()}🟩 "
            elif tentativa[i] in adivinhar:
                resultado += f"{tentativa[i].upper()}🟧 "
            else:
                resultado += f"{tentativa[i].upper()}🟥 "

        print(resultado.strip())
        
        if tentativa == adivinhar:
            print("Parabéns! Você acertou a palavra!")
            break
        
        print("======= 1-Continuar =======")
        print("========= 2-Dica ==========")
        
        opcao = input()
        if opcao == "1":
            continue
        if opcao == "2":
            
            if adivinhar == "tabela":
                print("Você encontra em um calendário, em uma planilha ou até no horario de aulas da escola.")
                
            if adivinhar == "script":
                print("É como um roteiro de teatro ou cinema, mas pode ser usado para dar instruções a um computador.")
                    
            if adivinhar == "chaves":
                print("Servem para abrir portas na vida real, e também são usadas em códigos.")
                    
            if adivinhar == "delete":
                print("Em inglês significa apagar, e aparece em um botão do teclado.")
                    
            if adivinhar == "cedula":
                print("Você usa para pagar, mas também pode aparecer em eleições.")

def menu():
    while True:
        print("\n======= BEM-VINDO AO TERMO =======")
        print("============ 1- Jogar ============")
        print("============ 2- Sair =============")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            jogo()
        elif escolha == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()