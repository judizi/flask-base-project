from common.response_code import ResponseCode
from common.response_messages import RESPONSE_MESSAGES
from flask_restx import Namespace, fields


class MainDto:
    def __init__(self, ns: Namespace):
        self.ns = ns


    def get_main_response(self):
        item_model = self.ns.model('Item', {})
        return self.ns.model("main_response", model={
            "code": fields.Integer(description="응답 코드", example=ResponseCode.SUCCESS),
            "message": fields.String(description="메시지", example=RESPONSE_MESSAGES.get(ResponseCode.SUCCESS)),
            "data": fields.List(fields.Nested(item_model), description='응답 리스트'),
        })

    