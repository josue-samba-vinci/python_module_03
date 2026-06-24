import sys


def parse_and_store(argv: list[str]) -> list[int]:
    nb_arg = len(argv)
    scores: list[int] = []

    for i in range(1, nb_arg):
        try:
            scores.append(int(argv[i]))
        except Exception:
            print(f"Invalid parameter: '{argv[i]}'")
    return scores


def main() -> None:
    scores: list[int]
    print("=== Player Score Analytics ===")
    scores = parse_and_store(sys.argv)
    if scores:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(sys.argv) - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/(len(sys.argv)-1)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
