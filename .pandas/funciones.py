def promedio(na, nc):
    try:
        df = pd.read_csv(na)
        
        if nc not in df.columns:
            return "No existe la columna"

        return df[nc].mean()

    except Exception as e:
        return f"Error al procesar la columna"
    
def desviacion(nombre_archivo, nombre_columna):
    try:
        if nombre_archivo.endswith(".csv"):
            df = pd.read_csv(nombre_archivo)
        elif nombre_archivo.endswith(".xlsx") or nombre_archivo.endswith(".xls"):
            df = pd.read_excel(nombre_archivo)
        else:
            print("Formato de archivo no soportado.")
            return None
        
        if nombre_columna not in df.columns:
            print("No existe la columna")
            return None
        
        return df[nombre_columna].std()

    except FileNotFoundError:
        print("No se encontró el archivo.")
        return None
