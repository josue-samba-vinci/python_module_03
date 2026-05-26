import random


def gen_player_achievement() -> set[str]:
    achievements = list[str]
    achievements = ["Crafting Genius", "World Savior", "Master Explorer",
                    "Collector Supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
                    "Treasure Hunter", "First Steps", "Sharp Mind",
                    "Hidden Path Finder"]
    set_achievements = set(random.sample(achievements, random.randint(0, 13)))
    return set_achievements


def main() -> None:
    achievements = {"Crafting Genius", "World Savior", "Master Explorer",
                    "Collector Supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
                    "Treasure Hunter", "First Steps", "Sharp Mind",
                    "Hidden Path Finder"}
    
    print("=== Achievement Tracker System ===")

    print()

    alice_achievements: set[str] = gen_player_achievement()
    bob_achievements: set[str] = gen_player_achievement()
    charlie_achievements: set[str] = gen_player_achievement()
    dylan_achievements: set[str] = gen_player_achievement()
    print(f"Player Alice: {alice_achievements}")
    print(f"Player Bob: {bob_achievements}")
    print(f"Player Charlie: {charlie_achievements}")
    print(f"Player Dylan: {dylan_achievements}")

    print()

    present_achievements = alice_achievements.union(
        bob_achievements, charlie_achievements, dylan_achievements)
    print(f"All distinct achievements: {present_achievements}")

    print()

    common_achievement = alice_achievements.intersection(
        bob_achievements, charlie_achievements, dylan_achievements)
    print(f"Common achievements: {common_achievement}")

    print()

    alice_different_achievements = alice_achievements.difference(
        bob_achievements, charlie_achievements, dylan_achievements)
    bob_different_achievements = bob_achievements.difference(
        alice_achievements, charlie_achievements, dylan_achievements)
    charlie_different_achievements = charlie_achievements.difference(
        bob_achievements, alice_achievements, dylan_achievements)
    dylan_different_achievements = dylan_achievements.difference(
        bob_achievements, charlie_achievements, alice_achievements)
    print(f"Only Alice has: {alice_different_achievements}")
    print(f"Only Bob has: {bob_different_achievements}")
    print(f"Only Charlie has: {charlie_different_achievements}")
    print(f"Only Dylan has: {dylan_different_achievements}")

    print()

    alice_missing_achievements = achievements.difference(
        alice_achievements)
    bob_missing_achievements = achievements.difference(
        bob_achievements)
    charlie_missing_achievements = achievements.difference(
        charlie_achievements)
    dylan_missing_achievements = achievements.difference(
        dylan_achievements)  
    print(f"Alice is missing: {alice_missing_achievements}")
    print(f"Bob is missing: {bob_missing_achievements}")
    print(f"Charlie is missing: {charlie_missing_achievements}")
    print(f"Dylan is missing: {dylan_missing_achievements}")


if __name__ == "__main__":
    main()
