from app.dto.response_dto import ResponseDTO
from app.model.main_model import MainModel
from common.status_enum import StatusEnum


class MainService:
    def __init__(self):
        self.main_model = MainModel()

        
    def get_datas(self):
        datas = self.main_model.select_datas()
        return ResponseDTO(status=StatusEnum.SUCCESS.value, data=datas)
