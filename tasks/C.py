from typing import List


def process_list(list_: List[str | int]) -> List[str | int]:
    """
    Transforms a list by adding the prefix "abc_" and the suffix "_cba" to each string element,
    and squaring each integer element.
    """
    new_list = list(
        map(lambda x: "abc_" + x + "_cba" if isinstance(x, str) else x ** 2, list_)
    )
    return new_list
