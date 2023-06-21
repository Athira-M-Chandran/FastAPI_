from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    executed_at = Column(DateTime, onupdate=func.now())

    def set_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.password = hashed_password.decode()
        # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # self.password = hashed_password.decode('utf-8')