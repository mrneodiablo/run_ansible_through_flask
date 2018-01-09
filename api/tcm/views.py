from api import app
from api.loggingformat import FormatLog
from api.responentity import ResponeEntity
from api.tcm.models import tcm_check, tcm_run
from utils.log_module.manager import LogManager
from flask import jsonify, request
from configure import ProductionConfig
from api.auth.authenapp import requires_auth, requires_content_type
import json




@app.route('/api/tcm', methods=['POST'])
@requires_auth
@requires_content_type
def tcm_api():
    __logging = LogManager("app").get_logger()
    __conf = ProductionConfig()

    # {'method': 'check', 'command': 'ls -las'}
    data = json.loads(request.data)
    if 'method' in [x for x in dict(data).iterkeys()] and 'command' in [x for x in dict(data).iterkeys()]:
        if data["method"] == "check":
            try:
                data_result = tcm_check(command=data["command"], host=__conf.HOST_TCM)
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="check tcm command " + data["command"], code=str(200),
                                       description=None, message=data_result).formatter()
                __logging.info(msg_result)
                return jsonify(ResponeEntity.return_ok(msg=None, data=data_result))
            except Exception as e:
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="exception check tcm command " + data["command"],
                                       description=None, code=str(5000), message=e.message).formatter()
                __logging.error(msg_result)
                return jsonify(ResponeEntity.return_exception(msg=e.message, data="exception check tcm command " + data[
                    "command"]))
        elif data["method"] == "run":
            try:
                data_result = tcm_run(command=data["command"], host=__conf.HOST_TCM)
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="check tcm command " + data["command"], code=str(200),
                                       description=None, message=data_result).formatter()
                __logging.info(msg_result)
                return jsonify(ResponeEntity.return_ok(msg=None, data=data_result))
            except Exception as e:
                msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url,
                                       name="exception check tcm command " + data["command"],
                                       description=None, code=str(5000), message=e.message).formatter()
                __logging.error(msg_result)
                return jsonify(ResponeEntity.return_exception(msg=e.message, data="exception check tcm command " + data[
                    "command"]))
        else:
            msg_result = FormatLog(remote_addr=request.remote_addr, base_url=request.base_url, code=str(5000),
                                   name="Method Wrong " ,
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


