from typing import List
from enum import IntEnum


class Mark(IntEnum):
    CROSS = -3
    EMPTY = -2
    FILL = -1


def fill_row(row: List[int], numbers, reverse=False):
    if reverse:
        row.reverse()
        numbers.reverse()
    row_i = 0
    for num_i, number in enumerate(numbers):
        number_fill = num_i if not reverse else len(numbers) - 1 - num_i
        for dot in range(number):
            while row[row_i] == Mark.CROSS:
                row_i += 1
            row[row_i] = number_fill
            row_i += 1
        while row_i < len(row) and row[row_i] == Mark.FILL:
            row[row_i] = number_fill
            row[row_i - number] = Mark.EMPTY
            row_i += 1
        row_i += 1
    if row_i < len(row):
        for i in range(row_i, len(row)):
            if row[i] == Mark.FILL:
                last_num_fill = len(numbers) - 1
                for i, cell in enumerate(row):
                    if cell == last_num_fill:
                        row[i] = Mark.EMPTY
                for insert_i in range(i - numbers[-1] + 1, i + 1):
                    row[insert_i] = last_num_fill
    if reverse:
        row.reverse()
        numbers.reverse()


def unite_rows(left_row, rigth_row, numbers):
    row_len = len(left_row)
    row = [Mark.EMPTY for cell in range(row_len)]
    complite_numbers = [0 for cell in range(len(numbers))]
    for rigth_cell, left_cell, col in zip(left_row, rigth_row, range(row_len)):
        assert rigth_cell != Mark.FILL
        assert left_cell != Mark.FILL
        if rigth_cell == left_cell and rigth_cell >= 0:
            complite_numbers[rigth_cell] += 1
            row[col] = Mark.FILL
    full_complite = True
    for complite_number, number, i in \
            zip(complite_numbers, numbers, range(len(numbers))):
        if complite_number == number:
            num_start_i = left_row.index(i)
            if num_start_i != 0:
                row[num_start_i - 1] = Mark.CROSS
            num_end_i = num_start_i + number
            if num_end_i != row_len:
                row[num_end_i] = Mark.CROSS
        else:
            full_complite = False
    if full_complite:
        row = [Mark.FILL if cell == Mark.FILL else Mark.CROSS for cell in row]
    return row, full_complite


def fill_side(field: List[list], numbers):
    field_complite = True
    for row, row_numbes in enumerate(numbers):
        left_row = field[row].copy()
        fill_row(left_row, row_numbes)
        rigth_row = field[row].copy()
        fill_row(rigth_row, row_numbes, reverse=True)
        pass
        field[row], row_colplite = unite_rows(left_row, rigth_row, row_numbes)
        field_complite &= row_colplite
    return field_complite


def append_number(row: list, number: Mark, start_index: int, shift: int) -> list:
    new_row = []
    for index, number in enumerate(row):
        pass
    return 0


def fill_row_brute(row: list, numbers: list) -> list:
    new_rows = []
    for number in numbers:
        pass
    return 0


def slove(numbers):
    assert len(numbers) == 2
    field = [[Mark.EMPTY for row in range(len(numbers[0]))]
             for column in range(len(numbers[1]))]
    sloved = False
    while (not sloved):
        sloved = fill_side(field, numbers[0])
