from api_v1.logs import Logs

logs = Logs()


def check_coord(limit: list, coord: list):
    """
    :param limit: Upper end point of the plane
    :param coord: Current position
    :return: Review that the current points do not exceed the allowed limits.
    """
    max_coord = max(coord)
    min_coord = min(coord)
    max_limit = max(limit)
    if max_coord > max_limit or min_coord < 0:
        logs.warning_limit()
