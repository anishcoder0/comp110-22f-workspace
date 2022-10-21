"""Dictionary exercise EX07."""


__author__: str = "730574592"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values given."""
    output: dict[str, str] = {}
    for key in input_dict:
        # checks to see if there is already duplicate key.
        if input_dict[key] in output:
            raise KeyError("Cannot have 2 duplicate key values.")
        else:
            # Creates new inverted dictionary.
            output[input_dict[key]] = key 
    return output
    

def favorite_color(name_color: dict[str, str]) -> str:
    """A function that reutrns the most repeated colors in a dictionary."""
    color_list: dict[str, int] = {}
    # loops through and adds up all the times color was listed and stores in color_list dictionary.
    for x in name_color:
        if name_color[x] in color_list:
            color_list[name_color[x]] += 1
        else:
            color_list[name_color[x]] = 1

    # print(color_list)
    counter: int = 0
    color: str = ""
    # returns the color that is repeated the most times.
    for x in color_list:
        if color_list[x] > counter:
            counter = color_list[x]
            color = x
    
    return color


def count(my_list: list[str]) -> dict[str, int]:
    """Counts up the number of times a str is repated and stores it in dict."""
    count_list: dict[str, int] = {}
    for x in my_list:
        if x in count_list:
            count_list[x] += 1
        else:
            count_list[x] = 1

    return count_list