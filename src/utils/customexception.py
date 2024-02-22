
class CustomException(Exception):
    def __init__(self, message):
        print(f"[CustomException] :: {message}")
        super().__init__(message)
