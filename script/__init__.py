import os
import toml
import logzero
from logzero import logger
from subprocess import check_call, call

formatter = logzero.LogFormatter(fmt="%(color)s[%(levelname)1.1s %(asctime)s]%(end_color)s %(message)s")
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


def api_document():
    opt = "-f" if os.path.exists(os.path.join("docs/api", "conf.py")) else "-F"
    call(["sphinx-apidoc", opt, "-M", "-e", "-o", "docs/api", PACKAGE_NAME])
    call(["make", "-C", "docs/api", "html"])


def test_document():
    opt = "-f" if os.path.exists(os.path.join("docs/test", "conf.py")) else "-F"
    call(["sphinx-apidoc", opt, "-M", "-e", "-o", "docs/test", "tests"])
    call(["make", "-C", "docs/test", "html"])


def metrics():
    logger.info("Analyze the given Python modules and compute Cyclomatic Complexity (CC).")
    call(["radon", "cc", "-s", PACKAGE_NAME])
    logger.info("Analyze the given Python modules and compute the Maintainability Index.")
    call(["radon", "mi", "-s", PACKAGE_NAME])
    logger.info("Analyze the given Python modules and compute raw metrics.")
    call(["radon", "raw", "-s", PACKAGE_NAME])


def test():
    logger.info("Running pytest...")
    call(["pytest", "--html=report.html", "--cov={}".format(PACKAGE_NAME), "--cov-branch"])
