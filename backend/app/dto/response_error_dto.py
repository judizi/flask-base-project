from common.response_messages import RESPONSE_MESSAGES
from flask_restx import fields


def get_error_schema(error_code):
    return {
        "code": fields.Integer(description="상태 코드", example=error_code),
        "message": fields.String(description="에러 메시지", example=RESPONSE_MESSAGES.get(error_code)),
    }
    