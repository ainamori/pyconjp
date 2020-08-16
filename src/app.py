#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import os
import sys
from logging import DEBUG, StreamHandler, basicConfig, getLogger

import click
import connexion
from flask_cors import CORS

logger = getLogger(__name__)
handler = StreamHandler()
logger.addHandler(handler)
logger.propagate = False
sys.path.append(os.path.join(os.path.dirname(__file__), 'api'))


class PyConJP:

    def __init__(self):
        self.swagger = 'config/swagger.yml'

    @classmethod
    def url_top(cls):
        return 'OK', 200

    def run_server(self):
        app = connexion.FlaskApp(__name__)
        app.add_api('config/swagger.yml')
        CORS(app.app)
        app.run(port=8000, host="0.0.0.0")


def _set_loglevel(debug):
    if debug:
        log_level = DEBUG
        click.echo(click.style("Debug ON", fg="yellow"))
    else:
        log_level = getLogger().getEffectiveLevel()
    basicConfig(
        level=log_level,
        format='[%(asctime)s] %(name)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


@click.command()
@click.option('--debug/--no-debug', help='Debug mode (default: False)')
def cmd(debug=False):
    _set_loglevel(debug)
    app = PyConJP()
    app.run_server()


def main():
    cmd()


if __name__ == '__main__':
    main()
