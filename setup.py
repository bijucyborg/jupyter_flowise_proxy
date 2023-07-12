import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-flowise-proxy",
    version="0.2.0",
    url="https://github.com/bijucyborg/jupyter_flowise_proxy",
    author="DataSiens",
    description="info@datasiens.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["jupyter", "flowise", "jupyterhub", "jupyter-server-proxy"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        "jupyter-server-proxy>=1.5.0",
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "flowise = jupyter_flowise_proxy:setup_flowise",
        ]
    },
    package_data={
        "jupyter_flowise_proxy": ["icons/flowise.svg"],
    },
)