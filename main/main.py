from flask.cli import FlaskGroup
from flask_cors import CORS
from app import create_app

app = create_app()
app.app_context().push()
cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    cli()
