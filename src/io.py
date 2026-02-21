from pathlib import Path

def load_csv(path: str | Path):
    """Load INE CSV file into a DataFrame with proper configuration."""
    import pandas as pd
    
    ### MODIFICACIÓN DE LA FUNCIÓN READ_CSV PARA TRATAR LOS DATOS CORRECTAMENTE ###
    df = pd.read_csv(
        path,
        sep=";",                    # Separadores del CSV importado: ";"
        encoding="latin-1",         # encoding del CSV del INE
        na_values=[".", ""],        # tratar "." y vacíos como NaN
    )
    
    return df
