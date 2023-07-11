from datetime import date, timedelta
data = date.today() + timedelta(0)


#local da minha encomenda
INPUT_TABLE = "D:\\VSCODE_notebook\\1_Robos\\Script_Generico\\encomenda_nova\\"

CURRENT_DATE = '{}-{}-{}'.format(data.day, data.month, data.year)
dif_date = data.strftime("%d_%m_%Y")
print(dif_date)
#elemento da box
ELEMENT_BOX = '.summary.entry-summary'
PRICE_ELEMENT = '.price'

MESES = {'1':'janeiro','2':'fevereiro','3':'marco','4':'abril','5':'maio','6':'junho',
         '7':'julho','8':'agosto','9':'setembro','10':'outubro','11':'novembro','12':'dezembro'}

ceps = {'AC': '69914480', 'AL': '57060530', 'AM': '69010000', 'AP': '68925147', 'PA': '66050000', 'RN': '59064902',
           'RO': '76824246',
           'RR': '69316400', 'TO': '77024028', 'DF': '70830020', 'GO': '74933130', 'MS': '79044490', 'MT': '78120665',
           'BA': '40015030', 'CE': '60720095',
           'MA': '65015330', 'PB': '58020671', 'PE': '52010000', 'PI': '64016380', 'SE': '49015350', 'ES': '29010930',
           'MG': '30140120',
           'RJ': '22231000', 'SP': '01310000', 'PR': '80730420', 'RS': '90560005', 'SC': '88010001'}

RENAME_COLUMNS = {
    "CD_PERIOD": "Periodicidade",
    "DATA_PREVISTA": "Data Prevista",
    "CD_COLETOR": "Coletor Padrão",
    "CD_INFORM": "Código do Informante",
    "CD_INSUMO": "Código do Insumo",
    "NM_INSUMO": "Nome Insumo",
    "DS_INSUMO": "Característica Insumo",
    "CD_MARCFAB": "Marca Insumo",
    "CD_MEDIDA": "Unidade Medida Insumo",
    "QT_MED_INSUMO": "Quantidade Insumo",
    "CD_EMB": "Embalagem Insumo",
    "NR_SEQ_INSINF": "Insumo Informado",
    "CD_TPPRECO": "Tipo de Preço",
    "CD_COTACAO": "Cotação",
    "DS_SINO_NOME_INS_INSINF": "Sinônimo Insumo Informado",
    "S_OBS_INSINF": "Obs Insumo",
    "CD_JOB": "JOB",
    "PAÍS": "Pais",
    "REGIÃO": "Região",
    "ESTADO": "Estado",
    "MUNICÍPIO": "Municipio",
    "URL DO INSUMO": "URL Insumo Informado",
    "GRUPO DE COLETA": "Grupo de Coleta Insumo",
    "EAN": "EAN Insumo",
    "data_coleta": "Data do Preço",
    "VL_PRECCOL": "valor_anterior",
    "TAXA_FRETE": "Taxa do Frete",
    "preco_coleta": "Valor do Preço",
    "ELEMENTAR": "Elementar" 
    }

REORDER_LIST = [
    "JOB",
    "Insumo Informado",
    "Sinônimo Insumo Informado",
    "Código do Informante",
    "Código do Insumo",
    "Tipo de Preço",
    "Pais",
    "Região",
    "Estado",
    "Municipio",
    "Bairro",
    "Pais_Retirada",
    "Regiao_Retirada",
    "Estado_Retirada",
    "Municipio_Retirada",
    "Bairro_Retirada",
    "Cotação",
    "Periodicidade",
    "Data do Preço",
    "Data Prevista",
    "Valor do Preço",
    "valor_anterior",
    "Moeda",
    "Preço Promocional",
    "Valor do Frete",
    "Taxa do Frete",
    "Frete Incluso",
    "Frete Nao Declarado",
    "Valor do Desconto",
    "Taxa do Desconto",
    "Desconto Incluso",
    "Desconto Não Declarado",
    "Coletor Padrão",
    "FT",
    "Justificativa Livre",
    "URL Insumo Informado",
    "Arquivo com Preço",
    "Nome Insumo",
    "Característica Insumo",
    "Especificação Insumo",
    "Marca Insumo",
    "Embalagem Insumo",
    "Quantidade Insumo",
    "Unidade Medida Insumo",
    "Grupo de Coleta Insumo",
    "Obs Insumo",
    "EAN Insumo",
    "Elementar"
    ]

DICT_ELEMENTOS = {"cep_button": "#shipping-calculate-link",
                      "cep_input": "#ship-postalCode",
                      "adicionar_quantidade": ".vtex-numeric-stepper__plus-button__text",
                      "adicionar_carrinho": ".fibracirurgica-add-to-cart-button-0-x-buttonText",
                      "pega_frete": ".monetary",
                      "pega_preco": ".price",
                      "elemento_box": ".summary.entry-summary"
                      }

rename_itens = {
    "BOVINO VIVO VACA GORDA (ARROBA)": "vaca gorda - à vista",
    "FEIJAO CARIOCA (SCO 60 KG)": "feijão",
    "SOJA EM GRAO (SCO 60 KG)": "soja disponível",
    "OLEO DE SOJA BRUTO DEGOMADO (T)": "óleo de soja - degomado",
    "BOVINO VIVO VACA GORDA RASTREADA (ARROBA)": "vaca gorda rastreada - à vista",
    "BOVINO VIVO BOI GORDO RASTREADO (ARROBA)": "boi gordo rastreado - à vista",
    "BOVINO VIVO BOI GORDO (ARROBA)": "boi gordo - à vista",
    "MILHO AMARELO (SCO 60 KG)": "milho futuro",
    "BOVINO VIVO VACA GORDA 30 DIAS (ARROBA)": "vaca gorda - 30 dias",
}