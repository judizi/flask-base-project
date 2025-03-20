from http import HTTPStatus

from app.dto.main_dto import MainDto
from app.dto.response_dto import ResponseDTO
from app.dto.response_error_dto import get_error_schema
from app.service.main_service import MainService
from common.status_enum import StatusEnum
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
    @ns.response(code=HTTPStatus.OK, model=[main_response], description="OK")
    @ns.response(code=HTTPStatus.INTERNAL_SERVER_ERROR, model=[ns.model('Error', get_error_schema(StatusEnum.FAIL.value))], description="INTERNAL_SERVER_ERROR")
    def get(self):
        try:
            response = main_service.get_datas()
            if response.status == StatusEnum.SUCCESS.value:
                return make_response(jsonify(response.to_dict()), HTTPStatus.OK)
            return make_response(jsonify(response.to_dict()), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            return make_response(jsonify(ResponseDTO(status=StatusEnum.FAIL.value, message=str(e)).to_dict()), HTTPStatus.INTERNAL_SERVER_ERROR)
