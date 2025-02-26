from setuptools import setup, find_packages

setup(
    name="my_ai_app_builder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        "console_scripts": [
            "my_ai_app_builder=src.main:main",
        ],
    },
)
