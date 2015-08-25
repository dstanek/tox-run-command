import copy

import tox.config
from tox import hookimpl


class FakeSectionReader(tox.config.SectionReader):
    """A hack to reuse the SectionReader logic to parse command lines."""

    def __init__(self):
        tox.config.SectionReader.__init__(self, None, None)

    def getargvlist(self, command):
        return tox.config._ArgvlistReader.getargvlist(self, command)


@hookimpl
def tox_addoption(parser):
    parser.add_argument('--run-command', help='run this command instead of configured commands')


@hookimpl
def tox_configure(config):
    alternative_cmd = config.option.run_command
    if alternative_cmd:
        reader = FakeSectionReader()
        alternative_cmd = FakeSectionReader().getargvlist(alternative_cmd)
        for env in config.envlist:
            # deepcopy is needed because tox updates the lists in place
            config.envconfigs[env].commands = copy.deepcopy(alternative_cmd)
