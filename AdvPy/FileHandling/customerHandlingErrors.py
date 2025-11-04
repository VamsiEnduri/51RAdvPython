try:
    a=input("entre some str here :-- ")
    if not a:
        raise ValueError("enter non empty str values")
except ValueError as v:
    print(v)        