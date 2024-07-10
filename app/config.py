import os
from dotenv import dotenv_values

if os.path.exists('.env'):
    __values = dotenv_values(".env")
else:
    __values = os.environ
    print(__values)


SERVER_NAME = __values["SERVER_NAME"]
DATABASE_URL = __values["DATABASE_URL"]
JSON_DB_PATH = __values["JSON_DB_PATH"]
JWT_SECRET_KEY = __values["JWT_SECRET_KEY"]
FILE_STORAGE=__values["FILE_STORAGE"]
HOST=__values["HOST"]
PORT=int(__values["PORT"])
USER_TAG_PREFIX=__values["USER_TAG_PREFIX"]