from entities import AuthData
from .datamodels.filters import AuthDataFilter
from .abstracts import AuthDataRepo, IJWTManager
from .exceptions import IncorrectValueException, NotFoundException
from hashlib import md5



class AuthUseCases():
    def __init__(self, repo: AuthDataRepo, jwt_manager: IJWTManager) -> None:
        self.__repo: AuthDataRepo = repo
        self.__jwt_manager: IJWTManager = jwt_manager


    def __hash(self, string: str):
        return md5(string.encode()).hexdigest()


    async def get_jwt_by_logpass(self, login: str, password: str) -> list[str]:
        auth_data = await self.__repo.get(filter=AuthDataFilter(login=login))

        if len(auth_data) == 0:
            raise NotFoundException(msg='User not found')
        else:
            auth_data = auth_data[0]
        
        if auth_data.password_hash != self.__hash(password):
            raise IncorrectValueException(msg='Incorrect password')
        
        user_id = auth_data.user_id
        access_t = self.__jwt_manager.create_access_token(sub=user_id.hex)
        refresh_t = self.__jwt_manager.create_refresh_token(sub=user_id.hex)

        return access_t, refresh_t


    async def refresh_jwt(self, refresh_token: str) -> list[str]:
        user_id = self.__jwt_manager.get_jwt_subject(refresh_token)

        access_t = self.__jwt_manager.create_access_token(sub=user_id)
        refresh_t = self.__jwt_manager.create_refresh_token(sub=user_id)

        return access_t, refresh_t


