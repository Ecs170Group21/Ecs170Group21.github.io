from setuptools import setup, find_packages

setup(
    name='tumordetector',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.0.3',
        'tensorflow==2.16.1',
        'blinker==1.8.2',
        'click==8.1.7',
        'itsdangerous==2.2.0',
        'Jinja2==3.1.4',
        'MarkupSafe==2.1.5',
        'Werkzeug==3.0.3',
    ],
)
