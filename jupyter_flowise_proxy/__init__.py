"""
Return config on servers to start for h2o-llm-studio

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_flowise():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "flowise.png"
        )

    # Make sure executable is in $PATH
    def _get_flowise_command(port):
        executable = "make"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find make executable in $PATH")
        # Create working directory
        home_dir = os.environ.get("HOME") or "/home/jovyan"
        working_dir = f"{home_dir}"
        os.chdir(working_dir)
        # Set environment variables
        return ["npx", "flowise", "start", "--PORT", f"{port}"]

    return {
        "command": _get_flowise_command,
        "timeout": 20,
        "launcher_entry": {
            "title": "flowise",
            "icon_path": _get_icon_path()
        },
        "absolute_url": True,
        "new_browser_tab": True,
    }
