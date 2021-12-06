from routes.restaurants import data_analyser_bp
blueprints = [data_analyser_bp]


def init_routes(app):
    # Register blueprints
    for blueprint in blueprints:
        app.blueprint(blueprint)