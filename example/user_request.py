from dbrequest import AbstarctDBRequest
from dbrequest import IdField

from user_fields import *


class UserDBRequest(AbstarctDBRequest):
    def __init__(self) -> None:
        super().__init__()
        self._TABLE_NAME = 'users'
        self._FIELDS = (
            IdField(),
            UserUsernameField('username', str),
            UserLastMessageField('last_message', str, allowed_none=True)
        )

        