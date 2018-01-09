from utils.ansible_module.controller import AnsibleController
from utils.ansible_module.taskdefine.task import (ExecTCM)

def tcm_check(command, host):
    task = ExecTCM(command=command)
    ansible = AnsibleController(host=host, task=[task.get_task()])
    data_result = ansible.__getitem__()
    return data_result


def tcm_run(command, host):
    task = ExecTCM(command=command)
    ansible = AnsibleController(host=host, task=[task.get_task()])
    result = ansible.play_task()
    return result.return_data