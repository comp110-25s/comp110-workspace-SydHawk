__author__: str = "730663953"


"""[Invert]"""
# this invert function matches a sport to a player


def invert(variable_name: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}  # create empty dict
    for key in variable_name:
        value = variable_name[key]
        if value in inverted:
            raise KeyError("repeated values can't be inverted")
        inverted[value] = key
    return inverted

    # loop through input (new key value pair)
    # key word error
    return invert


"""[Count]"""
# this count function counts the number of different cakes made


def count(cake_options: list[str]) -> dict[str, int]:
    """Count the number of cakes ordered"""
    orders: dict[str, int] = {}
    # empty dictionary; used to keep track of amounts of each cake ordered

    for cake in cake_options:  # making sure the ordered cake is an option
        if cake in orders:
            # checking if the cake option has already been ordered atleast once
            orders[cake] += 1  # increase order by 1 if already in dictionary
        else:
            orders[cake] = (
                1  # adding the cake to orders for first time if not ordered already
            )

    return orders


"""[Favorite Color]"""


def favorite_color(favorites: dict[str, str]) -> str:
    """Return most frequent favorite color"""
    color_counts: dict[str, int] = {}
    # empty dictionary; used to store favorite color "responses"

    # count color
    for name in favorites:  # for the color from favorites
        color = favorites[name]  # setting the name from favorite to the actual color
        if color in color_counts:  # color_counts represents "responses"
            color_counts[color] += 1  # increase that color count by 1
        else:
            color_counts[color] = 1

    # determine most popular color (frequency)

    most_frequent_color: str = ""  # will return the most frequent color
    max: int = 0  # used as a starting point to count frequency

    for color in color_counts:
        if color_counts[color] > max:
            most_frequent_color = color
            max = color_counts[
                color
            ]  # setting the max to the frequency of the color (was originally at 0)

    return most_frequent_color


"""[Bin Len]"""


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """bins a list of words into dictionary based on word length"""
    bins: dict[int, set[str]] = {}  # empty dictionary; used to store bins

    for word in words:
        length = len(word)  # variable to determine and store length of word

        if length in bins:  # if that length has a bin to go in already
            bins[length].add(word)  # take that length bin and add the word to it
        else:
            bins[length] = {word}  # create a bin/dictionary for that length

    return bins
