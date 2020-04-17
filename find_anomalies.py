import random
import time


def anomaly(pages):
    faults = {3: 0, 4: 0}

    for frames in faults:
        memory = []

        for page in pages:
            if page not in memory:
                if len(memory) == frames:
                    memory.pop(0)

                memory.append(page)
                faults[frames] += 1

    return True if faults[4] > faults[3] else False


if __name__ == "__main__":

    size = 13       # Tamanio de la secuencia
    minutes = 1/4   # Duracion de la busqueda
    sequences = 0   # Secuencias evaluadas
    anomalies = 0   # Anomalias encontradas
    repeated = 0    # Anomalias repetidas
    file_name = "sequences.txt"
    
    try:
        with open(file_name, "a+") as file:
            print("Procesando...")
            file.seek(0)                            # Posicionar al inicio del archivo
            data = file.read().splitlines()         # Guardar secuencias como lista de strs
            timeout = time.time() + 60 * minutes    # Sumar x min desde ahora

            while time.time() < timeout:            # Hasta que pasen x min
                pages = [random.randint(1, 5) for i in range(size)]
                sequences += 1
                
                if anomaly(pages):
                    pages = str(pages)              # Convertir pages de list a str
                    if pages in data:               # Si ya esta repetida, continuar
                        repeated += 1
                        continue

                    anomalies += 1
                    data.append(pages)              # Agregar a data
                    file.write(f"{pages}\n")        # Escribir en archivo

        print(f"{sequences} secuencias evaluadas\n{anomalies} nuevas anomalias encontradas ({len(data)} en total), {repeated} repetidas")

    except OSError:
        print(f"Error al manipular el archivo {file_name}")
