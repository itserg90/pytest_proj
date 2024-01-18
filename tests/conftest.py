import pytest

ARRAY_1 = []
ARRAY_2 = [1, 2, 3]
ARRAY_3 = [1, 2, 3, 4]


@pytest.fixture
def array_fixture_1():
    return ARRAY_1.copy()


@pytest.fixture
def array_fixture_2():
    return ARRAY_2.copy()


@pytest.fixture
def array_fixture_3():
    return ARRAY_3.copy()