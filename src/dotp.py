import sys


def dot_product(vector_x, vector_y):
    if len(vector_x) != len(vector_y):
        raise ValueError(len(vector_x) + "!=" + len(vector_y))
    vector_length = len(vector_x)
    result = 0
    for i in range(vector_length):
        result += vector_x[i] * vector_y[i]
    print(f"dot product result is {result}.")
    return result


def parse_input(arg):
    return list(map(int, arg.strip("[]").split(',')))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 dotp.py [vector_x] [vector_y]")
        sys.exit(1)

    vector_x = parse_input(sys.argv[1])
    vector_y = parse_input(sys.argv[2])

    dot_product(vector_x, vector_y)
