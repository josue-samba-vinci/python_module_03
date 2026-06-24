import sys


def parse_dict(args: list[str]) -> dict[str, int]:
    rpg_dict: dict[str, int] = {}
    for arg in args:
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
        elif parts[0] in rpg_dict:
            print(f"Redundant item '{parts[0]}' - discarding")
        else:
            try:
                rpg_dict.update({parts[0]: int(parts[1])})
            except ValueError as e:
                print(f"Quantity error for '{parts[0]}': {e} '{parts[1]}'")
    return rpg_dict


def main() -> None:
    print("=== Inventory System Analysis ===")
    rpg_dict = parse_dict(sys.argv[1:])
    print(f"Got inventory: {rpg_dict}")
    print(f"Item list: {list(rpg_dict)}")
    total_quantity = 0
    for value in dict.values(rpg_dict):
        total_quantity += value
    total_keys = 0
    for key in dict.keys(rpg_dict):
        total_keys += 1
    print(f"Total quantity of the {total_keys} items: {total_quantity}")
    for key in rpg_dict:
        print(f"Item {key} represents {(rpg_dict[key]/total_quantity)*100:.1f}"
              "%")
    max_key = None
    max_value = None
    for key in rpg_dict:
        if max_value is None or rpg_dict[key] > max_value:
            max_key = key
            max_value = rpg_dict[key]
    min_key = None
    min_value = None
    for key in rpg_dict:
        if min_value is None or rpg_dict[key] > min_value:
            min_value = value
            min_key = rpg_dict[key]
    print(f"Item most abundant: {max_key} with quantity {max_value}")
    print(f"Item least abundant: {min_key} with quantity {min_value}")
    rpg_dict.update({'magic_item': 1})
    print(f"Updated inventory: {rpg_dict}")


if __name__ == "__main__":
    main()
