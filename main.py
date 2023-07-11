from utils.constantes import data
from utils.createcarga import intervalo_datas, create_carga, create_folder, read_table
from PADRAO import SCRAPER
import pandas as pd



if __name__ == '__main__':

    nm_site = 'BOM_JESUS_ENGENHARIA'
    cod_informante = "99382"
    price_element = "#price_display"

    dt_prev = pd.Timestamp(year=data.year, month=data.month, day=data.day)
    print("Data Prevista: ", dt_prev)
    data_atual = str(data.year) + "_" + str(data.month).zfill(2) + "_" + str(data.day).zfill(2)
    dt_prev_ini, dt_prev_fim = intervalo_datas(dt_prev)
    create_folder(dt_prev, dt_prev_fim, nm_site)
    encomenda = read_table(cod_informante)
    SCRAPER(encomenda, price_element)
    create_carga(encomenda, cod_informante=cod_informante, nm_site=nm_site)