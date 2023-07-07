import setuptools

setuptools.setup(
    name="jupyter-h2o-llm-studio-proxy",
    version='1.0dev',
    url="https://github.com/jupyterhub/jupyter-server-proxy/tree/HEAD/contrib/h2o-llm-studio",
    author="biju.krishnan@datasiens.ai",
    description="biju.krishnan@datasiens.ai",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'h2o-llm-studio = jupyter_h2o-llm-studio_proxy:setup_h2o-llm-studio',
        ]
    },
    package_data={
        'jupyter_h2o-llm-studio_proxy': ['icons/*'],
    },
)
