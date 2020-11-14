import os
import toml
import logzero
from logzero import logger
from subprocess import check_call, call

formatter = logzero.LogFormatter(
    fmt="%(color)s[%(levelname)1.1s %(asctime)s]%(end_color)s %(message)s"
)
logzero.setup_default_logger(formatter=formatter)


with open("pyproject.toml") as f:
    conf = toml.load(f)
PACKAGE_NAME = conf["tool"]["poetry"]["name"]


def format():
    logger.info("Running isort...")
    call(["isort", PACKAGE_NAME])
    logger.info("Running black...")
    call(["black", PACKAGE_NAME])


def lint():
    logger.info("Running mypy...")
    call(["mypy", PACKAGE_NAME])
    logger.info("Running flake8...")
    call(["flake8", "template"])


def document():
    print("document")
    opt = "-f" if os.path.exists(os.path.join("docs", "conf.py")) else "-F"
    call(["sphinx-apidoc", opt, "-o", "docs", PACKAGE_NAME])
    #call(["make", "-C", "docs", "html"])