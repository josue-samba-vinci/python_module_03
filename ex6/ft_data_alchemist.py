import  random


def main():
    print("===  Game Data Alchemist ===")

    print()

    lst_names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    modified_names = [name.capitalize() for name in lst_names]
    capitalized_names = [name for name in lst_names if name == name.capitalize()]

    print(f"Initial list of players: {lst_names}")
    print(f"New list with all names capitalized: {modified_names}")
    print(f"New list of capitalized names only: {capitalized_names}")

    print()

    dict_names_scores: dict[str, int] = {}
    dict_names_scores = {name: random.randint(0, 1000) for name in modified_names}
    print(f"Score dict: {dict_names_scores}")
    total = 0
    for key in dict_names_scores:
        total += dict_names_scores[key]
    average = total/len(dict_names_scores)
    print(f"Score average is: {average:.2f}")
          
    high_scores = {name: score for name, score in dict_names_scores.items() if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__": 
    main()