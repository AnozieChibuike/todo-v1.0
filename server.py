from app import app, db
from app.models import Todo

@app.shell_context_processor
def shell_context():
    return {'db': db, 'Todo': Todo,}
