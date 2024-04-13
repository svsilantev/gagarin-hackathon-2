class BotException(Exception):
    pass

class UserDoesNotExist(BotException):
    def __init__(self, user: str) -> None:
        msg = f"User {user} does not exist."
        super().__init__(msg)

class InternalError(BotException):
    def __init__(self, error: Exception) -> None:
        msg = f"Internal Error: {error}"
        super().__init__(msg)