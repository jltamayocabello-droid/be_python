from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RUTA_CSV = Path(__file__).parent / "datos.csv"


class ErrorCargaDatos(Exception):
    """Error al leer o interpretar el archivo CSV."""


class ErrorGuardadoGrafico(Exception):
    """Error al escribir el gráfico en disco."""


def cargar_datos(ruta: str | Path = RUTA_CSV) -> pd.DataFrame:
    """Lee el CSV una sola vez y devuelve el DataFrame."""
    ruta_path = Path(ruta)

    if not ruta_path.is_file():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_path}")

    try:
        return pd.read_csv(ruta_path)
    except PermissionError as exc:
        raise PermissionError(f"Sin permiso para leer: {ruta_path}") from exc
    except pd.errors.EmptyDataError as exc:
        raise ErrorCargaDatos(f"El archivo está vacío: {ruta_path}") from exc
    except pd.errors.ParserError as exc:
        raise ErrorCargaDatos(f"Formato CSV inválido en {ruta_path}") from exc
    except OSError as exc:
        raise ErrorCargaDatos(f"Error de E/S al leer {ruta_path}: {exc}") from exc


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

    try:
        fig.savefig(ruta_salida, dpi=150, bbox_inches="tight")
    except PermissionError as exc:
        raise PermissionError(f"Sin permiso para escribir: {ruta_salida}") from exc
    except OSError as exc:
        raise ErrorGuardadoGrafico(f"Error de E/S al guardar {ruta_salida}: {exc}") from exc
    finally:
        plt.close(fig)

    return ruta_salida


def main() -> None:
    try:
        datos = cargar_datos()

        media, desviacion = estadisticas_columnas(datos)
        print("Media:")
        print(media)
        print("\nDesviación estándar:")
        print(desviacion)

        ruta_grafico = guardar_scatter_columnas(datos)
        print(f"\nScatter plot guardado en: {ruta_grafico}")

    except FileNotFoundError as exc:
        print(f"Archivo no encontrado: {exc}")
    except PermissionError as exc:
        print(f"Permiso denegado: {exc}")
    except ErrorCargaDatos as exc:
        print(f"Error al cargar datos: {exc}")
    except ValueError as exc:
        print(f"Dato inválido para el análisis: {exc}")
    except ErrorGuardadoGrafico as exc:
        print(f"Error al guardar el gráfico: {exc}")


if __name__ == "__main__":
    main()
