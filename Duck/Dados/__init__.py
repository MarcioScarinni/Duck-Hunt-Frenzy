def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArq(nome):
    arquivo = open(f'{nome}', 'wt+')
    arquivo.close()


def lerArq(nome):
    try:
        arquivo = open(f'{nome}', 'rt')
    except FileNotFoundError:
        #print(f'Arquivo {arquivo}não encontrado.')
        pass
    else:
        for i in arquivo:
            dados = i.split(';')
            dados[1] = dados[1].replace('\n', '')
            return int(dados[1])
        arquivo.close()



def criaNovo(arq, nome='Desconhecido', pontos= 0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            arquivo.write(f'{nome};{pontos}\n')
        except:
            print('Erro ao gravar arquivo!')
        else:
           pass
        finally:
            arquivo.close()