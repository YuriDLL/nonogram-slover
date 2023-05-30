from nonogram_slover import fill_row_brute, Mark


def assert_row(row, numbers, ans):
    assert fill_row_brute(row, numbers) == ans


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
