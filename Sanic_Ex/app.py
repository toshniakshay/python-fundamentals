from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)


@app.get("/")
async def hello_world(request):
    return text("Hello World!!")


if __name__ == '__main__':
    app.run()