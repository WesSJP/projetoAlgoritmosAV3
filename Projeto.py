# 15. Funcionalidade Extra (use a criatividade de verdade)
################################################################
import funcoes
import uuid
import time
import matplotlib.pyplot as grafico

usuarios = {'admin@admin.com': {'senha': "admin", 'nome': "Admin", 'eventosDoUser': ["Evento teste", "Evento legal"]},
            'wesley@gmail.com': {'senha': "123", 'nome': "Wesley", 'eventosDoUser': ["Evento legal"]}}
eventos = {'82665c00-259d-4930-9f26-166760627dae': {'nome': "Evento teste", 'descricao': "Evento para testes",
                                                    'data': "12/12/12",
                                                    'local': "Local-UF", 'valor': 10, 'emailDono': "admin@admin.com",
                                                    'qtdParticipantes': 1, 'valorArrecadado': 0,
                                                    'regras': ["Proibida a entrada calçando sandálias",
                                                               "Proibido fumar no abiente"],
                                                    'usuariosBanidos': ['wesley@gmail.com']},
           'f47ac10b-58cc-4372-a567-0e02b2c3d479': {'nome': "Evento legal", 'descricao': "Evento bastante divertido",
                                                    'data': "12/12/12",
                                                    'local': "SJP-PB", 'valor': 20, 'emailDono': "wesley@gmail.com",
                                                    'qtdParticipantes': 2, 'valorArrecadado': 0,
                                                    'regras': ["Proibido entrar vestido de verde"],
                                                    'usuariosBanidos': []}
           }

concorda = ["s", "sim", "sin", "ss", "yes", "y"]

