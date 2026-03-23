from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# -------- User Schemas --------
class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# -------- Reflection Schemas --------
class ReflectionBase(BaseModel):
    input_text: str

class ReflectionCreate(ReflectionBase):
    project_id: int

class ReflectionOut(ReflectionBase):
    id: int
    summary: Optional[str]
    created_at: datetime
    project_id: int

    class Config:
        from_attributes = True

# -------- Project Schemas --------
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int
    created_at: datetime
    user_id: int
    reflections: List[ReflectionOut] = []  

    class Config:
        from_attributes = True


# -------- AI Summarization Request --------
class SummarizeRequest(BaseModel):
    text: str
    project_title: Optional[str] = None
    save_to_project: bool = True
