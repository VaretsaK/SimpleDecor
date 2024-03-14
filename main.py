def simple_decor(func):
    """
    Simple decorator to print a message before and after calling the decorated function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: Decorated function.
    """
    def inner_wrapper(*args, **kwargs):
        """
        Inner wrapper function to execute before and after calling the decorated function.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.
        """
        print("Function is been called")
        result = func(*args, **kwargs)
        print("After function is been called")
        return result

    return inner_wrapper

