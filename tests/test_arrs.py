from utils import arrs


def test_get(array_fixture_1, array_fixture_2):
    assert arrs.get(array_fixture_2, 1, "test") == 2
    assert arrs.get(array_fixture_1, 0, "test") == "test"


def test_slice(array_fixture_1, array_fixture_2, array_fixture_3):
    assert arrs.my_slice(array_fixture_3, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture_2, 1) == [2, 3]
    assert arrs.my_slice(array_fixture_1, 1) == []
    assert arrs.my_slice(array_fixture_2) == [1, 2, 3]
