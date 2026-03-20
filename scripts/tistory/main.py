import asyncio
import logging
import sys

from app.core.logging import setup_logging
from scripts.tistory.login import login
from scripts.tistory.post import post


setup_logging()
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    try:
        match (sys.argv[1]):
            case 'login':
                asyncio.run(login())

            case 'post':
                asyncio.run(post())

            case '_':
                raise ValueError('argument not found')

    except (IndexError, ValueError) as e:
        logger.exception(str(e))

    except Exception as e:
        raise e