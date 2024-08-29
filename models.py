from sqlalchemy import String, DateTime, Boolean, ForeignKey
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

class task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    alarm: Mapped[bool] = mapped_column(Boolean, default=False)
    state: Mapped[bool] = mapped_column(Boolean, default=True)
    date_add: Mapped[datetime] = mapped_column(DateTime, default = datetime.now())
    date_end: Mapped[datetime] = mapped_column(DateTime)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    priority_id: Mapped[int] = mapped_column(ForeignKey('priorities.priority_id'))
    status_id: Mapped[int] = mapped_column(ForeignKey('status.id'))

class subtasks(Base):
    __tablename__ = 'subtasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id'))
    content: Mapped[str] = mapped_column(String(200), nullable=False)
    state: Mapped[bool] = mapped_column(Boolean, default=True)

class priorities(Base):
    __tablename__ = 'priorities'

    priority_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    priority: Mapped[str] = mapped_column(String(20), nullable=False)

class status(Base):
    __tablename__ = "status"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True)
    status: Mapped[String] = mapped_column(String(30), nullable=False)