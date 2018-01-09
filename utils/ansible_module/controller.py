from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory import Inventory
from ansible.vars import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play

from resulescollect import ResultsCollector
from options import OptionAnsible
from configure import ProductionConfig


class AnsibleController():

    __ansible_configure = ProductionConfig()
    __loader = DataLoader()
    __variable_manager = VariableManager()
    __options = OptionAnsible(
        become=__ansible_configure.ANSIBLE_CONFIG["become"],
        become_method=__ansible_configure.ANSIBLE_CONFIG["become_method"],
        become_user=__ansible_configure.ANSIBLE_CONFIG["become_user"],
        remote_user=__ansible_configure.ANSIBLE_CONFIG["remote_user"],
        private_key_file=__ansible_configure.ANSIBLE_CONFIG["private_key_file"],
        host_key_checking=False

    )

    def __init__(self, host, task, **kwargs):
        self.__tqm = None
        self.__tasks = task
        self.__host = host
        self.__inventory = Inventory(host_list=self.__host, loader=self.__loader,
                                     variable_manager=self.__variable_manager)


    def play_task(self):

        play_source = {"name": "app cfm", "hosts": "all", "gather_facts": "no", "tasks": self.__tasks}
        play = Play().load(play_source, variable_manager=self.__variable_manager, loader=self.__loader)
        data = self.__run(play)
        return data

    def __run(self, play):
        callback = ResultsCollector()

        try:
            self.__tqm = TaskQueueManager(
                inventory=self.__inventory,
                variable_manager=self.__variable_manager,
                loader=self.__loader,
                options=self.__options,
                stdout_callback=callback,
                passwords=None,
                run_tree=False,
            )

            self.__tqm.run(play)
            return callback
        finally:
            if self.__tqm is not None:
                self.__tqm.cleanup()

    def __getitem__(self):
        list_hosts = self.__host
        list_tasks = self.__tasks
        return {"hosts": list_hosts, "tasks": list_tasks}