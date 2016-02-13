import os
from subprocess import Popen, PIPE
from unittest import TestCase

example_directory = os.path.join(
    os.path.dirname(__file__),
    'example_tox_config')


class TestEnvironmentsAreCorrect(TestCase):
    def test_environment_py_27_1(self):
        command_args = [
            'tox', '-e', 'py27-1', '--run-command',
            'echo "Current environment: {envname}"']
        process = Popen(command_args, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                        cwd=example_directory)
        stdout, stderr = process.communicate()
        self.assertIn("Current environment: py27-1", stdout)
        self.assertNotIn("Current environment: py27-2", stdout)

    def test_environment_py_27_2(self):
        command_args = [
            'tox', '-e', 'py27-2', '--run-command',
            'echo "Current environment: {envname}"']
        process = Popen(command_args, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                        cwd=example_directory)
        stdout, stderr = process.communicate()
        self.assertNotIn("Current environment: py27-1", stdout)
        self.assertIn("Current environment: py27-2", stdout)

    def test_environment_py_27_all(self):
        command_args = [
            'tox', '--run-command', 'echo "Current environment: {envname}"']
        process = Popen(command_args, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                        cwd=example_directory)
        stdout, stderr = process.communicate()
        self.assertIn("Current environment: py27-1", stdout)
        self.assertIn("Current environment: py27-2", stdout)
