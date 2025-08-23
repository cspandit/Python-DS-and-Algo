import pytest
from pathlib import Path
from datetime import datetime

report_folder = Path("../../Z_Exercise/Report")
report_folder.mkdir(exist_ok=True)

date_format = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
file_name = "Sanity_test_report_{}.html".format(date_format)

pytest_args = [
    "/Users/shekharpandit/PycharmProjects/Python-DS-and-Algo_new/Z_Exercise",  # Specify the test directory
    "--html=" + file_name,
    "--self-contained-html", # to include html and css for test report
    "--capture=tee-sys",
    "-v"  # Increase verbosity
]


pytest.main(pytest_args)