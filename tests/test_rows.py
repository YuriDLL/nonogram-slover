from nonogram_slover import fill_row_brute, Mark, slove


def assert_row(row, numbers, ans):
    assert fill_row_brute(row, numbers) == ans


def convert_to_marks(str_field: list) -> list:
    mark_field = []
    for str_row in str_field:
        mark_row = []
        for sym in str_row:
            if sym == '◼':
                mark_row.append(Mark.FILL)
            else:
                mark_row.append(Mark.CROSS)
        mark_field.append(mark_row)
    return mark_field


def marks_to_str(mark_field: list) -> list:
    str_field = []
    for mark_row in mark_field:
        str_row = ''
        for sym in mark_row:
            str_row += '◼' if sym == Mark.FILL else '◻'
        str_field.append(str_row)
    return str_field


def test_unrecognized():
    assert_row(
        row=[Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
        numbers=[1, 1, 1],
        ans=[Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY]
    )


def test_set_cross():
    assert_row(
        row=[Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.FILL, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
        numbers=[3],
        ans=[Mark.CROSS, Mark.EMPTY, Mark.EMPTY, Mark.FILL, Mark.EMPTY, Mark.EMPTY, Mark.CROSS]
    )


def test_rigth_align():
    assert_row(
        row=[Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.FILL],
        numbers=[3],
        ans=[Mark.CROSS, Mark.CROSS, Mark.CROSS, Mark.CROSS, Mark.FILL, Mark.FILL, Mark.FILL]
    )


def test_ones_easy():
    assert_row(
        row=[Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
        numbers=[1, 1, 1, 1],
        ans=[Mark.FILL, Mark.CROSS, Mark.FILL, Mark.CROSS, Mark.FILL, Mark.CROSS, Mark.FILL]
    )


def test_fill_little_slots():
    assert_row(
        row=[Mark.CROSS, Mark.EMPTY, Mark.CROSS, Mark.EMPTY, Mark.CROSS, Mark.EMPTY, Mark.EMPTY],
        numbers=[2],
        ans=[Mark.CROSS, Mark.CROSS, Mark.CROSS, Mark.CROSS, Mark.CROSS, Mark.FILL, Mark.FILL]
    )


def test_fill_classification():
    assert_row(
        row=[Mark.EMPTY, Mark.EMPTY, Mark.FILL, Mark.EMPTY, Mark.EMPTY,
             Mark.EMPTY, Mark.CROSS, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
        numbers=[2, 3],
        ans=[Mark.CROSS, Mark.EMPTY, Mark.FILL, Mark.EMPTY, Mark.CROSS,
             Mark.CROSS, Mark.CROSS, Mark.FILL, Mark.FILL, Mark.FILL]
    )


def test_slove_easy():
    rule = [
        [
            [10],
            [1, 1],
            [1, 1, 1],
            [1, 3, 1],
            [1, 1],
            [1, 3, 1],
            [1, 1],
            [1, 3, 1],
            [1, 1],
            [10]
        ],
        [
            [10],
            [1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1],
            [1, 1],
            [1, 1, 1],
            [1, 1],
            [10]
        ],
    ]
    ans = [
        '◼◼◼◼◼◼◼◼◼◼',
        '◼◻◻◻◻◻◻◻◻◼',
        '◼◻◻◻◻◻◻◼◻◼',
        '◼◻◼◼◼◻◻◻◻◼',
        '◼◻◻◻◻◻◻◻◻◼',
        '◼◻◼◼◼◻◻◻◻◼',
        '◼◻◻◻◻◻◻◻◻◼',
        '◼◻◼◼◼◻◻◻◻◼',
        '◼◻◻◻◻◻◻◻◻◼',
        '◼◼◼◼◼◼◼◼◼◼',
    ]
    ans = convert_to_marks(ans)
    assert ans == slove(rule)


def test_slove_medium():
    rule = [
        [
            [1, 1],
            [2],
            [1, 2],
            [1, 3, 2],
            [6, 2],
            [1, 3, 1, 1, 2, 1],
            [2, 1, 1, 2, 2, 3],
            [4, 7, 2],
            [12],
            [2, 11],
            [9, 1, 2],
            [3, 1, 2, 2, 2],
            [2, 1, 2, 1, 1, 1],
            [2, 1, 1, 2, 4],
            [2, 1, 1, 6],
            [1, 2, 2, 2, 1, 2],
            [5, 1, 2, 3, 2],
            [1, 2, 7, 1],
            [2, 11, 1],
            [2, 8, 5],
            [2, 2, 6, 4],
            [2, 2, 6],
            [2, 2, 5],
            [5, 3],
            [3],
        ],
        [
            [2, 1, 2],
            [2, 2, 1, 6],
            [1, 2, 12],
            [3, 7, 2],
            [2, 6, 1, 3],
            [4, 3, 1, 4],
            [1, 15],
            [7, 3],
            [2, 7, 4],
            [4, 16],
            [1, 4, 9],
            [8, 7],
            [4, 3, 3, 8],
            [4, 2, 10],
            [1, 3, 1, 3],
            [1, 2, 2, 1, 3],
            [2, 4, 3],
            [2, 2, 2],
            [1, 4, 2],
            [2, 6],
        ],
    ]
    ans = [
        '◻◻◻◻◻◻◻◻◻◻◻◻◻◼◻◼◻◻◻◻',
        '◻◻◻◻◻◻◻◻◻◻◻◻◻◼◼◻◻◻◻◻',
        '◻◻◻◻◻◻◻◻◻◼◻◻◼◼◻◻◻◻◻◻',
        '◻◻◻◻◻◼◻◻◼◼◼◻◼◼◻◻◻◻◻◻',
        '◻◻◻◻◼◼◼◼◼◼◻◼◼◻◻◻◻◻◻◻',
        '◼◻◻◼◼◼◻◼◻◼◻◼◼◻◻◻◻◼◻◻',
        '◼◼◻◼◻◼◻◼◼◻◼◼◻◻◻◻◼◼◼◻',
        '◻◼◼◼◼◻◼◼◼◼◼◼◼◻◻◼◼◻◻◻',
        '◻◻◻◻◼◼◼◼◼◼◼◼◼◼◼◼◻◻◻◻',
        '◼◼◻◻◼◼◼◼◼◼◼◼◼◼◼◻◻◻◻◻',
        '◻◼◼◼◼◼◼◼◼◼◻◼◻◻◼◼◻◻◻◻',
        '◻◻◼◼◼◻◼◻◼◼◻◼◼◻◻◼◼◻◻◻',
        '◻◻◻◼◼◻◼◻◼◼◻◻◼◻◻◻◼◻◻◼',
        '◻◻◼◼◻◻◼◻◻◼◻◻◼◼◻◻◼◼◼◼',
        '◻◻◼◼◻◻◼◻◻◼◻◻◻◼◼◼◼◼◼◻',
        '◼◻◼◼◻◼◼◻◻◼◼◻◻◼◻◻◻◻◼◼',
        '◼◼◼◼◼◻◼◻◻◼◼◻◼◼◼◻◻◻◼◼',
        '◻◻◼◻◻◻◼◼◻◼◼◼◼◼◼◼◻◻◻◼',
        '◻◼◼◻◻◻◼◼◼◼◼◼◼◼◼◼◼◻◻◼',
        '◻◼◼◻◻◻◼◼◼◼◼◼◼◼◻◼◼◼◼◼',
        '◻◼◼◻◻◼◼◻◼◼◼◼◼◼◻◻◼◼◼◼',
        '◻◼◼◻◻◼◼◻◼◼◼◼◼◼◻◻◻◻◻◻',
        '◻◼◼◻◼◼◻◻◻◼◼◼◼◼◻◻◻◻◻◻',
        '◻◼◼◼◼◼◻◻◻◻◼◼◼◻◻◻◻◻◻◻',
        '◻◻◼◼◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻',

    ]
    ans = convert_to_marks(ans)
    assert ans == slove(rule)
