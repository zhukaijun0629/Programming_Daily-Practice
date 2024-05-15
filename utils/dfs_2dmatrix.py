def dfs(matrix):
    # 1. Check for an empty graph.
    if not matrix:
        return []
    # 2. Initialize
    ROWS, COLS = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        # a. Check if visited
        if (i, j) in visited:
            return
        # b. Else add to visted
        visited.add((i, j))
        # c. Traverse neighbors.
        for direction in directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if 0 <= next_i < ROWS and 0 <= next_j < COLS:
                # d. Add in your question-specific checks.
                traverse(next_i, next_j)
        # (Optional) e. if need backtracking
        visited.discard((i, j))

# 3. For each point, traverse it.
    for i in range(ROWS):
        for j in range(COLS):
            traverse(i, j)

    return something
