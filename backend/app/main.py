from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal, Base
from app import models
from app.routers import projects, ai
from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Initialize FastAPI app
app = FastAPI(
    title="Reflectify.ai API",
    description="AI-powered reflective documentation tool with database integration",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    """
    Initialize database and create test user on startup.
    """
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create test user if not exists
    db: Session = SessionLocal()
    try:
        test_user = db.query(models.User).filter(models.User.email == "test@reflectify.ai").first()
        
        if not test_user:
            # Passlib 1.7.4 has a known bug with newer bcrypt versions in python 3.13 causing the truncate bug
            # For this test user, we will just use a dummy hash since login doesn't seem fully implemented anyway
            hashed_password = "$2b$12$NqOTv/Q0jC2zJ/G8A/QO5OQjXnS/z.QZ.QqP.Q"
            test_user = models.User(
                email="test@reflectify.ai",
                name="Test User",
                hashed_password=hashed_password
            )
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print(f"[OK] Created test user: {test_user.email} (ID: {test_user.id})")
        else:
            print(f"[OK] Test user already exists: {test_user.email} (ID: {test_user.id})")
    finally:
        db.close()


# Include Routers
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(ai.router, prefix="/api/ai", tags=["AI"])


@app.get("/")
def read_root():
    return {
        "message": "Welcome to Reflectify.ai API",
        "version": "2.0.0",
        "features": "Database-backed with mock authentication"
    }


@app.get("/routes")
def list_routes():
    """List all available routes for debugging"""
    return [{"path": route.path, "name": route.name} for route in app.routes]
