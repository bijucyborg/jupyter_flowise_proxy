import setuptools
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-h2o-llm-studio-proxy",
    version='1.0dev',
    url="https://github.com/bijucyborg/jupyter_h2o-llm-studio_proxy",
    author="biju.krishnan@datasiens.ai",
    description="biju.krishnan@datasiens.ai",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=1.5.0'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'h2ollmstudio = jupyter_h2o-llm-studio_proxy:setup_h2ollmstudio',
        ]
    },
    package_data={
        'jupyter_h2o-llm-studio_proxy': ['icons/*'],
    },
)
