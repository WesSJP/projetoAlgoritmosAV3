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


def fazerLogin(email, senha, usuarios):
    for emailUser in usuarios:
        if (email == emailUser and senha == usuarios[emailUser]['senha']):
            return True

    return False


def listarEventos(dicionario):
    for eventoId in dicionario:
        print(f'Evento: {dicionario[eventoId]['nome']}', f'| Descrição: {dicionario[eventoId]['descricao']}',
              f'| Data: {dicionario[eventoId]['data']}',
              f'| Local: {dicionario[eventoId]['local']}', f'| Valor: R$ {dicionario[eventoId]['valor']:.2f} |',
              '\nRegras do evento:', end='\n')
        for regra in dicionario[eventoId]['regras']:
            print(regra, end=' | \n')
    print("--------------------------------------------------")


def encontrarEventoPorNome(eventos, nomeEvento):
    encontrado = False
    for evento in eventos:
        if (eventos[evento]['nome'] == nomeEvento):
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