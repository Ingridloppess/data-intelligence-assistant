import requests
import pandas as pd


def download_indicator(codigo):

    url = (
        f"https://api.bcb.gov.br/dados/"
        f"serie/bcdata.sgs.{codigo}/dados"
        f"?formato=json"
        f"&dataInicial=01/01/2020"
    )
    print(f"Baixando indicador {codigo}...")
    print(url)
    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    dados = response.json()

    if isinstance(dados, dict):
        print("Erro retornado pela API:")
        print(dados)
        return None

    df = pd.DataFrame(dados)


    return df


df = download_indicator(11)

if df is not None:
    print(df.head())
    print(df.shape)