def is_vertex_valid(v, position, current_path, adjacency_matrix):
    if adjacency_matrix[current_path[position - 1]][v] == 0:
        return False
    if v in current_path:
        return False
    return True

def find_hamiltonian_path(adjacency_matrix, current_path, position):
    if position == len(adjacency_matrix):
        return adjacency_matrix[current_path[position - 1]][current_path[0]] == 1 
    for vertex in range(1, len(adjacency_matrix)):
        if is_vertex_valid(vertex, position, current_path, adjacency_matrix):
            current_path[position] = vertex
            if find_hamiltonian_path(adjacency_matrix, current_path, position + 1):
                return True
            current_path[position] = -1
    return False

def get_hamiltonian_path(adjacency_matrix):
    current_path = [-1] * len(adjacency_matrix)
    current_path[0] = 0
    if not find_hamiltonian_path(adjacency_matrix, current_path, 1):
        return None
    return current_path
