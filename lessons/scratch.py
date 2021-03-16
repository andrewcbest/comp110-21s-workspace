
def f(a: list[str]) -> None:
    a[0] = "p"
    a = ["m", "j"]
    print(a)
a: list[str] = ["w", "u"]
f(a)

def g() -> None:
    global a
    a[1] = "y"
    a = ["k", "g"]
    print(a)
print(a)

g()
print(a)
