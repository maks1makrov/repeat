def header(func):
    def inner(*args, **kwargs):
        print("<h1>")
        func()
        print("</h1>")

    return inner


def say():
    print("hello world")


say = header(say)
say()
print(say.__name__)
print("-" * 10, )


def header(func):
    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")
        inner.__name__ = func.__name__

    return inner


@header  # say = header(say())
def say(name, surname="ivanov"):
    print(f"hello world from {name} {surname}")


say("maks")
print(say.__name__)
print("-" * 10)


def header(func):
    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")

    return inner


def header_2(func):
    def inner(*args, **kwargs):
        print("<h2>")
        func(*args, **kwargs)
        print("</h2>")

    return inner


@header_2
@header  # say =  header_2(header(say))
def say(name, surname="ivanov"):
    print(f"hello world from {name} {surname}")


say("maks")
print(say.__name__)
print("-" * 10)

from functools import wraps


def header(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")

    return inner


def header_2(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("<h2>")
        func(*args, **kwargs)
        print("</h2>")

    return inner


@header_2
@header  # say =  header_2(header(say))
def say(name, surname="ivanov"):
    print(f"hello world from {name} {surname}")


say("maks")
print(say.__name__)
print("-" * 10)
