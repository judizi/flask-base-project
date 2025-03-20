from common.status_enum import StatusEnum
from flask_restx import Namespace, fields


class MainDto:
    def __init__(self, ns: Namespace):
        self.ns = ns


    def get_main_response(self):
        item_model = self.ns.model('Item', {})
        return self.ns.model("main_response", model={
            "status": fields.String(description="응답 코드", example=StatusEnum.SUCCESS.value),
            "message": fields.String(description="메시지", example=None),
            "data": fields.List(fields.Nested(item_model), description='응답 리스트'),
        })

    