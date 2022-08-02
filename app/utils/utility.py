from flask import request


def get_lang_code():
    return request.args.get('lang_code', "eng")
