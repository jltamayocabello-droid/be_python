from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RUTA_CSV = Path(__file__).parent / "datos.csv"


def estadisticas_columnas(ruta: str | Path = RUTA_CSV) -> tuple[pd.Series, pd.Series]:
    """
    Lee un CSV y devuelve la media y la desviación estándar de cada columna numérica.
    """
    df = pd.read_csv(ruta)
    media = df.mean(numeric_only=True)
    desviacion = df.std(numeric_only=True)
    return media, desviacion


if __name__ == "__main__":
    media, desviacion = estadisticas_columnas()
    print("Media:")
    print(media)
    print("\nDesviación estándar:")
    print(desviacion)

    media.plot(kind="bar", title="Media por columna", ylabel="Valor")
    plt.tight_layout()
    plt.show()
