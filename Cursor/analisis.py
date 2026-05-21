from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RUTA_CSV = Path(__file__).parent / "datos.csv"


def cargar_datos(ruta: str | Path = RUTA_CSV) -> pd.DataFrame:
    """Lee el CSV una sola vez y devuelve el DataFrame."""
    return pd.read_csv(ruta)


def estadisticas_columnas(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Devuelve la media y la desviación estándar de las columnas numéricas."""
    media = df.mean(numeric_only=True)
    desviacion = df.std(numeric_only=True)
    return media, desviacion


def guardar_scatter_columnas(
    df: pd.DataFrame,
    archivo_salida: str | Path | None = None,
) -> Path:
    """
    Genera un scatter plot de las dos primeras columnas numéricas y lo guarda en disco.
    Usa la interfaz orientada a objetos de matplotlib (Figure y Axes).
    """
    numericas = df.select_dtypes(include="number")

    if numericas.shape[1] < 2:
        raise ValueError("Se necesitan al menos dos columnas numéricas para el scatter plot.")

    col_x, col_y = numericas.columns[0], numericas.columns[1]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(numericas[col_x], numericas[col_y], alpha=0.8)
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    ax.set_title(f"Scatter: {col_x} vs {col_y}")
    ax.grid(True, linestyle="--", alpha=0.5)

    if archivo_salida is None:
        archivo_salida = Path(__file__).parent / "scatter_columnas.png"
    ruta_salida = Path(archivo_salida)

    fig.savefig(ruta_salida, dpi=150, bbox_inches="tight")
    plt.close(fig)

    return ruta_salida


if __name__ == "__main__":
    datos = cargar_datos()

    media, desviacion = estadisticas_columnas(datos)
    print("Media:")
    print(media)
    print("\nDesviación estándar:")
    print(desviacion)

    ruta_grafico = guardar_scatter_columnas(datos)
    print(f"\nScatter plot guardado en: {ruta_grafico}")
