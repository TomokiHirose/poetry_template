import pytest
from datetime import datetime, timedelta, timezone
from py.xml import html


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Description"))
    cells.insert(3, html.th("Time", class_="sortable time", col="time"))


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description, style="white-space:pre-wrap; word-wrap:break-word"))
    cells.insert(3, html.td(datetime.now(timezone(timedelta(hours=+9), "JST")).strftime("%Y/%m/%d %H:%M:%S"), class_="col-time"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = item.function.__doc__
