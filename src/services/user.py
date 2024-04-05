from ..database import db
from ..utils import Res

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