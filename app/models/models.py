from app import db


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f"{self.id} {self.todo}"
