from app.extensions.extensions import db
from datetime import datetime

class Access(db.Model):

    __tablename__ = 'access'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    access_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f"<User {self.email}>"
