# -*- coding: utf-8 -*-
from flask_restx import Resource
from app.config.exceptions import InvalidDataException
from flask import request


def get_lang_code():
    return request.args.get("lang_code", "en")


class BaseResource(Resource):

    @classmethod
    def parse_int(cls, **kwargs):
        """ Validates the pagination request params """

        key = kwargs.get("key", None)
        if key is None:
            raise InvalidDataException(message="key not found")

        value = request.args.get(key)
        if value is None:
            return None
        try:
            return int(value)
        except Exception as ex:
            raise InvalidDataException(message="invalid arg value")

    @classmethod
    def parse_float(cls, **kwargs):
        """ Validates the pagination request params """

        key = kwargs.get("key", None)
        if key is None:
            raise InvalidDataException(message="key not found")

        value = request.args.get(key)
        if value is None:
            return None

        try:
            return float(value)
        except Exception as ex:
            raise InvalidDataException(message="invalid arg value")

    @classmethod
    def get_pagination_params(cls):
        """
            Generates the pagination params
            Args:
                page(int): page number
                limit(int): maximun number of items per page

            Returns:
                dict: page and limit data
        """
        page = request.args.get('page')
        limit = request.args.get('limit')
        # cls._validate_pagination_args(page=page, limit=limit)

        if page is None:
            page = 1

        if limit is None:
            limit = 10

        return int(page), int(limit)

    @classmethod
    def paginate_resource(cls, query):
        """
            Paginate the given resource
            Args:
                query: resource model query

            Returns:
                dict: paginated data and metadata
        """

        page, limit = cls.get_pagination_params()

        records_query = query.paginate(page=page, max_per_page=limit)
        current_page_num = records_query.page
        pages_count = records_query.pages
        total_count = records_query.total
        meta = {
            'page': current_page_num,
            'pages_count': pages_count,
            'total_count': total_count
        }

        return records_query.items, meta

    @classmethod
    def response_success(cls, data=None, message=None, code=200):
        success_response = {
            'status': 'success',
            "message": ""
        }

        if data:
            success_response["result"] = data

        if message:
            success_response["message"] = message

        return success_response, code
