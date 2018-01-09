import requests
from configure import ProductionConfig
from utils.ansible_module.controller import AnsibleController
from utils.ansible_module.taskdefine.task import (CopyFile)

def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(ProductionConfig.LOCAL_PATCH_DIR + local_filename, 'w') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return 0
    else:
        return 1


def copy_check(filname, host):
    task = CopyFile(filename=filname)
    ansible = AnsibleController(host=host, task=[task.get_task()])
    data_result = ansible.__getitem__()
    return data_result


def copy_run(filname, host):
    task = CopyFile(filename=filname)
    ansible = AnsibleController(host=host, task=[task.get_task()])
    result = ansible.play_task()
    return result.return_data
