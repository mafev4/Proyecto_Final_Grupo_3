def promedio(na, nc):
    try:
        df = pd.read_csv(na)
        
        if nc not in df.columns:
            return "No existe la columna"

        return df[nc].mean()

    except Exception as e:
        return f"Error al procesar la columna"