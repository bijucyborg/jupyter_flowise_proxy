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


def setup_h2ollmstudio():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "logo.svg"
        )

    # Make sure executable is in $PATH
    def _get_h2ollmstudio_command(port):
        executable = "make"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find make executable in $PATH")
        # Create working directory
        home_dir = os.environ.get("HOME") or "/home/jovyan"
        working_dir = f"{home_dir}/h2o-llmstudio"
        os.chdir(working_dir)
        # Set environment variables
        os.environ["H2O_WAVE_MAX_REQUEST_SIZE"] = "25MB"
        os.environ["H2O_WAVE_NO_LOG"] = "true"
        os.environ["H2O_WAVE_PRIVATE_DIR"] = "/download/@output/download"
        os.environ["H2O_WAVE_LISTEN"] = f":{port}"
        os.environ["H2O_WAVE_ADDRESS"] = f"http://127.0.0.1:{port}/h2ollmstudio/"
        os.environ["H2O_WAVE_BASE_URL"] = "/h2ollmstudio/"
        return ["make", "wave"]

    return {
        "command": _get_h2ollmstudio_command,
        "timeout": 20,
        "launcher_entry": {
            "title": "h2ollmstudio",
            "icon_path": _get_icon_path()
        },
        "new_browser_tab": True,
    }
