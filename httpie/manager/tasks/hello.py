import argparse
from httpie.context import Environment
from httpie.status import ExitStatus


def cli_hello(env: Environment, args: argparse.Namespace) -> ExitStatus:
    env.stdout.write('Hello from HTTPie!\n')
    return ExitStatus.SUCCESS
