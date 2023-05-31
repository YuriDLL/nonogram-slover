from typing import List, Optional
from enum import IntEnum


class Mark(IntEnum):
    CROSS = -3
    EMPTY = -2
    FILL = -1


def append_number(row: list, number: int, start_index: int) -> Optional[list]:
    if start_index + number > len(row):
        return None
    new_row = row.copy()
    for index in range(start_index, start_index + number):
        if new_row[index] == Mark.CROSS:
            return None
    if start_index + number < len(new_row):
        if new_row[start_index + number] != Mark.FILL:
            new_row[start_index + number] = Mark.CROSS
        else:
            return None
    for fill_index in range(start_index, start_index + number):
        new_row[fill_index] = Mark.FILL
    return new_row


def fill_cross_end(row: list, start: int) -> bool:
    valid_row = True
    for index in range(start, len(row)):
        if row[index] == Mark.FILL:
            valid_row = False
        row[index] = Mark.CROSS
    return valid_row


def append_numbers(rows: list, current_row: list, numbers: list, start_index: int):
    numbers = numbers.copy()
    current_row = current_row.copy()
    current_number = numbers.pop(0)
    need_cross_end = len(numbers) == 0
    for shift in range(start_index, len(current_row) - current_number + 1):
        next_row = append_number(current_row, current_number, shift)
        if next_row is not None:
            if need_cross_end:
                if fill_cross_end(next_row, shift + current_number + 1):
                    rows.append(next_row)
            else:
                append_numbers(rows, next_row, numbers, shift + current_number + 1)
        if current_row[shift] == Mark.FILL:
            return
        else:
            current_row[shift] = Mark.CROSS


def fill_row_brute(row: list, numbers: list) -> list:
    assert min(numbers) > 0
    possible_rows: list = []
    new_row = row.copy()
    append_numbers(possible_rows, row, numbers, 0)
    if possible_rows:
        for cell_index in range(len(row)):
            all_cells_equal = True
            cell_mark = possible_rows[0][cell_index]
            for possible_row in possible_rows[1:]:
                if possible_row[cell_index] != cell_mark:
                    all_cells_equal = False
            if all_cells_equal:
                new_row[cell_index] = cell_mark
            else:
                new_row[cell_index] = row[cell_index]
    return new_row


def is_complete_row(row: list) -> bool:
    for cell in row:
        if cell == Mark.EMPTY:
            return False
    return True


def fill_side(field: List[list], numbers) -> bool:
    field_complite = True
    for i in range(len(field)):
        if is_complete_row(field[i]):
            continue
        field[i] = fill_row_brute(field[i], numbers[i])
        field_complite = False
    return field_complite


def rotate_field(field: List[list]) -> list:
    rotated_field = []
    for i in range(len(field[0])):
        row = []
        for j in range(len(field)):
            row.append(field[j][i])
        rotated_field.append(row)
    return rotated_field


def slove(numbers) -> list:
    assert len(numbers) == 2
    field = [[Mark.EMPTY for row in range(len(numbers[1]))] for column in range(len(numbers[0]))]
    sloved = False
    while (not sloved):
        sloved = fill_side(field, numbers[0])
        field = rotate_field(field)
        sloved = fill_side(field, numbers[1])
        field = rotate_field(field)
    return field
