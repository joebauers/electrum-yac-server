from setuptools import setup

setup(
    name="electrum-yac-server",
    version="1.0",
    scripts=['run_electrum_yac_server.py','electrum-yac-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumyacserver':'src'
        },
    py_modules=[
        'electrumyacserver.__init__',
        'electrumyacserver.utils',
        'electrumyacserver.storage',
        'electrumyacserver.deserialize',
        'electrumyacserver.networks',
        'electrumyacserver.blockchain_processor',
        'electrumyacserver.server_processor',
        'electrumyacserver.processor',
        'electrumyacserver.version',
        'electrumyacserver.ircthread',
        'electrumyacserver.stratum_tcp'
    ],
    description="Yacoin Electrum Server",
    author="JB",
    author_email="dev@devnull",
    license="MIT Licence",
    url="https://github.com/joe_bauers/electrum-yac-server/",
    long_description="""Server for the Electrum Lightweight Litecoin Wallet"""
)
