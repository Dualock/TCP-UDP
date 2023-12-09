from setuptools import find_packages, setup

setup(
    name='code',
    packages=find_packages(include=['code']),
    version='0.0.1',
    description='TCP UDP Client and Server',
    author='Dualok Fonseca',
    license='MIT',
    install_requires=[
    	'socket',
        #'numpy',
        #'scipy',
        #'json',
        #'pandas',
        #'requests',
        #'statsmodels',
        #'matplotlib',
        #'mpl_toolkits',
        #'fitter',
        #'request'
    ],
)
