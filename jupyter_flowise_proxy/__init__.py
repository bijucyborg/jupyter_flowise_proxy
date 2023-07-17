"""
Return config on servers to start for flowise.

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil
import logging
from urllib.parse import urlparse, urlunparse
import requests
from urllib.parse import urlparse, urlunparse

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")



def setup_flowise():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "flowise.svg"
        )

    # Make sure executable is in $PATH
    def _get_flowise_command(port):
        executable = "npx"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find npx executable in $PATH")
        # Create working directory
        home_dir = os.environ.get("HOME") or "/home/jovyan"
        working_dir = f"{home_dir}/Flowise"
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
            logger.info("Created directory %s" % working_dir)
        else:
            logger.info("Directory %s already exists" % working_dir)
        # Set environment variables
        os.chdir(working_dir)
        return ["yarn", "start", "--PORT", f"{port}"]
    

    return {
        'command': _get_flowise_command,
        'timeout': 20,
        'launcher_entry': {
            'title': 'flowise',
            'icon_path': _get_icon_path()
        },
        'absolute_url': False,
        'new_browser_tab': True,
        },
    }
