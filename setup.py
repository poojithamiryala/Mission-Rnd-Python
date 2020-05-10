from setuptools import setup

setup(
    name="dumptoexcel.py",
    version='0.1',
    py_modules=['pca3'],
    install_requires=[
        'Click','openpyxl','beautifulsoup4'
    ],
    entry_points='''
        [console_scripts]
        dumptoexcel.py=pca3:cli
    ''',
)
