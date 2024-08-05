
from app import db

class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(128), unique=True, nullable=False)
    is_vulnerable = db.Column(db.Boolean, default=False)
    last_checked = db.Column(db.DateTime)
