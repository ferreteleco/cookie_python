from os import listdir
from os.path import join
from pathlib import Path
import shutil

import logging


def remove_pyenv_version_file():

    generate_pyenv_file = {{cookiecutter.generate_pyenv_file}}

    if generate_pyenv_file == False:
        LOG.info("Skipping .python-version file generation (pyenv) ...")
        path = Path("./.python-version")
        path.unlink()
"""Post-generate hook for cookiecutter."""

def remove_pyproject_file():

    generate_poetry_file = {{cookiecutter.generate_poetry_file}}

    if generate_poetry_file == False:
        LOG.info("Skipping pyproject.toml file generation (Poetry) ...")
        path = Path("./pyproject.toml")
        path.unlink()


def remove_vscode_project_files():

    vscode_project = {{cookiecutter.vscode_project}}

    if vscode_project == True:
        LOG.info("Generating .vscode folder (VSCode) with default tasks.json ...")
        vscode_files = join("_", "vscode")

        for file_or_folder in listdir(vscode_files):
        shutil.move(join(project_folder, file_or_folder), '.vscode')

    else:
        LOG.info("Skipping .vscode file generation (VSCode) ...")


def set_up_license():
    """Get license text and put it in project root."""
    license_type = "{{ cookiecutter.license }}"

    LOG.info("Moving %s license ...", license_type)
    license_file = join("_", "licenses", license_type)
    shutil.move(license_file, "./LICENSE")


def clean():
    """Remove files and folders only needed as input for generation."""
    LOG.info("Removing input data folder ...")
    shutil.rmtree("_")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    LOG = logging.getLogger("post_gen_project")

    remove_pyenv_version_file()
    remove_pyproject_file()
    remove_vscode_project_files()
    set_up_license()
    clean()
