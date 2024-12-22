from app.models import User

def create_user(data):
    user = User(**data) 
    db.session.add(user)
    db.session.commit()
    return user

# ... other service functions
