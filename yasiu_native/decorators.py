from functools import update_wrapper


def flexible_decorator(decorator):
    """
    Decorator for decorators.
    Turns Single Level decorator into two leveled decorator,
    by passing decoration parameters alongside function signature for ease of use.
    Decorators wrapped with `Flexible` can be used both with `()` and without `()` operator.
    Child decorator receive function signature, decoration parameters and function arguments.
    Supports both positional and key arguments on any level.

    Args:
        decorator - decorator for wrapping

    Returns:
        your decorated decorator: for decorating other functions.

    Example:

          @flexible_decorator
          def yourDecorator(decoratedFunction, *posParam, **keyParam):
            decoratedFunction: function To be decorated with your decorator.
            posParam, keyParam: [Optional] decorativeArguments for customizng your decorator behaviour

            def inner(*args, **kwargs):
                args kwargs: arguments of decorated funciton passed to it.
                ret = decoratedFunction(*args, **kwargs)
                return ret
            return inner

    Usage:

        yourDecorator
        def someFunction(a=1, b=2):
            pass

        yourDecorator()
        def someFunction(a=1, b=2):
            pass

        yourDecorator(decorationParam)
        def someFunction(a=1, b=2):
            pass
    """
    def wrapper(*args, **kw):
        if len(args) == 1:
            "If more arguments, then it is not function reference"
            fun1 = args[0]
        else:
            fun1 = None

        if callable(fun1):
            "Decorated without calling () in decoration"
            "No arguments were used during"
            decorWrapped = update_wrapper(decorator, fun1)
            return decorWrapped(fun1)

        def inner(fun2, ):
            ""
            decorWrapped = update_wrapper(decorator, fun2)
            ret = decorWrapped(fun2, *args, **kw)  # (*a2, **kw2)

            return ret

        return inner

    return wrapper


def flexible_decorator_2d(decor_func):
    """
    Decorator that asserts function is called even without ().
    Child decorator receives function and decoration variables if any were used.
    Supports both positional and key arguments.


    Args:
        **decor_func:

    Returns:

    Example:

          @flexible_decorator_2d
          def custom_decorator(decorative_argument):

            def wrapper(func):

                def inner(*args, **kwargs):
                    "Use decorative arguments to modify decorator"
                    ret = func(*args, **kwargs)
                    return ret

                return inner

            return wrapper

    """

    def wrapper(*args, **kw):
        if len(args) > 0:
            fun1 = args[0]

        else:
            fun1 = None

        if callable(fun1):
            "Passed callable as first argument, without calling () in decoration"
            return decor_func()(fun1)

        def inner(fun2, ):
            ret = decor_func(*args, **kw)(fun2)

            return ret

        return inner

    return wrapper


__all__ = ['flexible_decorator', 'flexible_decorator_2d']
