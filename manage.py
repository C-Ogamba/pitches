from app.models import Pitch, User
from app import create_app, db
from flask_script import Manager, Server
# from flask_migrate import Migrate, MigrateCommand

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitch=Pitch)

if __name__ == '__main__':
    app.run()