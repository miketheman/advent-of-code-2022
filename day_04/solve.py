"""https://adventofcode.com/2022/day/4"""
from pathlib import Path


example_assignment_pairs = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def parse_assignement_pair_to_ranges(assignment_pair) -> tuple[range]:
    """Parse the assignment pair to two-tuple of ranges."""
    assignment_1, assignment_2 = assignment_pair.split(",")

    assignment_1_start, assignment_1_end = assignment_1.split("-")
    assignment_2_start, assignment_2_end = assignment_2.split("-")

    return (
        range(int(assignment_1_start), int(assignment_1_end) + 1),
        range(int(assignment_2_start), int(assignment_2_end) + 1),
    )


assert parse_assignement_pair_to_ranges(example_assignment_pairs[0]) == (
    range(2, 5),
    range(6, 9),
)
assert parse_assignement_pair_to_ranges(example_assignment_pairs[1]) == (
    range(2, 4),
    range(4, 6),
)


def does_either_range_fully_contain_other_range(range_1: range, range_2: range) -> bool:
    """Check if either range fully contains the other range."""
    return (
        range_1.start <= range_2.start
        and range_1.stop >= range_2.stop
        or range_2.start <= range_1.start
        and range_2.stop >= range_1.stop
    )


assert does_either_range_fully_contain_other_range(range(2, 5), range(6, 9)) is False
assert does_either_range_fully_contain_other_range(range(2, 8), range(3, 7)) is True
assert does_either_range_fully_contain_other_range(range(6, 6), range(4, 6)) is True


def solve(assignment_pairs: list) -> int:
    """
    Solve puzzle

    For each assignment pair, check if either range fully contains the other range.
    If it does, add 1 to the total.
    """
    total = 0
    for assignment_pair in assignment_pairs:
        range_1, range_2 = parse_assignement_pair_to_ranges(assignment_pair)
        if does_either_range_fully_contain_other_range(range_1, range_2):
            total += 1
    return total


assert solve(example_assignment_pairs) == 2

input_file = Path(__file__).parent / "input.txt"

with input_file.open() as f:
    assignment_pairs = [line.strip() for line in f]

print("Part 1 Result:", solve(assignment_pairs))

# Part 2


def does_any_range_overlap_other_range(range_1: range, range_2: range) -> bool:
    """Check if any range overlaps the other range."""
    return range_1.start < range_2.stop and range_1.stop > range_2.start


assert does_any_range_overlap_other_range(range(5, 8), range(7, 10)) is True
assert does_any_range_overlap_other_range(range(2, 8), range(3, 7)) is True


def solve_part_2(assignment_pairs: list) -> int:
    """
    Solve puzzle

    For each assignment pair, check if any range overlaps the other range.
    If it does, add 1 to the total.
    """
    total = 0
    for assignment_pair in assignment_pairs:
        range_1, range_2 = parse_assignement_pair_to_ranges(assignment_pair)
        if does_any_range_overlap_other_range(range_1, range_2):
            total += 1
    return total


assert solve_part_2(example_assignment_pairs) == 4

print("Part 2 Result:", solve_part_2(assignment_pairs))
