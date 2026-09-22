import requests
import pandas as pd


def download_indicator(codigo):

    url = (
        f"https://api.bcb.gov.br/dados/"
        f"serie/bcdata.sgs.{codigo}/dados"
        f"?formato=json"
        f"&dataInicial=17/09/2016"
    )

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    dados = response.json()

    df = pd.DataFrame(dados)

    return df
