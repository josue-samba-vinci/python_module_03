import math


def get_player_pos() -> tuple[float, int, str, bool]:
    while True:
        try:
            data = input("Enter new coordinates as floats in format 'x,y,z':")
            parts = data.split(',')
            if (len(parts) == 3):
                coords = []
                for coord in data.split(','):
                    coords.append(float(coord))
                return tuple(coords)
            else:
                print("Invalid syntax")
                continue
        except ValueError as e:
            print(f"Error on parameter '{coord}': {e}")


def main() -> None:
    tuple1: tuple[float, int, str, bool] = []
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    tuple1 = get_player_pos()
    if tuple1:
        total: int = 0
        print(f"Got a first tuple {tuple1}")
        print(f"It includes: X={tuple1[0]}, Y={tuple1[1]}, ", end="")
        print(f"Z={tuple1[2]}")
        total = tuple1[0]**2+tuple1[1]**2+tuple1[2]**2
        print(f"Distance to center: {math.sqrt(total):.4f}")
    print()
    print("Get a second set of coordinates")
    tuple2 = get_player_pos()
    result = math.sqrt((tuple2[0]-tuple1[0])**2+(tuple2[1]-tuple1[1])**2+(tuple2[2]-tuple1[2])**2)
    if tuple2:
        print(f"Distance between the 2 sets of coordinates: {result:.4f}")


if __name__ == "__main__":
    main()
