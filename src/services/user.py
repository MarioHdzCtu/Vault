from ..database import db
from ..utils import Res, logger
from ..models import User
import bcrypt

class UserService:

    def __init__(self) -> None:
        pass

    def get_user(self, user_id: int | None = None):
        user_query = "WHERE id = ?" if user_id is not None else ''
        query = f"SELECT * FROM vault.users {user_query}"
        vals = (user_id,) if user_id is not None else tuple()
        with db as conn:
            res = conn.select(query=query, vals=vals)

        if res == []:
            d = {
                'msg':  f'No user was found with id {user_id}',
                'data': None,
                'status_code': 204
            }
            return Res(**d)
        d = {
                'msg':  f'Found {len(res)} {"user" if len(res) == 1 else "users"}',
                'data': res,
                'status_code': 200
            }
        return Res(**d)
    
    def create_user(self, username: str, password: str, recovery_email: str | None = None):
        logger.info(f'Creating new user with username {username}')
        query = "INSERT INTO vault.users(username, password, recovery_email, salt) VALUES(?,?,?,?)"
        salt = bcrypt.gensalt()
        hashed_psw = bcrypt.hashpw(password=password.encode('utf-8'),salt=salt)
        vals = (username.lower(), hashed_psw, recovery_email.lower(), salt)
        with db as conn:
           rows = conn.insert(query=query, data=vals)
        if rows != 1:
            d = {
                'msg':  f'An error occured when creating user {username}',
                'data': rows,
                'status_code': 409
            }
            logger.error(f'{d["msg"]}. {rows}')
            return Res(**d)
        else:
            d = {
                'msg':  f'Created user {username}',
                'data': rows,
                'status_code': 200
            }
            logger.info(d['msg'])
            return Res(**d)