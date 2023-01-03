def generate_cnf(puzzle, n):
    # Initialize a list to store the clauses
    clauses = []

    # Generate clauses for each row, column, and bold-lined rectangle
    for i in range(n):
        for j in range(n):
            # Generate clauses for each row
            row_vars = [get_var(n, i, j, k) for k in range(1, n+1)]
            clauses.extend(exactly_one(row_vars))

            # Generate clauses for each column
            col_vars = [get_var(n, k, j, i+1) for k in range(n)]
            clauses.extend(exactly_one(col_vars))

            # Generate clauses for each bold-lined rectangle
            box_vars = [get_var(n, i//n*n + k//n, j//n*n + k % n, l+1)
                        for k in range(n*n) for l in range(n)]
            clauses.extend(exactly_one(box_vars))

    # Generate clauses for black circles
    for row, col in puzzle.get("black", []):
        for k in range(1, n+1):
            clauses.append(
                [-get_var(n, row, col, k), -get_var(n, row, col+1, k)])

    # Generate clauses for white circles
    for row, col in puzzle.get("white", []):
        for k in range(1, n+1):
            clauses.append([-get_var(n, row, col, k), -
                           get_var(n, row, col+1, k+1)])

    # Generate the header for the DIMACS-CNF format
    header = f"p cnf {n**3} {len(clauses)}\n"

    # Convert the clauses to DIMACS-CNF format
    cnf = ""
    for clause in clauses:
        cnf += " ".join([str(x) for x in clause]) + " 0\n"

    return header + cnf


def exactly_one(vars):
    """Generates clauses for the "exactly-one" constraint"""
    clauses = []
    for i in range(len(vars)):
        for j in range(i+1, len(vars)):
            clauses.append([-vars[i], -vars[j]])
    clauses.append(vars)
    return clauses


def get_var(n, row, col, val):
    """Gets the variable number for a given cell and value"""
    return row*n*n + col*n + val


# Define the puzzle input
puzzle = {
    "n": 3,
    "black": [(0, 0), (1, 1)],
    "white": [(2, 0)]
}

# Generate the DIMACS-CNF formula for the puzzle
cnf = generate_cnf(puzzle, puzzle["n"])

# Open a file in write mode
with open("cnf.txt", "w") as f:
  # Write the DIMACS-CNF formula to the file
  f.write(cnf)

