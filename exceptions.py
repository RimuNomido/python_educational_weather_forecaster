class CustomResponseError(Exception):
    """Исключение, вызываемое при status_code != 200"""
    def __init__(self, message: str, status_code: int):
        super().__init__(message)

        self.message = message
        self.status_code = status_code
    
    def __str__(self):
        return f"[Ошибка API] {self.message}"