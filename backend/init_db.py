"""
Database initialization script.
Run this to manually create the database and test user.
"""
from app.database import engine, SessionLocal, Base
from app.models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def init_db():
    """Initialize database with tables and test user."""
    print("🔧 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")
    
    db = SessionLocal()
    try:
        # Check if test user exists
        test_user = db.query(User).filter(User.email == "test@reflectify.ai").first()
        
        if test_user:
            print(f"ℹ️ Test user already exists: {test_user.email} (ID: {test_user.id})")
        else:
            # Create test user
            hashed_password = pwd_context.hash("testpassword123")
            test_user = User(
                email="test@reflectify.ai",
                name="Test User",
                hashed_password=hashed_password
            )
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print(f"✅ Test user created: {test_user.email} (ID: {test_user.id})")
            print(f"   Password: testpassword123")
    finally:
        db.close()
    
    print("\n🎉 Database initialization complete!")
    print("   You can now start the API server with: uvicorn app.main:app --reload")


if __name__ == "__main__":
    init_db()
