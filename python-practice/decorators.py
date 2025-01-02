def announce(f):
    def wrapper():
        print("Doing something before executing the function...")
        f()
        print("Printing after executing the function!")

    return wrapper

@announce
def greet():
    print("Hello world!")

greet()    