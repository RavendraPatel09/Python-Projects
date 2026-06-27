def read_matrix(rows, cols, label):
    print(f"Enter {label} row by row, space separated:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix

def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def multiply_matrix(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        return None
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(cols_a))
    return result

def transpose_matrix(a):
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]

def print_matrix(m):
    for row in m:
        print(" ".join(str(v) for v in row))

def main():
    print("1.Add 2.Multiply 3.Transpose")
    ch = input()
    rows_a = int(input("Rows of matrix A: "))
    cols_a = int(input("Cols of matrix A: "))
    a = read_matrix(rows_a, cols_a, "matrix A")
    if ch == "1":
        rows_b = int(input("Rows of matrix B: "))
        cols_b = int(input("Cols of matrix B: "))
        b = read_matrix(rows_b, cols_b, "matrix B")
        print_matrix(add_matrix(a, b))
    elif ch == "2":
        rows_b = int(input("Rows of matrix B: "))
        cols_b = int(input("Cols of matrix B: "))
        b = read_matrix(rows_b, cols_b, "matrix B")
        result = multiply_matrix(a, b)
        if result is None:
            print("Incompatible dimensions")
        else:
            print_matrix(result)
    elif ch == "3":
        print_matrix(transpose_matrix(a))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
