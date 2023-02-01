from loguru import logger


class ErrorHandler:
    def __init__(self, person):
        self.person = person

    def __call__(self, ex):
        logger.error(f"Failed producing person {self.person}", exc_info=ex)
