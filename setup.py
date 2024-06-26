from setuptools import setup, find_packages

setup(
    name='redcsv2xlsx',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'redcsv2xlsx=csv2xlsx.csv2xlsx:main',
        ],
    },
    install_requires=[
        'pandas',
        'openpyxl'
    ],
    python_requires='>=3.6',
    description='Convert multiple CSV files into a single XLSX file with each CSV as a separate sheet.',
    author='RedBready',
    author_email='RedBready'
)
