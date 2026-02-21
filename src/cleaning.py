import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpiar y tratar los datos de INE Camping España
    """

    # -------------------------------------------------
    # Renombrado de columnas principales:
    #   - Se renombran las columnas primarias para mejorar su tratamiento más adelante
    # -------------------------------------------------
    df = df.rename(columns={
        "ï»¿Provincias con mayor nÃºmero de pernoctaciones": "provincia",
        "Establecimientos y personal empleado (parcelas)": "variable"
    })

    # -------------------------------------------------
    # Reducción de datos
    #   - Se toman solo datos a partir del 2017
    #   - Análisis pre, post y durante covid
    #   - Datos más accurate
    # -------------------------------------------------
    df["year"] = df["Periodo"].str[:4].astype(int)
    df = df[df["year"] >= 2017]

    # -------------------------------------------------
    # Limpiar columna de datos Total, para eliminar formatos no tratables con Python
    # -------------------------------------------------
    df["Total"] = df["Total"].str.replace(".", "", regex=False)
    df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

    # -------------------------------------------------
    # Poner un formato de fecha real
    # -------------------------------------------------
    df["month"] = df["Periodo"].str[5:7].astype(int)
    df["date"] = pd.to_datetime(dict(year=df["year"], month=df["month"], day=1))

    # -------------------------------------------------
    # Pivotar DataSet para que todos los datos que aparecen como filas se puedan reproducir comom columnas
    # -------------------------------------------------
    df_pivot = df.pivot_table(
        index=["provincia", "date"],
        columns="variable",
        values="Total",
        aggfunc="first"
    ).reset_index()

    # -------------------------------------------------
    # Renombrar variables finales
    # -------------------------------------------------
    df_pivot = df_pivot.rename(columns={
        "NÃºmero de establecimientos abiertos estimados": "Establecimientos",
        "NÃºmero de plazas estimadas": "Plazas",
        "NÃºmero de parcelas": "Parcelas",
        "Parcelas ocupadas": "Parcelas_Ocupadas",
        "Grado de ocupaciÃ³n por parcelas": "Ocupacion_Parcelas",
        "Grado de ocupaciÃ³n de parcelas en fin de semana": "Ocupacion_finde",
        "Personal empleado": "Personal"
    })

    return df_pivot