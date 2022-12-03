import datetime
import logging


class Logs:
    def __init__(self):
        self.timestamp = datetime.datetime.now()

    def info(self, X, Y, coord):
        message = "{}: Movement ({}, {}, {})".format(self.timestamp, X, Y, coord)
        logging.info(message)

    def mov_error(self, movement):
        message = " {}: Movement not allowed: {}".format(self.timestamp, movement)
        logging.error(message)

    def coord_error(self):
        message = "{}: Coord not allowed}".format(self.timestamp)
        logging.error(message)

    def warning_limit(self):
        message = "{}: Mower out of the limit".format(self.timestamp)
        logging.warning(message)
