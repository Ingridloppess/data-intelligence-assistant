print('Projeto Data Intelligence Assistant iniciado!')

from src.extract.economic_data import download_indicator
from src.transform.clean_data import clean_dataframe

df = download_indicator(11)

df = clean_dataframe(df)

print(df.head())
print(df.dtypes)