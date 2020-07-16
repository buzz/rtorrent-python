from setuptools import setup, find_packages

required_pkgs = []

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python3",
    "Topic :: Communications :: File Sharing",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="rtorrent-rpc",
    version="1.0.0-alpha",
    url="https://github.com/buzz/rtorrent-rpc",
    author="Chris Lucas",
    maintainer="buzz",
    description="A simple rTorrent interface written in Python3",
    keywords="rtorrent p2p",
    license="MIT",
    packages=find_packages(),
    scripts=[],
    install_requires=required_pkgs,
    classifiers=classifiers,
    include_package_data=True,
)
