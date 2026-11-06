import logging
import signal
from threading import Event

from app.config import get_settings

logger = logging.getLogger("quickconnect.worker")


def main() -> None:
    """Run the worker process until it receives a shutdown signal.

    Notification and scheduled-job handlers will be added in a later step.
    """
    settings = get_settings()
    logging.basicConfig(
        level=settings.log_level.upper(),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    shutdown = Event()

    def request_shutdown(_signum: int, _frame: object) -> None:
        shutdown.set()

    signal.signal(signal.SIGINT, request_shutdown)
    signal.signal(signal.SIGTERM, request_shutdown)
    logger.info("QuickConnect worker skeleton started; no jobs are registered")

    while not shutdown.wait(timeout=60):
        continue

    logger.info("QuickConnect worker stopped")


if __name__ == "__main__":
    main()
