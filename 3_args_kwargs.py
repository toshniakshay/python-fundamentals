def print_args(*ars):
    for name in ars:
        print(name)


def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key, value)


names = ['Akshay', 'Sunil', 'Sakshi', 'Anam']
print_args(*names)


kwargs = {
    "Akshay": "SSE",
    "Sunil": "SSE",
    "Sakshi": "SSE",
    "Anam": "SSE"
}

print_kwargs(**kwargs)

