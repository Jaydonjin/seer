from app import db


class article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    auther = db.Column(db.String(100))
    body = db.Column(db.BLOB)
    liketime = db.Column(db.Integer)
    pushdate = db.Column(db.Float)
