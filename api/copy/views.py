from api import app
from api.loggingformat import FormatLog
from api.responentity import ResponeEntity
from utils.log_module.manager import LogManager
from flask import jsonify, request
from configure import ProductionConfig
from api.auth.authenapp import requires_auth, requires_content_type
import json
from models import download_file, copy_check, copy_run

@app.route('/api/get_patch', methods=['POST'])
@requires_auth
@requires_content_type
def get_patch():
    __logging = LogManager("app").get_logger()

    # {'method': 'download', 'url': ' cfm.ffddd.vn.tar.gz'}
    data = json.loads(request.data)

    # check request body
    if 'method' in [x for x in dict(data).iterkeys()] and 'url' in [x for x in dict(data).iterkeys()]:
        if data["method"] == "download":
            try:
                data_result = download_file(data["url"])
                if data_result == 0:
                    #download done
                    msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                           name="download patch " + data["url"], code=str(200),
                                           description="download ok", message=data_result).formatter()
                    __logging.info(msg_result)
                    return jsonify(ResponeEntity.return_ok(msg=msg_result, data="ok"))
                else:
                    # file not found
                    msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                           name="download patch " + data["url"], code=str(201),
                                           description="file not found", message=data_result).formatter()
                    __logging.error(msg_result)
                    return jsonify(ResponeEntity.return_error(msg=msg_result, data="file not found"))
            except Exception as e:
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="download patch " + data["url"],
                                       description=e.message, code=str(5000), message=e.message).formatter()
                __logging.error(msg_result)
                return jsonify(ResponeEntity.return_exception(msg=msg_result, data="exception download patch " + data[
                    "url"]))
        else:
            msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=str(5000),
                                   name="Method Wrong ",
                                   description=None, message="dkmm ngu vai noi").formatter()
            __logging.error(msg_result)
            return jsonify(ResponeEntity.return_error(msg=msg_result, data="Method Wrong Format"))
    else:

        msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=str(5000), name="Data "
                                                                                                                "Wrong " \
                                                                                                                "Format",
                               description=None, message="dkmm ngu vai noi").formatter()
        __logging.error(msg_result)
        return jsonify(ResponeEntity.return_error(msg=msg_result, data="Data Wrong Format"))


@app.route('/api/copy', methods=['POST'])
@requires_auth
@requires_content_type
def copy_api():
    __logging = LogManager("app").get_logger()
    __conf = ProductionConfig()

    # {'method': 'check', 'filename': 'cfm.ssff.tar.gz'}
    data = json.loads(request.data)
    if 'method' in [x for x in dict(data).iterkeys()] and 'filename' in [x for x in dict(data).iterkeys()]:
        if data["method"] == "check":
            try:
                data_result = copy_check(filname=data["filename"], host=__conf.HOST_GAME)
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="check copy file " + data["filename"], code=str(200),
                                       description=None, message=data_result).formatter()
                __logging.info(msg_result)
                return jsonify(ResponeEntity.return_ok(msg=None, data=data_result))
            except Exception as e:
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="exception copy file " + data["filename"],
                                       description=None, code=str(5000), message=e.message).formatter()
                __logging.error(msg_result)
                return jsonify(ResponeEntity.return_exception(msg=e.message, data="exception copy file " + data[
                    "filename"]))

        elif data["method"] == "run":
            try:
                data_result = copy_run(filname=data["filename"], host=__conf.HOST_GAME)
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="copy file " + data["filename"], code=str(200),
                                       description=None, message=data_result).formatter()
                __logging.info(msg_result)
                return jsonify(ResponeEntity.return_ok(msg=None, data=data_result))
            except Exception as e:
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="exception copy file " + data["filename"],
                                       description=None, code=str(5000), message=e.message).formatter()
                __logging.error(msg_result)
                return jsonify(ResponeEntity.return_exception(msg=e.message, data="exception filename" + data[
                    "filename"]))
        else:
            msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=str(5000),
                                   name="Method Wrong ",
                                   description=None, message="dkmm ngu vai noi").formatter()
            __logging.error(msg_result)
            return jsonify(ResponeEntity.return_error(msg=msg_result, data="Method Wrong Format"))
    else:

        msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=str(5000), name="Data "
                                                                                                                "Wrong " \
                                                                                                                "Format",
                               description=None, message="dkmm ngu vai noi").formatter()
        __logging.error(msg_result)
        return jsonify(ResponeEntity.return_error(msg=msg_result, data="Data Wrong Format"))

