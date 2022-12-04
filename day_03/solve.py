"""https://adventofcode.com/2022/day/3"""
from pathlib import Path
from textwrap import wrap

example_rucksacks = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def split_rucksack_into_equal_compartments(rucksack: str) -> list:
    """Split rucksack into equal compartments"""
    if len(rucksack) % 2 != 0:
        raise ValueError("Rucksack must have an even number of supplies.")
    return wrap(rucksack, len(rucksack) // 2)


assert split_rucksack_into_equal_compartments("vJrwpWtwJgWrhcsFMMfFFhFp") == [
    "vJrwpWtwJgWr",
    "hcsFMMfFFhFp",
]


def find_common_supplies(rucksack: str) -> set:
    """Find the item type that appears in both compartments of each rucksack"""
    compartments = split_rucksack_into_equal_compartments(rucksack)
    return set(compartments[0]).intersection(set(compartments[1]))


assert find_common_supplies(example_rucksacks[0]) == {"p"}
assert find_common_supplies(example_rucksacks[1]) == {"L"}
assert find_common_supplies(example_rucksacks[2]) == {"P"}
assert find_common_supplies(example_rucksacks[3]) == {"v"}
assert find_common_supplies(example_rucksacks[4]) == {"t"}
assert find_common_supplies(example_rucksacks[5]) == {"s"}


def compute_priotity(item: str) -> int:
    """Compute priority of item
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    """
    if item.islower():
        return ord(item) - 96
    return ord(item) - 38


assert compute_priotity("a") == 1
assert compute_priotity("z") == 26
assert compute_priotity("A") == 27
assert compute_priotity("Z") == 52


def solve(rucksacks: list) -> int:
    """Solve puzzle"""
    return sum(
        [
            compute_priotity(item)
            for rucksack in rucksacks
            for item in find_common_supplies(rucksack)
        ]
    )


assert solve(example_rucksacks) == 157

input_file = Path(__file__).parent / "input.txt"

with input_file.open() as f:
    rucksacks = [line.strip() for line in f]

print("Part 1 Result:", solve(rucksacks))


# Part 2


def find_badge(rucksacks: list) -> str:
    """Find the item type that appears in all rucksacks"""
    return set.intersection(*[set(rucksack) for rucksack in rucksacks])


assert find_badge(example_rucksacks[:3]) == {"r"}
assert find_badge(example_rucksacks[3:]) == {"Z"}


def solve_part_2(rucksacks: list) -> int:
    """Solve puzzle"""
    return sum(
        [
            compute_priotity(item)
            for rucksacks in zip(*[iter(rucksacks)] * 3)
            for item in find_badge(rucksacks)
        ]
    )


assert solve_part_2(example_rucksacks) == 70

print("Part 2 Result:", solve_part_2(rucksacks))
