from api import app
from utils.log_module.manager import LogManager
from flask import jsonify,request
from api.responentity import ResponeEntity
from api.loggingformat import FormatLog


@app.errorhandler(404)
def page_not_found(e):
    write_log = LogManager("app").get_logger()
    msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=e.code,  name=e.name,
                           description=e.description, message=e.message).formatter()
    write_log.error(msg_result)
    return jsonify(ResponeEntity.return_error(data=e.name,msg=msg_result))


@app.errorhandler(500)
def server_error(e):
    write_log = LogManager("app").get_logger()
    msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code = e.code, name=e.name,
                           description=e.description, message=e.message).formatter()
    write_log.error(msg_result)
    return jsonify(ResponeEntity.return_error(data=e.name,msg=msg_result))


@app.errorhandler(403)
def server_error(e):
    write_log = LogManager("app").get_logger()
    msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=e.code, name=e.name,
                           description=e.description, message=e.message).formatter()
    write_log.error(msg_result)
    return jsonify(ResponeEntity.return_error(data=e.name,msg=msg_result))


@app.errorhandler(405)
def server_error(e):
    write_log = LogManager("app").get_logger()
    msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=e.code, name=e.name,
                           description=e.description, message=e.message).formatter()
    write_log.error(msg_result)
    return jsonify(ResponeEntity.return_error(data=e.name, msg=msg_result))

def request_not_authen():
    write_log = LogManager("app").get_logger()
    msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=str(5000),
                           name="Authentication "
                                                                                                    "Failed",
                           description=None, message="dkmm ngu vai noi set authen vao").formatter()
    write_log.error(msg_result)
    return jsonify(ResponeEntity.return_error(msg=msg_result, data="Authentication Failed"))

def request_content_type_wrong():
    write_log = LogManager("app").get_logger()
    msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=str(5000), name="Content-Typer Wrong",
                           description=None, message="dkmm ngu vai noi set content-type=json").formatter()
    write_log.error(msg_result)
    return jsonify(ResponeEntity.return_error(msg=msg_result, data="Content-Typer Wrong"))
