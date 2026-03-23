"""
Dependencies for FastAPI endpoints.
Provides mock authentication for development.
"""
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models


def get_current_user(db: Session = Depends(get_db)) -> models.User:
    """
    Mock authentication dependency.
    Returns the hardcoded test user (ID: 1) for development.
    
    In production, this would validate JWT tokens and return the authenticated user.
    """
    user = db.query(models.User).filter(models.User.id == 1).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Test user not found. Database may not be initialized."
        )
    
    return user
