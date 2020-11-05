import logging
import re
import sys


def validate_project_slug():

    LOG.info("Validating repository name ...")

    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    project_slug = "{{ cookiecutter.project_slug }}"

    if not re.match(MODULE_REGEX, project_slug):
        print("ERROR: %s is not a valid Python module name!" % repo_name)

        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    LOG = logging.getLogger("pre_gen_project")

    validate_repo_name()
