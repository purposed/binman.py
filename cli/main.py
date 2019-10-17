from .install import Installer

from fire import Fire


class BinmanCLI:
    """
    Binary Application Manager.
    """

    def install(self, name_or_path: str, version: str = "latest", verbose: bool = False) -> None:
        """
        Install an application from a github URL or purposed package name.
        """
        ins = Installer(verbose=verbose)
        ins.install(name_or_path, version)


def main():
    Fire(BinmanCLI)
