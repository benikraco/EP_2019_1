# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Fulano da Silva, fulanos@insper.edu.br
# - aluno B: Sicrano de Almeida, sicranoa1@insper.edu.br
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "tobogã": "Entrar no tobogã"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                "biblioteca":"Ir para a biblioteca",
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "tobogã": "Entrar no tobogã"
            }
        },
        "tobogã": {
            "titulo": "Prédio 2 do Insper",
            "descricao": "Você está no terceiro andar do prédio 2 do Insper",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "sala secreta": "Ir para a sala secreta"
        },
        "sala secreta": {
            "titulo": "Sala de entidades",
            "descricao": "Você está na mesa com os veteranos do D.A. Vários itens estão espalhados pela mesa.",
            "opcoes":{
                "inicio": "Voltar para o saguao de entrada",
                "biblioteca": "Ir para a biblioteca"
        },
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    cenarios, nome_cenario_atual = carregar_cenarios()
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        print (cenario_atual['titulo'])
        print ("-"*len(cenario_atual['titulo']))
        print (cenario_atual['descricao'])
        import random
        monstrinho=random.randint(0,3)
        if len(cenario_atual['opcoes']) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            print ()
            print ("As suas opções são: ")
            print ()
            for k,v in cenario_atual['opcoes'].items():
                print ("{0} - {1}".format(k,v))
            print ()
            escolha = str(input('Qual é a sua escolha?'))
            if escolha in cenario_atual['opcoes']:
                nome_cenario_atual = escolha
                itens = ['Protoboard','Arduíno','Computador','Chave']
                if escolha == "sala secreta":
                    print ("Você encontrou alguns itens! Qual deseja levar?")
                    print ()
                    print (itens)
                    item=str(input('insira aqui o seu item: '))
                    print("Voce agora tem um {}".format(item))
                    print ()
                    print ("As suas opções são: ")
                    print ()
                    for k,v in cenario_atual['opcoes'].items():
                        print ("{0} - {1}".format(k,v))
                        print ()
                    escolha = str(input('Qual é a sua escolha?'))
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
