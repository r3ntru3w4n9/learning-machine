from numpy import ndarray


def star_temparature(image: ndarray) -> float:
    """
    This function looks just like `cat_or_dog` but is actually different
    since the return value does not have a range.
    """
    return (10000 * image.sum() / image.size).item()
