# binman

![](https://img.shields.io/pypi/v/binman?style=flat-square) ![](https://img.shields.io/github/license/purposed/binman?style=flat-square)

Binman is a lightweight tool for installing binaries provided in Github releases.

## Configuration
Binman's configuration file is located at `~/.config/purposed/binman/config.json`.

| Setting | Type | Default Value | Description
|---------|------|---------------|------------
| `default_code_host` | String | `github.com/purposed` | Default github org to use when only an application name is provided.
| `install_location` | String | `~/bin` | Default location for the installed binaries.


## Usage

### Installing Software
```bash
$ binman [-v] install PACKAGE_PATH [VERSION]
```
This tool expects the releases to be named with a version number, and the binaries to be named along the following pattern: `{name}-{platform}-{architecture}`. When installing software, binman will detect your current platform & architecture, and select the correct binary.

By default, binman will put the binaries under `~/bin`.

### Updating Software
```bash
$ binman [-v] update PACKAGE_NAME [VERSION]...
```
For now, `binman update PACKAGE VERSION` is equivalent to 
`binman uninstall PACKAGE && binman install PACKAGE VERSION`.
In the future, we will improve the update mechanism so it takes into account the package version pre-update.

### Listing installed software
```
$ binman [-v] list
```

### Uninstalling software
```
$ binman [-v] uninstall [PACKAGE_NAME]
```
