from http import HTTPStatus

from app.dto.main_dto import MainDto
from app.dto.response_dto import ResponseDTO
from app.dto.response_error_dto import get_error_schema
from app.service.main_service import MainService
from common.response_code import ResponseCode
from common.response_messages import RESPONSE_MESSAGES
from flask import jsonify, make_response
from flask_restx import Namespace, Resource

ns = Namespace("MAIN API")
path = "/"

main_dto = MainDto(ns)
main_response = main_dto.get_main_response()

main_service = MainService()

@ns.route('main', methods=['GET'])
class MainApi(Resource):
    @ns.expect()
    @ns.response(code=HTTPStatus.OK, description=RESPONSE_MESSAGES.get(ResponseCode.SUCCESS), model=main_response)
    @ns.response(code=HTTPStatus.INTERNAL_SERVER_ERROR, description=RESPONSE_MESSAGES.get(ResponseCode.SERVER_ERROR), model=ns.model('Error', get_error_schema(ResponseCode.SERVER_ERROR)))
    def get(self):
        try:
            response = main_service.get_datas()
            if response.code == ResponseCode.SUCCESS:
                return make_response(jsonify(response), HTTPStatus.OK)
            return make_response(jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            return make_response(jsonify(ResponseDTO(code=ResponseCode.SERVER_ERROR, message=str(e))), HTTPStatus.INTERNAL_SERVER_ERROR)