while (True):
    logado = False
    statusCadastro = False
    print("--------------- Seja bem vindo ao Wevents! ---------------")

    print("\nCadastre-se ou faça login para continuar!")

    opcaoMenuPrincipal = int(input("\n1 - Cadastro de usuário\n2 - Login\n3 - Encerrar programa\nEscolha uma opção: "))

    if (opcaoMenuPrincipal == 1):
        while (True):
            if (statusCadastro):
                break
            else:
                nome = str(input("Insira seu nome: "))
                email = str(input("Insira o email a ser cadastrado: ")).lower()

                if (funcoes.encontrarUserPorEmail(usuarios, email)):
                    print("\nUsuário já foi cadastrado!\n")
                else:
                    while (True):
                        if (funcoes.verificarEmail(email)):
                            primeiraSenha = str(
                                input("Digite a senha que deseja cadastrar (máxmimo de 8 caracteres): ")).lower()
                            senhaConfirmacao = str(input("Repita sua senha: ")).lower()
                            if (funcoes.verificarSenha(primeiraSenha, senhaConfirmacao)):
                                senha = senhaConfirmacao
                                usuarios[email] = {'senha': senha, 'nome': nome, 'eventosDoUser': []}
                                print("Usuário cadastrado!")
                                statusCadastro = True
                                break

                        else:
                            print('\nPor favor, insira um email válido.\nEx: email@dominiodoemail.com')
                            statusCadastro = False
                            break

    elif (opcaoMenuPrincipal == 2):
        email = str(input("Digite seu email: "))
        senha = str(input("Digite sua senha: "))
        if (funcoes.fazerLogin(email, senha, usuarios)):
            print("LOGIN BEM SUCEDIDO")
            logado = True
        else:
            print("-------------------------\nEmail ou senha incorretos.\n-------------------------")
            logado = False

        if (logado):
            for emailUser in usuarios:
                if (emailUser == email):
                    nomeUserAtual = usuarios[emailUser]['nome']

            print(f"-------------------------\nSeja bem vindo(a), {nomeUserAtual}!\n-------------------------")

            while (True):
                print(f"-------------------------\nMenu do Usuário\n-------------------------")
                opcaoPosLogin = int(input(
                    "\n1 - Cadastrar evento\n2 - Buscar evento\n3 - Listar eventos\n4 - Meus eventos\n5 - Retornar ao menu principal\nEscolha uma opção: "))

                if (opcaoPosLogin == 5):
                    break

                elif (opcaoPosLogin == 3):
                    print("-------------------------\nListar eventos\n-------------------------")
                    print("Eis aqui a quantidade de participantes por evento")

                    funcoes.gerarGrafico(eventos, grafico)

                    funcoes.listarEventos(eventos)
                    participarEvento = str(input("Deseja participar de algum evento? (s/n): "))
                    if (participarEvento in concorda):
                        nomeEventoAParticipar = str(
                            input("Insira corretamente o nome do evento que deseja participar: "))
                        print("--------------------------------------------------")

                        if (funcoes.encontrarEventoPorNome(eventos, nomeEventoAParticipar)):
                            print("Evento encontrado!")
                            if (not (funcoes.verificarBanimento(eventos, nomeEventoAParticipar, email))):
                                print("--------------------------------------------------")
                                print(
                                    f"Para completar a insrição no evento '{nomeEventoAParticipar}', é necessário realizar o pagamento.")
                                print("--------------------------------------------------")

                                confirmarPagamento = str(input("Deseja confirmar o pagamento? (s/n): "))
                                if (confirmarPagamento in concorda):
                                    funcoes.inserirParticipante(usuarios, eventos, email, nomeEventoAParticipar)

                                    print("--------------------------------------------------")
                                    print("Pagamento confirmado!\nVocê está inscrito no evento.")
                                    print("--------------------------------------------------")
                                else:
                                    print("Pagamento não confirmado, você perdeu essa reserva.\nReserve novamente.")
                            else:
                                print("Você está banido desse evento.")
                        else:
                            print("Não existe nenhum evento com esse nome.")


                elif (opcaoPosLogin == 1):
                    while (True):
                        print("-------------------------\nCadastrar evento\n-------------------------")

                        while (True):
                            nomeEvento = str(input("Insira o nome do evento: "))
                            if (len(nomeEvento) >= 3):
                                break
                            else:
                                print("\nNome muito curto, por favor, insira novamente.\n")

                        while (True):
                            descricaoEvento = str(input("Insira a descrição do evento: "))
                            if (len(descricaoEvento) >= 10):
                                break
                            else:
                                print("\nDescrição muito curta, por favor, insira novamente.\n")

                        dataEvento = str(input("Insira a data do evento (dd/mm/aa): "))

                        while (True):
                            localEvento = str(input("Insira o local do evento: "))
                            if (len(localEvento) >= 3):
                                break
                            else:
                                print("\nNome do local muito curto, por favor, insira novamente.\n")

                        while (True):
                            valorInscricaoEvento = float(input("Insira o valor de inscrição do evento: "))
                            if (valorInscricaoEvento >= 0):
                                break
                            else:
                                print("O valor de inscrição deve ser positivo.")

                        numeroDeParticipantes = 0

                        valorTotalArrecadado = 0

                        print("--------------------------------------------------")
                        print("Insira as regras do evento")
                        print("--------------------------------------------------")

                        regrasDoEvento = []
                        while (True):
                            regraParaOEvento = str(input("Regra (insira 0 para encerrar a inserção de regras): "))
                            if (regraParaOEvento == '0'):
                                break

                            regrasDoEvento.append(regraParaOEvento)

                        id = str(uuid.uuid4())

                        eventos[id] = {'nome': nomeEvento, 'descricao': descricaoEvento, 'data': dataEvento,
                                       'local': localEvento, 'valor': valorInscricaoEvento, 'emailDono': email,
                                       'qtdParticipantes': numeroDeParticipantes,
                                       'valorArrecadado': valorTotalArrecadado,
                                       'regras': regrasDoEvento, 'usuariosBanidos': []}
                        print("O evento foi cadastrado com sucesso!")
                        break

                elif (opcaoPosLogin == 2):
                    while (True):
                        encontrado = False
                        print("-------------------------\nBuscar evento\n-------------------------")

                        opcaoMenuBusca = int(input(
                            "Deseja realizar a busca por:\n1 - Nome do evento\n2 - Preço do ingresso\n3 - Retornar ao menu anterior\nEscolha uma opção: "))

                        if (opcaoMenuBusca) == 3:
                            break

                        elif (opcaoMenuBusca) == 1:
                            while (True):
                                eventosEncontradosNome = []
                                nomeEventoABuscar = str(input("Insira o nome do evento que deseja buscar: "))

                                funcoes.encontrarEventoPorNome(eventos, nomeEventoABuscar, eventosEncontradosNome)

                                if (funcoes.encontrarEventoPorNome(eventos, nomeEventoABuscar)):
                                    print("Evento encontrado!")
                                    funcoes.listarNomes(eventosEncontradosNome, "Evento")
                                    break
                                else:
                                    print("Não foi encontrado nenhum evento com esse nome.")
                                    break

                        elif (opcaoMenuBusca) == 2:
                            while (True):
                                eventosEncontradosPreco = []
                                while (True):
                                    precoMin = float(input("Insira o preço MÍNIMO que deseja buscar: "))
                                    if (precoMin < 0):
                                        print("Por favor, insira um valor positivo.")
                                    else:
                                        break
                                while (True):
                                    precoMax = float(input("Insira o preço MÁXIMO que deseja buscar: "))
                                    if (precoMax < 0 or precoMax < precoMin):
                                        print("Por favor, insira um valor positivo ou maior que o preço mínimo.")
                                    else:
                                        break

                                for evento in eventos:
                                    if (eventos[evento]['valor'] >= precoMin and eventos[evento]['valor'] <= precoMax):
                                        encontrado = True
                                        eventosEncontradosPreco.append(eventos[evento]['nome'])

                                if (encontrado):
                                    print("Esses foram os eventos encontrados:")
                                    funcoes.listarNomes(eventosEncontradosPreco, "Evento")
                                    break
                                else:
                                    print("Não foi encontrado nenhum evento nesse intervalo de preço.")
                                    break

                        else:
                            print("Opção inválida.")

                elif (opcaoPosLogin == 4):
                    while (True):
                        print("-------------------------\nMeus eventos\n-------------------------")

                        opcaoMenuMeusEventos = int(input(
                            "1 - Eventos que criei\n2 - Eventos que participo\n3 - Voltar ao menu anterior\nEscolha uma opção: "))

                        if (opcaoMenuMeusEventos == 1):
                            while (True):
                                eventosDoUsuario = {}

                                for eventoId in eventos:
                                    if (eventos[eventoId]['emailDono'] == email):
                                        eventosDoUsuario[eventoId] = eventos[eventoId]

                                if (len(eventosDoUsuario) == 0):
                                    print("\nVocê não possui nenhum evento.\n")
                                    break

                                print("--------------------------------------------------")
                                print(f"Olá, {nomeUserAtual}!\nAqui estão os eventos que você criou: ")
                                print(" ")

                                print("Gráfico com a quantidade de participantes dos seus eventos")
                                funcoes.gerarGrafico(eventosDoUsuario, grafico)
                                funcoes.listarEventos(eventosDoUsuario, True)

                                opcaoMenuMeusEventosCriados = int(input("O que deseja fazer com seus eventos?"
                                                                        "\n1 - Remover evento"
                                                                        "\n2 - Listar participantes do evento"
                                                                        "\n3 - Adicionar participante ao evento"
                                                                        "\n4 - Banir participante do evento"
                                                                        "\n5 - Voltar ao menu anterior"
                                                                        "\nEscolha sua opção: "))

                                if (opcaoMenuMeusEventosCriados == 5):
                                    break

                                elif (opcaoMenuMeusEventosCriados == 1):
                                    while (True):
                                        logadoRemover = False

                                        print("--------------------------------------------------")
                                        idEventoRemover = str(input("Insira o ID do evento que deseja remover: "))

                                        if (funcoes.encontrarEventoPorId(eventosDoUsuario, idEventoRemover)):
                                            certezaRemover = str(
                                                input("Tem cereteza que deseja remover esse evento? (s/n): "))
                                            if (certezaRemover in concorda):
                                                print("--------------------------------------------------")
                                                print("Faça login para remover o evento.")
                                                print("--------------------------------------------------")
                                                emailLoginRemover = str(input("Insira seu email: "))
                                                senhaLoginRemover = str(input("Insira sua senha: "))
                                                if (funcoes.loginVerificacao(usuarios, email, emailLoginRemover,
                                                                             senhaLoginRemover)):
                                                    statusRem = False
                                                    for evento in eventos:
                                                        if (evento == idEventoRemover):
                                                            statusRem = True

                                                    if (statusRem):
                                                        del eventos[evento]
                                                        print("Evento removido!")
                                                    break
                                                else:
                                                    print("Email ou senha inválidos!")
                                                    print("Remoção cancelada.")
                                                    break

                                            else:
                                                print("Remoção cancelada.")
                                                break

                                        else:
                                            print("Você não possui nenhum evento com esse nome.")
                                            break

                                elif (opcaoMenuMeusEventosCriados == 2):
                                    participantesDoEventoArquivo = open('participantesDoEvento.txt', 'w')
                                    nomeEventoAListarParticipantes = str(
                                        input("Insira o nome do evento do qual quer a lista de participantes: "))

                                    if (
                                    funcoes.encontrarEventoPorNome(eventosDoUsuario, nomeEventoAListarParticipantes)):
                                        participantesDoEventoArquivo = open('participantesDoEvento.txt', 'a')
                                        participantesDoEventoArquivo.write(
                                            f'---------------------------- PARTICIPANTES DO {nomeEventoAListarParticipantes.upper()} ----------------------------\n')
                                        for user in usuarios:
                                            for nomeEvento in usuarios[user]['eventosDoUser']:
                                                if (nomeEvento == nomeEventoAListarParticipantes):
                                                    print(f"Participante: {usuarios[user]['nome']}", end=" |\n",
                                                          file=participantesDoEventoArquivo)
                                                    time.sleep(1.5)
                                    else:
                                        print("Você não possui nenhum evento com esse nome.")

                                    time.sleep(1.5)

                                elif (opcaoMenuMeusEventosCriados == 3):
                                    idEventoAInserirParticipante = str(
                                        input("Insira o ID do evento que deseja inserir o participante: "))

                                    emailUsuarioAInserirNoEvento = str(
                                        input("Insira o email do usuário que deseja inserir no evento: "))

                                    if ((funcoes.encontrarUserPorEmail(usuarios, emailUsuarioAInserirNoEvento)) and (
                                    funcoes.encontrarEventoPorId(eventos, idEventoAInserirParticipante))):

                                        if (not (funcoes.verificarBanimento(eventos,
                                                                            eventos[idEventoAInserirParticipante][
                                                                                'nome'],
                                                                            emailUsuarioAInserirNoEvento))):
                                            funcoes.inserirParticipante(usuarios, eventos, emailUsuarioAInserirNoEvento,
                                                                        eventos[idEventoAInserirParticipante]['nome'])

                                            print("--------------------------------------------------")
                                            print("Você inscreveu um novo participante no evento!")
                                            print("--------------------------------------------------")
                                        else:
                                            print("Esse usuário está banido do evento.")

                                    else:
                                        print("Esse usuário ou evento não existem.")

                                elif (opcaoMenuMeusEventosCriados == 4):
                                    emailUserASerBanido = str(input("Insira o email do usuário a ser banido: "))
                                    if (funcoes.encontrarUserPorEmail(usuarios, emailUserASerBanido)):
                                        idEventoABanirAlguem = str(
                                            input("Insira o ID do evento do qual irá banir o usuário: "))
                                        if (funcoes.encontrarEventoPorId(eventos, idEventoABanirAlguem)):
                                            eventos[idEventoABanirAlguem]['usuariosBanidos'].append(emailUserASerBanido)
                                            time.sleep(1)
                                        else:
                                            print("Esse evento não existe.")
                                    else:
                                        print("Esse usuário não existe.")
                                else:
                                    print("Opção inválida.")



                        elif (opcaoMenuMeusEventos == 2):
                            while (True):
                                eventosQueOUsuarioParticipa = []

                                if (funcoes.encontrarUserPorEmail(usuarios, email)):
                                    for evento in usuarios[user]['eventosDoUser']:
                                        eventosQueOUsuarioParticipa.append(evento)

                                if (len(eventosQueOUsuarioParticipa) == 0):
                                    print("Você não participa de nenhum evento.")
                                    break

                                print("--------------------------------------------------")
                                print(f"Olá, {nomeUserAtual}!\nAqui estão os eventos que você está participando: ")
                                print(" ")

                                funcoes.listarNomes(eventosQueOUsuarioParticipa, "Evento")

                                print("--------------------------------------------------")
                                desejaCancelarInscricao = str(
                                    input("Deseja cancelar a inscrição de algum evento? (s/n): "))

                                if (desejaCancelarInscricao in concorda):
                                    nomeEventoACancelarInscricao = str(input(
                                        "Insira corretamente o nome do evento no qual quer cancelar a inscrição: "))
                                    encontrado = False

                                    for evento in eventosQueOUsuarioParticipa:
                                        if (evento == nomeEventoACancelarInscricao):
                                            encontrado = True

                                    if (encontrado):
                                        certezaCancelarInscricao = str(
                                            input("Tem cereteza que deseja cancelar a inscrição do evento? (s/n): "))
                                        if (certezaCancelarInscricao in concorda):
                                            for indice in range(len(eventosQueOUsuarioParticipa)):
                                                if (eventosQueOUsuarioParticipa[
                                                    indice] == nomeEventoACancelarInscricao):
                                                    del usuarios[user]['eventosDoUser'][indice]
                                            print("--------------------------------------------------")
                                            print("Inscrição CANCELADA!")
                                            break

                                        else:
                                            print("Inscrição NÃO cancelada.")
                                            break

                                    else:
                                        print("Você não participa de nenhum evento com esse nome.")
                                        break

                                else:
                                    break

                        elif (opcaoMenuMeusEventos == 3):
                            break

                        else:
                            print("Opção inválida.")

                else:
                    print("Opção inválida.")

    elif (opcaoMenuPrincipal == 3):
        break

    else:
        print("Opção inválida!")