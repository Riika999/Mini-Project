from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # ... other user fields

    def __repr__(self):
        return f'<User {self.name}>'

# Define other models as needed (e.g., Product, Order)
