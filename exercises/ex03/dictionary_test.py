__author__: str = "730663953"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len

# Invert Unit Tests


def test_invert_use_case_1():
    """ "testing single strings"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_case_2():
    """testing multiple strings"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_edge_case():
    """Testing edge case with KeyError"""
    assert invert({}) == {}


# Count Unit Tests


def test_count_use_case_1():
    """Test normal ordering of multiple cakes"""
    assert count(["chocolate", "vanilla", "chocolate", "strawberry"]) == {
        "chocolate": 2,
        "vanilla": 1,
        "strawberry": 1,
    }


def test_count_use_case_2():
    """Testing when cake option is not ordered"""
    assert count(["chocolate"]) == {"chocolate": 1}


def test_count_edge_case():
    assert count([]) == {}


# Favorite Color Unit Test


def test_favorite_color_use_case_1():
    assert (
        favorite_color(
            {"John": "blue", "Charlie": "blue", "Sally": "pink", "James": "yellow"}
        )
        == "blue"
    )


def test_favorite_color_use_case_2():
    assert (
        favorite_color({"Charlie": "green", "John": "blue", "James": "yellow"})
        == "green"
    )


def test_favorite_color_edge_case_():
    assert favorite_color({}) == ""  # empty dict, empty str, no responses


# Bin Len Unit Test


def test_bin_len_use_case_1():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_2():
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}  # no repeats


def test_bin_len_edge_case():
    assert bin_len([]) == {}
