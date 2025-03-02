from setuptools import setup, find_packages

setup(
    name="gestion_depenses",
    version="0.1",
    packages=["gestion_depenses"],
    entry_points={
        "console_scripts": [
            "depense=gestion_depenses.main:main",
        ],
    },
)