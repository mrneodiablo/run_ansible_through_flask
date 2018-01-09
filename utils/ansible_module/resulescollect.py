from ansible.plugins.callback import CallbackBase

class ResultsCollector(CallbackBase):

    def __init__(self, *args, **kwargs):
        super(ResultsCollector, self).__init__(*args, **kwargs)
        self.return_data = []

    def _command_generic_msg(self, host, task, result, changed, status):

        data = {
            'host': host,
            'changed': changed,
            'task': task,
            'status': status,
            'rc': result.get('rc', 0),
            'stdout': result.get('stdout', ''),
            'stderr': result.get('stderr', ''),
            'start': result.get('start', ''),
            'end': result.get('end', ''),
            'msg': result.get('msg', ''),
            'result': result
        }

        return data

    def v2_runner_on_unreachable(self, result, ignore_errors=False):
        name = result._host.get_name()
        task = result._task.get_name()

        # return data
        self.return_data.append(
            self._command_generic_msg(host=name, task=task, result=result._result, changed=result._result['changed'],
                                      status="unreachable"))

    def v2_runner_on_ok(self, result, *args, **kwargs):

        name = result._host.get_name()
        task = result._task.get_name()
        if task == "setup":
            self.return_data.append(self._command_generic_msg(host=name, task=task, result=result._result,
                                                              changed=result._result['changed'], status="ok"))
        else:
            self.return_data.append(self._command_generic_msg(host=name, task=task, result=result._result,
                                                              changed=result._result['changed'], status="ok"))

    def v2_runner_on_failed(self, result, *args, **kwargs):
        name = result._host.get_name()
        task = result._task.get_name()
        self.return_data.append(
            self._command_generic_msg(host=name, task=task, result=result._result, changed=result._result['changed'],
                                      status="failed"))

    def v2_runner_on_skipped(self, result):
        name = result._host.get_name()
        task = result._task.get_name()
        self.return_data.append(
            self._command_generic_msg(host=name, task=task, result=result._result, changed=result._result['changed'],
                                      status="skipped"))

    def v2_on_file_diff(self, result):
        pass

    def v2_playbook_on_play_start(self, play):
        pass

    def v2_playbook_on_task_start(self, task, is_conditional):
        pass

    def v2_playbook_on_stats(self, stats):
        pass


