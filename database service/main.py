from sanic import Sanic, response
import os

app = Sanic(__name__)


if __name__ == "__main__":

    @app.listener('before_server_start')
    async def before_server_start(sanic_app, loop) -> None:
        # connect to database
        from models import connect_db
        await connect_db()


    from routes import init_routes
    init_routes(app)

    app.run(host="0.0.0.0", port=os.environ.get('PORT') or 5001)
