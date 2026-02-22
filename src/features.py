import pandas as pd

### FEATURES PARA ANÁLISIS ESTRÁTEGICO DEL SECTOR ###
# --------------------------------------------------
#   Incluimos nuevas columnas a nuestro data frame
#   para enriquecerlo con más variables
# --------------------------------------------------

def build_features(df: pd.DataFrame) -> pd.DataFrame:

    # --------------------------------------------
    # Intensidad laboral
    #   Tamaño medio de plantilla
    # --------------------------------------------
    df["empleados_por_establecimiento"] = (
        df["Personal"] / df["Establecimientos"].replace(0, pd.NA)
    )

    df["empleados_por_parcela"] = (
        df["Personal"] / df["Parcelas"].replace(0, pd.NA)
    )

    # --------------------------------------------
    # Tamaño medio del camping
    # --------------------------------------------
    df["parcelas_por_establecimiento"] = (
        df["Parcelas"] / df["Establecimientos"].replace(0, pd.NA)
    )

    # --------------------------------------------
    # Ocupación real mensual
    #   Ajustamos por número de días del mes
    # --------------------------------------------
    df["dias_mes"] = df["date"].dt.days_in_month

    df["ocupacion_real"] = (
        df["Parcelas_Ocupadas"] /
        (df["Parcelas"] * df["dias_mes"])
    )

    return df