from fire import Fire

from .config import Config
from .install import Installer


class BinmanCLI:
    """
    Binary Application Manager.
    """

    def __init__(self) -> None:
        self._config = Config.load()

    def install(
        self, name_or_path: str, version: str = "latest", verbose: bool = False
    ) -> None:
        """
        Install an application from a github URL or purposed package name.
        """
        ins = Installer(
            code_host=self._config.default_code_host,
            install_location=self._config.install_location,
            verbose=verbose,
        )
        ins.install(name_or_path, version)


def main():
    Fire(BinmanCLI)
