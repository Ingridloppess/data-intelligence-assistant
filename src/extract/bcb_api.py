import requests
import pandas as pd

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=17/09/2016"

print(url)
response = requests.get(
    url,
    timeout=30
)

dados = response.json()
print(type(dados))
print(dados)
df = pd.DataFrame(dados)

print(df.head())

# Validações
print("\nShape:")
print(df.shape)

print("\nTipos:")
print(df.dtypes)

print("\nValores nulos:")
print(df.isnull().sum())

# Salvar CSV
df.to_csv(
    "data/raw/selic.csv",
    index=False
)

print("\nArquivo salvo com sucesso!")