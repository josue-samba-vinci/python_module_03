import sys


def main() -> None:
    nbr_arg = len(sys.argv)
    program_name = sys.argv[0].split("/")[-1]
    print("=== Command Quest ===")
    print(f"Program name: {program_name}")
    if len(sys.argv) == 1:
        print("No arguments provided")
    else:
        print(f"Arguments received: {nbr_arg}")
        for i in range(1, nbr_arg):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {nbr_arg}")


if __name__ == "__main__":
    main()
