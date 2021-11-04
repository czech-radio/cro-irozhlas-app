
from setuptools import setup


if __name__ == "__main__":

    setup(
        name="geneea-demo",
        version="0.2.0",
        install_requires = [
            "requests"
        ],
        entry_points = {
            'console_scripts': ['geneea=main:analyze'],
        }
    )