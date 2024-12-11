def verificarEmail(email):
    contadordeArroba = 0
    contadordePonto = 0
    if ('@' in email) and ('.com' in email):

        for caractere in email:
            if caractere == '@':
                contadordeArroba += 1
            if caractere == '.':
                contadordePonto += 1

        if (contadordeArroba == 1) and (contadordePonto == 1):
            return True
        else:
            return False


def verificarSenha(primeiraSenha, senhaConfirmacao):
    if (len(primeiraSenha) <= 8):
        if (senhaConfirmacao == primeiraSenha):
            return True
        else:
            print("As senhas diferem, insira novamente.")
            return False
    else:
        print("Senha muito longa, insira novamente.")
        return False


def verificarBanimento(eventos, nomeEvento, email):
    banido = False
    for evento in eventos:
        if ((eventos[evento]['nome'] == nomeEvento)):
            id = evento
            if (email in eventos[id]['usuariosBanidos']):
                banido = True

    return banido


def fazerLogin(email, senha, usuarios):
    for emailUser in usuarios:
        if (email == emailUser and senha == usuarios[emailUser]['senha']):
            return True

    return False


def loginVerificacao(usuarios, emailLogado, emailInformado, senhaInformada):
    if (emailInformado == emailLogado and senhaInformada == usuarios[emailLogado]['senha']):
        return True

    return False


def listarEventos(dicionario, dono=False):
    if (dono):
        for eventoId in dicionario:
            print(f'ID: {eventoId}', f'| Evento: {dicionario[eventoId]['nome']}',
                  f'| Descrição: {dicionario[eventoId]['descricao']}', f'| Data: {dicionario[eventoId]['data']}',
                  f'| Local: {dicionario[eventoId]['local']}', f'| Valor: R$ {dicionario[eventoId]['valor']:.2f} |',
                  '\nRegras do evento:', end='\n')
            for regra in dicionario[eventoId]['regras']:
                print(regra, end=' | \n')
    else:
        for eventoId in dicionario:
            print(f'Evento: {dicionario[eventoId]['nome']}', f'| Descrição: {dicionario[eventoId]['descricao']}',
                  f'| Data: {dicionario[eventoId]['data']}',
                  f'| Local: {dicionario[eventoId]['local']}', f'| Valor: R$ {dicionario[eventoId]['valor']:.2f} |',
                  '\nRegras do evento:', end='\n')
            for regra in dicionario[eventoId]['regras']:
                print(regra, end=' | \n')
    print("--------------------------------------------------")


def listarNomes(lista, oQueEstaListando):
    for evento in lista:
        print(f'{oQueEstaListando}: {evento}', end=' | \n')


def encontrarEventoPorNome(eventos, nomeEvento, lista=[]):
    encontrado = False
    for evento in eventos:
        if (eventos[evento]['nome'] == nomeEvento):
            lista.append(eventos[evento]['nome'])
            encontrado = True

    return encontrado


def encontrarEventoPorId(eventos, idEvento):
    encontrado = False
    for evento in eventos:
        if (evento == idEvento):
            encontrado = True

    return encontrado


def encontrarUserPorEmail(usuarios, email):
    userEncontrado = False
    for emailUser in usuarios:
        if (emailUser == email):
            userEncontrado = True

    return userEncontrado


def inserirParticipante(usuarios, eventos, email, nomeEvento):
    for user in usuarios:
        if (user == email):
            usuarios[user]['eventosDoUser'].append(nomeEvento)
            break

    for eventoId in eventos:
        if (eventos[eventoId]['nome'] == nomeEvento):
            eventos[eventoId]['qtdParticipantes'] += 1
            eventos[eventoId]['valorArrecadado'] += eventos[eventoId]['valor']


def gerarGrafico(eventos, grafico):
    nomesEventos = []
    quantidadeDeParticipantes = []

    for evento in eventos:
        nomesEventos.append(eventos[evento]['nome'])
        quantidadeDeParticipantes.append(eventos[evento]['qtdParticipantes'])

    grafico.bar(nomesEventos, quantidadeDeParticipantes, color="blue")
    grafico.yticks(quantidadeDeParticipantes)
    grafico.xlabel("Eventos")
    grafico.ylabel("Quantidade de participantes")
    grafico.title("Quantidade de participantes de cada evento")
    grafico.show()