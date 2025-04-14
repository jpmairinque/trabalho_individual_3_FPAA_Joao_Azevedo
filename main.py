from functions import *

import time

if __name__ == "__main__":    
    
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    start_time = time.time()

    path = get_hamiltonian_path(graph)
    
    print("Caminho Hamiltoniano encontrado:" if path else "Nenhum caminho encontrado.")
    print(path)

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Tempo de execução: {elapsed_time:.6f} segundos")
