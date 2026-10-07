from src.extract.economic_data import (
    download_indicator
)

from src.transform.clean_data import (
    clean_dataframe
)

from src.utils.save_files import (
    save_csv
)
from src.utils.logger import logger

INDICATORS = {
    "selic": 11,
    "ipca": 433,
    "dolar": 1
}

def run_pipeline():

    for name, code in INDICATORS.items():

        logger.info(
            f"Baixando {name}..."
        )

        raw_df = download_indicator(code)

        save_csv(
            raw_df,
            f"data/raw/{name}.csv"
        )

        clean_df = clean_dataframe(
            raw_df
        )

        save_csv(
            clean_df,
            f"data/processed/{name}.csv"
        )

        logger.info(
            f"{name} concluído."
        )

if __name__ == "__main__":
    run_pipeline()