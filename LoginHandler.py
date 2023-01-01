from User import User, Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, Query


class LoginHandler:
    def __init__(self):
        self.engine = create_engine("sqlite:///C:\\Users\\lob55\\PycharmProjects\\pythonProject\\db\\pskk_db", echo=True, future=True)

        session = Session(self.engine)
        session.execute("DROP TABLE IF EXISTS user;")
        session.commit()
        session.close()

        Base.metadata.create_all(self.engine)

    def create_user(self, user: User) -> bool:
        session = Session(self.engine)

        session.add(user)

        session.commit()
        session.close()

        return True

    def get_user_by_username_and_password(self, user: User) -> User:

        session = Session(self.engine)

        query = select(User).where((User.username == user.username) & (User.password == user.password))

        user_return = session.execute(query).one_or_none()

        session.close()

        if user_return:
            return user_return[0]

        return user_return
    
    def get_user_by_id(self, id: int) -> User:
        session = Session(self.engine)

        query = select(User).where(User.id == id)

        user_return = session.execute(query).one_or_none()

        session.close()

        if user_return:
            return user_return[0]

        return user_return


    def add_test_users(self):
        user = User("admin", "admin")
        self.create_user(user)
