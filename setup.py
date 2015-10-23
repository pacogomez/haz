from setuptools import setup

setup(
    name='haz',
    version='1',
    py_modules=['haz'],
    include_package_data=True,
    install_requires=[
        'Click',
        # Colorama is only required for Windows.
        'colorama',
        'pyyaml',
    ],
    entry_points='''
        [console_scripts]
        haz=haz:cli
    ''',
)
