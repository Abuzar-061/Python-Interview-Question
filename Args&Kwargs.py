print("ARGS UNDERSTANDING ....")

def info_args(*args):
    for i in args:
        print(i)

info_args(1,2,3,4)

print("KWARGS UNDERSTANDING ....")

def info_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


info_kwargs(name="Abuzar", Age=22)

print("ARGS & KWARGS UNDERSTANDING ....")


def combine(*args, **kwargs):
    print("POSITIONAL ARGUMENTS:")
    for i in args:
        print(i)
    print("KEYWORD ARGUMENTS:")
    for key, value in kwargs.items():
        print(f"{key}:{value}")

combine(1,2,3,4,5, name="Abuzar",age=22)