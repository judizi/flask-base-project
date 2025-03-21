from http import HTTPStatus

from app.dto.response_dto import ResponseDTO
from common.response_code import ResponseCode
from common.response_messages import RESPONSE_MESSAGES
from flask import jsonify, make_response
from flask_restx import fields


def get_error_response(e):
    return make_response(
        jsonify(ResponseDTO(code=ResponseCode.SERVER_ERROR, message=str(e))), 
        HTTPStatus.INTERNAL_SERVER_ERROR
    )


def get_error_schema(error_code):
    return {
        "code": fields.Integer(description="상태 코드", example=error_code),
        "message": fields.String(description="에러 메시지", example=RESPONSE_MESSAGES.get(error_code)),
    }
    