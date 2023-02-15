import logging
import typing

import flask

import tornium_extension.skynet.commands


class Extension:
    def __init__(
        self,
        app: typing.Optional[flask.Flask]=None,
        logger: typing.Optional[logging.Logger]=None
    ):
        if app is not None:
            self.init_app(app)

        if logger is None:
            self.logger = logging.getLogger("skynet")
            self.logger.setLevel(logging.DEBUG)
            handler = logging.FileHandler(filename="skynet.log", encoding="utf-8", mode="a")
            handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
            self.logger.addHandler(handler)
        else:
            self.logger = logger

        self.discord_enabled = True
        self.discord_commands = tornium_extension.skynet.commands.COMMANDS["active"]
        self.discord_buttons = tornium_extension.skynet.commands.BUTTONS["active"]

    def init_app(self, app: flask.Flask):
        import tornium_extension.flask_ext

        app.register_blueprint(tornium_extension.flask_ext.mod)

