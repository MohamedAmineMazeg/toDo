from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(UserMixin, Base):

    def __init__(self, id, email, password, username, firstname, lastname, dateAdd):
        self.id = self.get_id()
        self.email = email
        self.password = password
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.dateAdd = dateAdd

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    email: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    firstname: Mapped[str] = mapped_column(String(30), nullable=True)
    lastname: Mapped[str] = mapped_column(String(30), nullable=True)
    dateadd: Mapped[datetime] = mapped_column(DateTime, default = datetime.now())

    def get_id(self):
        return self.id