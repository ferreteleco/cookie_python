# python_cookie

A [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template for python projects.

## Usage

In order to start a new project, [install Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html) and run the following command:

```bash
$ cookiecutter
```

## Variables

Variables allow to customize your project. When running the previous command, you will be prompted to fill in the following values:

- _**project_name**_: name of the project. This variable will also be used to create the default value for the project slug.
- _**project_slug**_: URL friendly name of the project. It is recommended to keep the default value.
- _**project_description**_: short description of the project.
- _**project_version**_: initial version of the project. If using a different value from the default, please follow [Semantic Versioning](https://semver.org/) recommendations.
- _**python_version**_: minimum required Python version in order to run the program.
- _**generate_pyenv_file**: flag to control generation of .python-version file (local Python version definition file for pyenv).
- _**generate_poetry_file**_: flag to control generation of pyproject.toml file (Poetry build system definition file).
- _**vscode_project**_: flag to control generation of .vscode folder, with default tasks.json file (VSCode text editor config file)
- _**full_name**_: full name of the main maintainer of the project.
- _**email**_: contact email of the main maintainer of the project.
- _**license**_: default license file for the project.

## Contributing

If you want to contribute to this template, feel free to do so! Create a new branch to work in, and open a pull request when you are done! It will be reviewed and merged into master by one of the maintainers as soon as possible.
