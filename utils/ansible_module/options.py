
class OptionAnsible(object):

    def __init__(self, module_path=None, forks=None, become=False, listhosts=None, listtasks=None, listtags=None,
                 verbosity=None, subset=None, extra_vars=None, ask_vault_pass=None,
                 vault_password_files=None, new_vault_password_file=None, output_file=None, tags=None,
                 skip_tags=None, one_line=None, tree=None, ask_sudo_pass=None, ask_su_pass=None, sudo=None,
                 sudo_user=None, ask_pass=None, private_key_file=None, poll_interval=None, seconds=None, check=False,
                 syntax=None, diff=None, force_handlers=None, flush_cache=None, become_method=None, become_user='root',
                 remote_user='root', connection='smart', timeout=300, host_key_checking=False):

        self.forks = forks
        self.remote_user = remote_user
        self.connection = connection
        self.timeout = timeout
        self.module_path = module_path
        self.become = become
        self.become_method = become_method
        self.become_user = become_user
        self.check = check
        self.listhosts = listhosts
        self.listtasks = listtasks
        self.listtags = listtags
        self.verbosity = verbosity
        self.subset = subset
        self.extra_vars = extra_vars
        self.ask_vault_pass = ask_vault_pass
        self.vault_password_files = vault_password_files
        self.new_vault_password_file = new_vault_password_file
        self.output_file = output_file
        self.tags = tags
        self.skip_tags = skip_tags
        self.one_line = one_line
        self.tree = tree
        self.ask_sudo_pass = ask_sudo_pass
        self.ask_su_pass = ask_su_pass
        self.sudo = sudo
        self.sudo_user = sudo_user
        self.ask_pass = ask_pass
        self.private_key_file = private_key_file
        self.poll_interval = poll_interval
        self.seconds = seconds
        self.check = check
        self.syntax = syntax
        self.diff = diff
        self.force_handlers = force_handlers
        self.flush_cache = flush_cache
        self.host_key_checking = host_key_checking
