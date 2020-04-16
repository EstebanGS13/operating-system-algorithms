# Esteban Garcia Sanchez 1088325697

if __name__ == "__main__":

    pages = (5, 4, 3, 2, 1, 4, 3, 5, 4, 3, 2, 1, 5)
    faults = {3: 0, 4: 0}

    for frames in faults:
        memory = []

        for page in pages:
            out = None
            
            if page not in memory:
                if len(memory) == frames:
                    out = memory.pop(0)

                memory.append(page)
                faults[frames] += 1

            print(f"In: {page} --> {memory} --> Out: {out}")

        print(f"Marcos: {frames}, Fallas: {faults[frames]}\n")

    if faults[4] > faults[3]:
        print(f"La secuencia {pages} presenta anomalia de Belady")
