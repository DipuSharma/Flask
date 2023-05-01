from flask import Blueprint

urls_blueprint = Blueprint('urls', __name__,)


@urls_blueprint.route('/')
def index():
    return 'urls index route'