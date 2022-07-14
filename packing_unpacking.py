from datetime import date
d = (2022, 3, 15)
# date = date(d[0], d[1], d[2])
date = date(*d) #mesma coisa que a linha acima
print(date)


def new_user(active=False, admin=False):
    print(active)
    print(admin)

config = {"active": False, "admin": True}

# new_user(config.get('active'), config.get('admin'))
new_user(**config) # 1 * são as chaves 2 * são os valores


# UNPACKING

def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)

unpacking_experiment(1,2,3,4,5,6)

def unpacking_kwargs(**kwargs):
    print(kwargs)

unpacking_kwargs(named="Test", other="Other")