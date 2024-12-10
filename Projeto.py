# 13.Gerar gráfico de barra com quantidade de participantes dos
# eventos

# 14.Criar uma lista de usuários proibidos de serem adicionados em
# eventos
#   o Ao inserir um participante no evento, verificar se o nome dele
#   não está nesta lista

# 15. Funcionalidade Extra (use a criatividade de verdade)

def loginVerificacao(emailInformado, senhaInformada):
    if (emailInformado == email and senhaInformada == senha):
        return True

    return False


import funcoes
import uuid
import time

usuarios = {'admin@admin.com': {'senha': "admin", 'nome': "Admin", 'eventosDoUser': []}}
eventos = {'82665c00-259d-4930-9f26-166760627dae': {'nome': "Evento teste", 'descricao': "Evento para testes",
                                                    'data': "12/12/12",
                                                    'local': "Local-UF", 'valor': 10, 'emailDono': "admin@admin.com",
                                                    'qtdParticipantes': 0, 'valorArrecadado': 0,
                                                    'regras': ["Proibida a entrada calçando sandálias",
                                                               "Proibido fumar no abiente"]}
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
                    funcoes.listarEventos(eventos)
                    participarEvento = str(input("Deseja participar de algum evento? (s/n): "))
                    if (participarEvento in concorda):
                        nomeEventoAParticipar = str(
                            input("Insira corretamente o nome do evento que deseja participar: "))
                        print("--------------------------------------------------")

                        if (funcoes.encontrarEventoPorNome(eventos, nomeEventoAParticipar)):
                            print("Evento encontrado!")
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

                        id = str(uuid.uuid4)

                        eventos[id] = {'nome': nomeEvento, 'descricao': descricaoEvento, 'data': dataEvento,
                                       'local': localEvento, 'valor': valorInscricaoEvento, 'emailDono': email,
                                       'qtdParticipantes': numeroDeParticipantes,
                                       'valorArrecadado': valorTotalArrecadado,
                                       'regras': regrasDoEvento}
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

                                for eventoBuscaNome in eventos:
                                    if (eventoBuscaNome[0] == nomeEventoABuscar):
                                        encontrado = True
                                        eventosEncontradosNome.append(eventoBuscaNome)

                                if (encontrado):
                                    print("Evento encontrado!")
                                    funcoes.listarEventos(eventosEncontradosNome)
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
                                    if (evento[4] >= precoMin and evento[4] <= precoMax):
                                        encontrado = True
                                        eventosEncontradosPreco.append(evento)

                                if (encontrado):
                                    print("Esses foram os eventos encontrados:")
                                    funcoes.listarEventos(eventosEncontradosPreco)
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

                                funcoes.listarEventos(eventosDoUsuario)

                                opcaoMenuMeusEventosCriados = int(input("O que deseja fazer com seus eventos?"
                                                                        "\n1 - Remover evento"
                                                                        "\n2 - Listar participantes do evento"
                                                                        "\n3 - Adicionar participante ao evento"
                                                                        "\n4 - Voltar ao menu anterior"
                                                                        "\nEscolha sua opção: "))

                                if (opcaoMenuMeusEventosCriados == 4):
                                    break

                                elif (opcaoMenuMeusEventosCriados == 1):
                                    while (True):
                                        logadoRemover = False

                                        print("--------------------------------------------------")
                                        nomeEventoRemover = str(input("Insira o nome do evento que deseja remover: "))

                                        if (funcoes.encontrarEventoPorNome(eventosDoUsuario, nomeEventoRemover)):
                                            certezaRemover = str(
                                                input("Tem cereteza que deseja remover esse evento? (s/n): "))
                                            if (certezaRemover in concorda):
                                                print("--------------------------------------------------")
                                                print("Faça login para remover o evento.")
                                                print("--------------------------------------------------")
                                                emailLoginRemover = str(input("Insira seu email: "))
                                                senhaLoginRemover = str(input("Insira sua senha: "))
                                                if (loginVerificacao(emailLoginRemover, senhaLoginRemover)):
                                                    statusRem = False
                                                    for evento in eventos:
                                                        if (eventos[evento]['nome'] == nomeEventoRemover):
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
                                    nomeEventoAInserirParticipante = str(
                                        input("Insira o nome do evento que deseja inserir o participante: "))

                                    emailUsuarioAInserirNoEvento = str(
                                        input("Insira o email do usuário que deseja inserir no evento: "))

                                    if ((funcoes.encontrarUserPorEmail(usuarios, emailUsuarioAInserirNoEvento)) and (
                                    funcoes.encontrarEventoPorNome(eventos, nomeEventoAInserirParticipante))):

                                        funcoes.inserirParticipante(usuarios, eventos, emailUsuarioAInserirNoEvento,
                                                                    nomeEventoAInserirParticipante)

                                        print("--------------------------------------------------")
                                        print("Você inscreveu um novo participante no evento!")
                                        print("--------------------------------------------------")

                                    else:
                                        print("Esse usuário ou evento não existem.")
                                else:
                                    print("Opção inválida.")



                        elif (opcaoMenuMeusEventos == 2):
                            while (True):
                                eventosQueOUsuarioParticipa = []

                                for user in usuarios:
                                    if (user == email):
                                        for evento in usuarios[user]['eventosDoUser']:
                                            eventosQueOUsuarioParticipa.append(evento)

                                if (len(eventosQueOUsuarioParticipa) == 0):
                                    print("Você não participa de nenhum evento.")
                                    break

                                print("--------------------------------------------------")
                                print(f"Olá, {nomeUserAtual}!\nAqui estão os eventos que você está participando: ")
                                print(" ")

                                for evento in eventosQueOUsuarioParticipa:
                                    print(f'Evento: {evento}', end=' | \n')

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