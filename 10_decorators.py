import functools


def f1(func):
    def wrapper(*args, **kwargs):
        print('Started')
        val = func(*args, **kwargs)
        print('Ended')
        return val

    return wrapper


@f1
def f(name):
    print(name)


f("Akshay")


@f1
def add(x, y):
    return x + y


print(add(45, 34))

# ------------------------------------------------------
# Example 2
user = {"username": 'Akshay', "access_level": "guest"}


def check_access(func):
    @functools.wraps(func)
    def is_user_admin():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f"You don't have permission to perform this operation"

    return is_user_admin


@check_access
def get_admin_password():
    return 'Admin@1234'


print(get_admin_password())


# ------------------------------------------------------
# Example 3
# https://www.geeksforgeeks.org/python-functools-wraps-function/

def check_access(func):
    @functools.wraps(func)
    def is_user_admin(*args, **kwargs):
        return func(*args, **kwargs)

    return is_user_admin


@check_access
def get_password(panel):
    if panel == 'admin':
        return 'Admin@1234'
    elif panel == 'billing':
        return 'Billing@1234'


print(get_password('billing'))

# ------------------------------------------------------
# Example 3


from sanic import Sanic, text

app = Sanic(__name__)

stores = []


@app.on_request()
async def increment_foo(request):
    if not hasattr(request.conn_info.ctx, "foo"):
        request.conn_info.ctx.foo = 0
    request.conn_info.ctx.foo += 1


@app.get('/')
async def count_foo(request):
    return text(f"request.conn_ifo.ctx.foo: {request.conn_info.ctx.foo}")


app.run(host='0.0.0.0', port=8001, debug=True)
