from api_v1.logs import Logs

logs = Logs()


def check_coord(limit, coord):
    max_coord = max(coord)
    max_limit = max(limit)
    if max_coord > max_limit:
        logs.warning_limit()


