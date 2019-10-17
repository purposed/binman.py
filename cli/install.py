from .output import OutputManager


class Installer:
    def __init__(self, verbose: bool):
        self.log = OutputManager(verbose=verbose)

    def _validate_and_expand_path(self, name_or_path: str) -> str:
        if not name_or_path.startswith("github.com"):  # TODO: Support multiple hosts.
            if "/" in name_or_path:
                raise ValueError("Unsupported or incomplete path")
            self.log.debug(
                "No code host specified, assuming [github.com/purposed]"
            )  # TODO: Allow configuration of default host.
            name_or_path = f"github.com/purposed/{name_or_path}"

        return name_or_path

    def install(self, name_or_path: str, version: str) -> None:
        try:
            name_or_path = self._validate_and_expand_path(name_or_path)
            self.log.step(f"Installing from {name_or_path}@{version}")

        except Exception as e:
            self.log.error(f"{type(e).__name__}: {e}.")
