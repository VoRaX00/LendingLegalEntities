from repositories.legal_user import LegalUserRepo
from schemas.legal_user import LegalUser
from models.legal_user import LegalUser as LegalUserModel
from service.exceptions.already_exists import AlreadyExistsException
from service.exceptions.internal_server import InternalServerException
from service.exceptions.not_found import NotFoundException




class LegalUserService:
    def __init__(self, repository: LegalUserRepo):
        self.repository = repository

    def create(self, user: LegalUser) -> LegalUser:
        exists_user = self.repository.get_by_inn(user.inn)
        if exists_user:
            raise AlreadyExistsException('User already exists')

        model = self.map_schemas_to_model(user)
        try:
            model = self.repository.create(model)
        except Exception as e:
            raise InternalServerException()
        return LegalUser.model_validate(model)

    def get_by_inn(self, inn: int) -> LegalUser:
        user = self.repository.get_by_inn(inn)
        if user is None:
            raise NotFoundException('User not found')
        return LegalUser.model_validate(user)

    @staticmethod
    def map_schemas_to_model(user: LegalUser) -> LegalUserModel:
        return LegalUserModel(
            inn=user.inn, name=user.name,
            type_activity=user.type_activity, contact_person=user.contact_person,
            address=user.address,
        )