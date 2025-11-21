import matplotlib.pyplot as plt

prom_cp1 = df.filter(regex="CP1").iloc[:, 0].mean()
prom_nf  = df.filter(regex="NF").iloc[:, 0].mean()
prom_cp2 = df["CP2"].mean()
prom_cp3 = df["CP3"].mean()
plt.figure(figsize=(6,4))
plt.title("Promedios")
plt.bar(
    ["CP1", "CP2", "CP3", "NF"],
    [prom_cp1, prom_cp2, prom_cp3, prom_nf]
)

plt.ylabel("Promedio")
plt.xlabel("Calificaciones")
plt.show()

def grafico_desviaciones(nombre_archivo):
    columnas = ["CP1", "CP2", "CP3", "NF"]
    desv = []
    for col in columnas:
        d = desviacion(nombre_archivo, col)
        desv.append(d if d is not None else 0)

    plt.figure(figsize=(8,5))
    plt.bar(columnas, desv, color=["#4C72B0"])
    plt.title("Desviaciones")
    plt.ylabel("Desviación estándar")
    plt.xlabel("Calificaciones")

    plt.savefig("Desviaciones.png") 
    plt.show()


nf = df.filter(regex="NF").iloc[:, 0]

percentiles = list(range(10, 100, 10))

valores = np.percentile(nf, percentiles)

plt.figure(figsize=(8,5))
plt.title("Percentiles")

plt.bar([str(p) for p in percentiles], valores)

plt.xlabel("Percentil")
plt.ylabel("Valor en NF")
plt.show()    