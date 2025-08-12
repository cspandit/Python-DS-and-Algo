import pytest
from pathlib import Path
from datetime import datetime

report_dir = Path('Reports')
report_dir.mkdir(exist_ok=True)
time_stamp = datetime.now().strftime("%Y-%m-%d_%H:%H:%S")
file_name = 'Reports/Sanity_Test_Report_{}.html'.format(time_stamp)

pytest.main([
    ".",
    "--html="+file_name,
    "--self-contained-html",
    #"--report-title="+"Automated Sanity Test Report",
    "--capture=tee-sys"
])
