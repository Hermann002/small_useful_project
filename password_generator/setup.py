from setuptools import setup, find_packages

setup(
    name="password_generator",
    version="0.2",
    packages=["password_generator"],
    entry_points={
        "console_scripts": [
            "generate-password=password_generator.main:main",
        ],
    },
)