# Copyright (C) tiksan - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by tiksan <webmaster@deek.sh>

import click
from flask import Blueprint


mod = Blueprint("tornium_extension_cli", __name__)

@mod.cli.command("test")
def test_command():
    """Test"""
    click.echo("test")
