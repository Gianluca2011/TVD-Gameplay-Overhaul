
"""
The Vampire Diaries Gameplay Overhaul
Initial script-mod bootstrap.
"""

import sims4
from sims4.log import Logger

LOGGER = Logger("TVD_Gameplay_Overhaul")
MOD_VERSION = "0.1.0"


def log_startup():
    """Write a startup message to the Sims 4 log."""
    LOGGER.info(
        "TVD Gameplay Overhaul v{} initialized.".format(
            MOD_VERSION
        )
    )


log_startup()

