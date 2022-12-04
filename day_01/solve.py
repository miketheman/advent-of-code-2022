"""https://adventofcode.com/2022/day/1"""
from itertools import groupby
from pathlib import Path

# Input file located relative to this file using Path
input_file = Path(__file__).parent / "input.txt"

# Read input file into a list line by line
with input_file.open() as f:
    data = [line.strip() for line in f]

# Split data into "elf" chunks split on empty values
elf_chunks = [list(g) for k, g in groupby(
    data, key=lambda x: x == "") if not k]

# Find the largest sum of calorie counts in `elf_chunks`
highest_calorie_count = max(sum(int(cal) for cal in chunk)
                            for chunk in elf_chunks)

print("Part 1 answer:", highest_calorie_count)

# Part 2

# Find the top three Elves carrying the most Calories.
top_three = sorted(elf_chunks, key=lambda x: sum(int(cal) for cal in x),
                   reverse=True)[:3]

# How many Calories are those Elves carrying in total?
total_calories = sum(sum(int(cal) for cal in chunk) for chunk in top_three)

print("Part 2 answer:", total_calories)
