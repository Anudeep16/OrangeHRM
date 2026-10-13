import logging
from pathlib import Path


def get_logger(name):
    base_logger = logging.getLogger("orangehrm")
    base_logger.setLevel(logging.INFO)
    base_logger.propagate = False

    if not base_logger.handlers:
        log_path = Path(__file__).resolve().parent.parent / "logs" / "automation.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(log_path, encoding="utf-8")
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )
        )
        base_logger.addHandler(handler)

    return logging.getLogger(f"orangehrm.{name}")
