import pandas as pd
import os
import numpy as np
from datetime import datetime
from calendar import isleap
from utils.constantes import data, INPUT_TABLE, MESES, RENAME_COLUMNS, REORDER_LIST, rename_itens, CURRENT_DATE, dif_date

def intervalo_datas(dt_prev):
    '''Retorna o primeiro e ultimo dia do dec referente a data passada'''

    # caso o mês seja fevereiro
    if dt_prev.month == 2:

        #A função isleap irá verificar se fevereiro está em um ano bissexto. Caso esteja, o mes terá 29 dias ou 28 dias.
        if isleap(dt_prev.year):
            max_day = 29
        else:
            max_day = 28

    #Os meses Abril, Junho, Setembro e Novembro são meses com 30 dias, logo o máximo será 30 dias.        
    elif dt_prev.month in {4, 6, 9, 11}:
        max_day = 30

    #O restante dos meses contêm 31 dias em seu total.
    else: 
        max_day = 31

    intervalo = [
        {'ini': 1, 'fim': 10},
        {'ini': 11, 'fim': 20},
        {'ini': 21, 'fim': max_day} #A condicional irá obter a quantidade máxima de dias que aquele mês possui.
    ]

    #retorna o intervalo do dec em que a data está.
    for dec in intervalo:
        if dt_prev.day <= dec['fim']:
            dt_prev_ini = pd.Timestamp(year=dt_prev.year, month=dt_prev.month, day=dec['ini'])
            print("Data Prevista inicial: ", dt_prev_ini)
            dt_prev_fim = pd.Timestamp(year=dt_prev.year, month=dt_prev.month, day=dec['fim'])
            print("Data Prevista final: ", dt_prev_fim)
            break

    return dt_prev_ini, dt_prev_fim

def folder(nome_pasta):
    '''Cria uma pasta com o nome especificado e navega até ela'''
    try:
        # Converte o nome da pasta em uma string, caso ainda não seja uma
        nome_pasta = str(nome_pasta)
        # Cria o caminho completo da pasta, concatenando o diretório atual com o nome da pasta
        dir_destino = os.path.join(os.getcwd(), nome_pasta)
        # Verifica se a pasta já existe, se não existir, cria a pasta
        if not os.path.exists(dir_destino):
            # Cria a pasta com o nome especificado
            os.makedirs(dir_destino)
        # Navega para a pasta criada
        os.chdir(dir_destino)
        # Exibe mensagem de sucesso
        print(f"Foi para a pasta {nome_pasta}")
    except OSError as e:
        # Exibe mensagem de erro caso não seja possível criar a pasta
        print(f"Não foi possível criar a pasta {nome_pasta}: {e}")

def create_folder(data_prevista, dt_prev_fim, nm_site, folder_prints="prints"):
    '''Cria as pastas necessárias para armazenar os arquivos da coleta e saída'''
    folder('data_output')
    folder(nm_site)
    # Cria a pasta coleta_n, onde n é o ano da data prevista
    year_folder = f'coleta_{data_prevista.year}          '
    folder(year_folder)

    # Cria a pasta coleta_mes, onde mes é o mês correspondente à data prevista
    month_folder = f'coleta_{MESES.get(str(data_prevista.month))}'
    folder(month_folder)

    # Cria a pasta do decendio correspondente à data prevista
    decendio = (dt_prev_fim.day) // 10 
    folder(f"coleta_{decendio}_dec")

    # Cria a pasta saida_ano_mes_dia correspondente à data prevista
    folder(f"saida_{data_prevista.strftime('%Y_%m_%d')}")

    try:
        os.mkdir(folder_prints)
    except OSError as e:
        # Exibe mensagem de erro caso não seja possível criar a pasta
        print(f"Não foi possível criar a pasta {folder_prints}: {e}")

def read_table(cod_informante) -> pd.read_csv: #dt_prev_fim, dt_prev_ini
    '''Função para ler a tabela encomenda em csv.'''

    #listando todo os arquivos no diretório input_table
    ultima_encomenda = os.listdir(INPUT_TABLE)

    #pegando a última encomenda dentro do diretório input_table que começa com "encomenda" e termina com ".xls"
    ultima_encomenda = [i for i in ultima_encomenda if i.startswith(
        'encomenda') if i.endswith('.xlsx')][-1]
    
    #lendo o arquivo mais recente dentro do diretório input_table com seus devidos argumentos
    tabela = pd.read_excel(INPUT_TABLE + ultima_encomenda, dtype=str)
    
    
    #convertendo a coluna data_prevista para o formato de horas usando o to_datetime
    tabela['DATA_PREVISTA'] = pd.to_datetime(tabela['DATA_PREVISTA'], format='%d/%m/%y', errors='coerce')
    # #filtrando para o intervalo de data da função intervalo_datas()
    # tabela = tabela[(tabela['DATA_PREVISTA'] <= dt_prev_fim) & (tabela['DATA_PREVISTA'] > dt_prev_ini)]

    # #convertendo de volta a coluna data_prevista para o padrão str
    # tabela['DATA_PREVISTA'] = tabela['DATA_PREVISTA'].dt.strftime('%d/%m/%Y')

    #filtrando pelo código do informante
    tabela = tabela[tabela.CD_INFORM == cod_informante]
    print(tabela)
    return tabela

def create_carga(encomenda, nm_site, cod_informante) -> pd.DataFrame:
    #dt_prev_ini, dt_prev_fim = intervalo_datas(dt_prev)
    encomenda["data_coleta"] = data.strftime('%d/%m/%Y')
    encomenda = encomenda.rename(columns=RENAME_COLUMNS)
    encomenda = encomenda.reindex(columns=REORDER_LIST)
    encomenda = encomenda.fillna("")

    

    print('encomenda', encomenda.shape)
    carga = encomenda[REORDER_LIST].copy()
    print('carga', carga.shape)
  
    carga['Pais_Retirada'] = encomenda['Pais']
    carga['Regiao_Retirada'] = encomenda['Região']
    carga['Estado_Retirada'] = encomenda['Estado']
    carga['Municipio_Retirada'] = encomenda['Municipio']
    #carga['Data Prevista'] = f'{dt_prev_fim.day}/{dt_prev_fim.month}/{dt_prev_fim.year}'
    carga['Justificativa Livre'] = np.where(carga['Valor do Preço'].isna(), 'ITEM EM FALTA NO SITE/BOLETIM/TABELA', 'PREÇO CONFORME SITE/BOLETIM/TABELA')
    carga['Moeda'] = 'R$'
    carga['Valor do Preço'] = carga['Valor do Preço'].apply(lambda x: x.replace('.', ','))
    carga['Frete Incluso'] = 'N'
    carga['Data Prevista'] = encomenda['Data Prevista']
    carga["FT"] = np.where(carga["Valor do Preço"] == "", "S", "")
    file_name = f"carga_{nm_site}_BP{cod_informante}_{dif_date}.xls"
    carga.to_excel(file_name, sheet_name='Carga BP', index=False)