from app.models import Pitch, User
from app import create_app, db


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, user=User, Pitch=Pitch)

