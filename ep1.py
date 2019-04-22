# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Beni Kracochansky, benik@alinsper.edu.br
# - aluno B: Amanda Ades, amandaa2@insper.edu.br
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
                "capsula de teletransporte":"Ir para a capsula"
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
            "titulo": "Bibloteca Telles",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "tobogã": "Entrar no tobogã",
                "capsula de teletransporte":"Ir para a capsula"
            }
        },
        "tobogã": {
            "titulo": "Prédio 2 do Insper",
            "descricao": "Você está no terceiro andar do prédio 2 do Insper",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "sala secreta": "Ir para a sala secreta",
                "capsula de teletransporte":"Ir para a capsula",
                "sala secretíssima": "Você não sabe onde está se metendo..."
            }
        },
        "sala secreta": {
            "titulo": "Sala de entidades",
            "descricao": "Você está na mesa com os veteranos do D.A. Vários itens estão espalhados pela mesa.",
            "opcoes":{
                "inicio": "Voltar para o saguao de entrada",
                "biblioteca": "Ir para a biblioteca",
                "capsula de teletransporte":"Ir para a capsula"
            }
        },
        "sala secretíssima": {
            "titulo": "Sala do Marcos Lisboa",
            "descricao": "Você foi convocado para uma reunião com a Carol da Costa e o Marcos Lisboa",
            "opcoes":{
                    "inicio": "Voltar para o saguao de entrada",
                    "andar professor": "Ir para a sala do Toshi",
                    "biblioteca": "Vá ler uns livros na biblioteca Telles",
                    "tobogã": "Entrar no tobogã",
                    "sala secreta": "Ir para a sala de entidades",
                    "capsula de teletransporte":"Ir para a capsula"
            }
        },
        "capsula de teletransporte":{
            "titulo":"Sala de transporte magico",
            "descricao":"Bem vindo à capsula de teletransporte!",
            "opcoes":{
                    "inicio": "Voltar para o saguao de entrada",
                    "andar professor": "Ir para a sala do Toshi",
                    "biblioteca": "Vá ler uns livros na biblioteca Telles",
                    "tobogã": "Entrar no tobogã",
                    "sala secreta": "Ir para a sala de entidades"
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
    x=1
    itens = []
    pontos_a={"hit points": 10, "pontos de ataque": 2,"pontos de defesa": 2}
    pontos_b={"hit points": 4, "pontos de ataque": 1,"pontos de defesa":1}
    objetos = ["Ingresso para festa Madrelisa","Motor de carro","Panfleto da nova campanha do GAS"]
    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print ()
        print ()
        print (cenario_atual['titulo'])
        print ("-"*len(cenario_atual['titulo']))
        print (cenario_atual['descricao'])
        print ()
        
        opcoes = cenario_atual ["opcoes"]
        if len(cenario_atual['opcoes']) == 0:
            print ()
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print ()
            print ("Escolha sua opção: ")
            print ()
            for k,v in cenario_atual['opcoes'].items():
                print ("{0} - {1}".format(k,v))
            print ()
            escolha = input('Qual é a sua escolha? ')
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
                opcoes = cenario_atual ["opcoes"]
                cenario_atual = cenarios [nome_cenario_atual]
                if escolha == "sala secreta":
                    x += 1 # Importar o código do monstrinho com randint 
                    print ()
                    print (cenario_atual["titulo"])
                    print ("-"*len(cenario_atual["titulo"]))
                    print (cenario_atual["descricao"])
                    print ()
                    print ("Bem vindo à sala secreta...")
                    print ()
                    print ("A sala de entidades te recebe de braços abertos! Cada entidade te oferece um objeto." )
                    print ()
                    print ("Os objetos que o GAS, o D.A e o Baja se propuseram a doar a você são: {0}".format(objetos))
                    dec = input ("Você deseja pegar algum objeto? (sim para pegar): ")
                    while dec == "sim":
                        print ()
                        obj = input ("Qual deles você quer??")
                        itens.append (obj)
                        print ("Objeto adicionado à sua mochila!")
                        dec = input ("Você deseja pegar mais algum objeto? (sim para pegar): ")
                        nome_cenario_atual = "sala secreta"
                            
                if escolha == 'capsula de teletransporte': 
                    print ()
                    print ()
                    print('Você poderá ir para onde quiser, desde que lembre o nome do lugar de cor!')
                    print ()
                    print('Você quer entrar nesta capsula?')
                    print ()
                    print('Caso você digite o nome do lugar errado você morrerá!')
                    print ()
                    print('Digite s para continuar e n para voltar ao início')
                    continuar=input('Você deseja continuar? ')
                    print ()
                    if continuar == 's':
                        s_transporte=input('Para onde você deseja ir? ')
                        if s_transporte == 'biblioteca':
                            nome_cenario_atual ='biblioteca'
                        elif s_transporte == 'tobogã':
                            nome_cenario_atual = 'tobogã'
                        elif s_transporte == 'sala secreta':
                            nome_cenario_atual = 'sala secreta'
                        elif s_transporte == 'sala secretíssima':
                            nome_cenario_atual = 'sala secretíssima'
                        elif s_transporte == 'professor':
                            nome_cenario_atual = 'professor'
                        elif s_transporte == 'andar professor':
                            nome_cenario_atual = 'andar professor'
                        else:
                            game_over=True
                    if continuar == 'n':
                        nome_cenario_atual=='inicio'
        
                if escolha =='tobogã':
                    print (cenario_atual['titulo'])
                    print ("-"*len(cenario_atual['titulo']))
                    print (cenario_atual['descricao'])
                    from random import randint
                    y=randint(1,2)
                    contador=1
                    if y==1:
                        print ("Você encontrou um veterano que esta bloqueando a sua passagem pelo tobogã!")
                        print ("Você tem 5 tentativas para acertar um número de 1 a 20 e assim desestabilizar o veterano.")
                        n = randint(1,20)
                        b=int(input("Digite um valor entre 1 e 20: "))
                        while b<1 or b>20:
                            print("Valor invalido")
                            b=int(input("Digite um valor entre 1 e 20: "))
                        while b!= n and contador<5:
                            contador+=1
                            if b<n:
                                print("Muito baixo")
                            elif b>n:
                                print("Muito alto")
                            b=int(input("Digite um valor entre 1 e 20: "))
                            while b<1 or b>20:
                                print("Valor invalido")
                                b=int(input("Digite um valor entre 1 e 20: "))
                        if contador == 6:
                            print("Que pena, o veterano ficou consciente e te devorou!")
                            game_over = True
                        elif b==n:
                            print("Você acertou em {0} tentativas. Agora voce podera passar pelo tobogã".format(contador))
                if escolha == "biblioteca":
                    x += 1  # Importar o código do monstrinho com randint 
                    print (cenario_atual['titulo'])
                    print ("-"*len(cenario_atual['titulo']))
                    print (cenario_atual['descricao'])
                    xa=[0,0,0]
                    xb=[0,0,0]
                    from random import randint
                    x= randint(1, 2)
                    if x==1:
                        print('Você esta com os seus livros atrasados!')
                        print('Por este motivo, terá que lutar com a bibliotecária...')
                        print ('Você tem {0} pontos'.format(pontos_a))
                        print ('A bibliotecária tem {0} pontos'.format(pontos_b))
                        decisao=input('Voce deseja entrar nesta batalha?(s para sim) ')
                        if decisao == 's':
                            if pontos_a['hit points']>pontos_b['hit points']:
                                if pontos_a['pontos de ataque']>pontos_b['pontos de defesa']:
                                    print('Aeee!!! Você ganhou a batalha e tem  à um aumento de pontos de ataque! Pode continuar.')
                                    xa=[0,pontos_b['pontos de defesa']-1,0]
                                    xb=[0,-2,-1]
                                    
                                elif pontos_a['pontos de ataque']<pontos_b['pontos de defesa']:
                                    print('VOCE PERDEUUUUUUUU! Infelizmente perdeu tambem um ponto de ataque...')
                                    xa=[0,-1,0]
                                elif pontos_a['pontos de ataque']==pontos_b['pontos de defesa']:
                                    print('Voce empatou...')
                            elif pontos_a['hit points']==pontos_b['hit points']:
                                print('Que sorte... vocês empataram. Pode prosseguir, voce voltara para o inicio.')
                        else:
                            print('Tá com medinho????')
                            print('Você voltará para o início')
                            nome_cenario_atual="inicio"
                        pontos_a["hit points"]+=xa[0]
                        pontos_a["pontos de ataque"]+=xa[1]
                        pontos_a["pontos de defesa"]+=xa[2]
                        pontos_b["hit points"]+=xb[0]
                        pontos_b["pontos de ataque"]+=xb[1]
                        pontos_b["pontos de defesa"]+=xb[2]
                elif escolha == "andar professor": 
                    if "Ingresso para festa Madrelisa" and "Motor de carro" in itens:
                        print ()
                        print ("Se você chegou aqui é porque tem o necessário.")
                        nome_cenario_atual = "andar professor"
                        cenario_atual = cenarios[nome_cenario_atual]
                        opcoes = cenario_atual ["opcoes"]
                    else:
                        print ("Você ainda não tem o que é necessário para entrar no andar do professor")
                        print ("Você retornará ao início e poderá refletir sobre como entrar na sala...")
                        nome_cenario_atual = "inicio"
                if escolha == "professor": 
                    nome_cenario_atual = "professor"
                    cenario_atual = cenarios[nome_cenario_atual]
                    opcoes = cenario_atual ["opcoes"]
                if escolha == "sala secretíssima":
                    print ("Sala do Marcos Lisboa")
                    t = "-"*len("Sala do Marcos Lisboa")
                    print (t)
                    print ()
                    print ("Você foi convocado para uma reunião com a Carol da Costa e o Marcos Lisboa.")
                    print ()
                    print ("Aqui o seu desejo se torna realidade (dentro do possível)")
                    print ("Você pode receber hit points, pontos de ataque ou pontos de defesa. Basta digitar o que desejas e terás.")
                    print ("Porém tome cuidado! Qualquer erro ortográfico e já era pra você.")
                    a = input("O que você deseja? ")    
                    if a == "hit points":
                        pontos_a["hit points"] += 3
                        print ("Você ganhou 3 hit points!")
                    if a == "pontos de defesa":
                        pontos_a["pontos de defesa"] += 2
                        print ("Você ganhou 2 pontos de defesa!")
                    if a == "pontos de ataque":
                        pontos_a["pontos de defesa"] += 2
                        print ("Você ganhou 2 pontos de ataque!")
                    else:
                        game_over = True
                

                        
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")

# Programa principal.
if __name__ == "__main__":
    main()
