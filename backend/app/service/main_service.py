from app.dto.response_dto import ResponseDTO
from app.model.main_model import MainModel
from common.response_code import ResponseCode
from common.response_messages import RESPONSE_MESSAGES


class MainService:
    def __init__(self):
        self.main_model = MainModel()

        
    def get_datas(self):
        datas = self.main_model.select_datas()
        return ResponseDTO(code=ResponseCode.SUCCESS, message=RESPONSE_MESSAGES.get(ResponseCode.SUCCESS), data=datas)
