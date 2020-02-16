import threading


def printit():
    threading.Timer(0.2, printit).start()
    print("Hello, World!")


printit()
