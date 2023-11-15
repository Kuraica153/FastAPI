from fastapi import HTTPException
from loguru import logger
import inspect

class AppExceptionCase(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

class AppException():

    class BadRequest(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=400, detail=detail)
            logger.error(f"Status code {400}: {detail} | caller={caller_info()}")

    class Unauthorized(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=401, detail=detail)
            logger.error(f"Status code {401}: {detail} | caller={caller_info()}")

    class Forbidden(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=403, detail=detail)
            logger.error(f"Status code {403}: {detail} | caller={caller_info()}")

    class NotFound(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=404, detail=detail)
            logger.error(f"Status code {404}: {detail} | caller={caller_info()}")

    class Conflict(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=409, detail=detail)
            logger.error(f"Status code {409}: {detail} | caller={caller_info()}")

    class UnprocessableEntity(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=422, detail=detail)
            logger.error(f"Status code {422}: {detail} | caller={caller_info()}")

    class InternalServerError(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=500, detail=detail)
            logger.error(f"Status code {500}: {detail} | caller={caller_info()}")

    class NotImplemented(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=501, detail=detail)
            logger.error(f"Status code {501}: {detail} | caller={caller_info()}")

    class ServiceUnavailable(AppExceptionCase):
        def __init__(self, detail: str):
            super().__init__(status_code=503, detail=detail)
            logger.error(f"Status code {503}: {detail} | caller={caller_info()}")

def caller_info() -> str:
    info = inspect.getframeinfo(inspect.stack()[2][0])
    return f"{info.filename}:{info.lineno}:{info.function}"