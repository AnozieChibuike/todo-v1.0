from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    created = db.Column(db.String(50))

    def __repr__(self):
        return f'<Todo {self.task}>'
