from typing import Generator
import random

def gen_event() -> Generator[tuple[str, str], None, None]:
    names = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]
    while True:
        yield (random.choice(names), random.choice(actions))
    

def consume_event(lst: list) -> Generator[tuple[str, str], None, None]:
    while len(lst) > 0:
        random_index = random.randint(0, len(lst) - 1)
        yield lst.pop(random_index)

def main():
    event_generator = gen_event()
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1
    list_of_ten = [next(event_generator) for i in range(10)]
    print(f"Built list of ten events: {list_of_ten}")
    for event in consume_event(list_of_ten):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_of_ten}")



if __name__ == "__main__": 
    main()