import logging
from pathlib import Path
from datetime import datetime
from venv import logger


def setup_log(name):
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)

    lgger = logging.getLogger()
    lgger.setLevel(logging.DEBUG)

    time_stamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    file_handler = logging.FileHandler("logs/Sanity_Test_log_{}".format(time_stamp))
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s]:%(lineno)d %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S"
                                  )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    if not lgger.handlers:
        lgger.addHandler(file_handler)
        lgger.addHandler(console_handler)

    return logger