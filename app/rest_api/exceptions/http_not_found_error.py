from typing import Any, Dict
from fastapi import Request
from fastapi.responses import JSONResponse



class HTTPNotFoundError(Exception):
    def __init__(self, message: str|None = None) -> None:
        self.status_code = 404
        self.message = message



def http_not_found_exception_handler(request: Request, exc: HTTPNotFoundError):
    """
    Handler for error of JWT authorization
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
