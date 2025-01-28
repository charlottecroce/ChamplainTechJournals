def days_to_hours(days):
    """ Converts days to hours

    Arguments:
      days (int): number of days as an integer

    Return:
      number of hours (int)

    Assumptions:
      days must be an int
    """
    return days * 24

print('Days to hours:', days_to_hours(3))
hours = days_to_hours(2)


def days_to_minutes(days):
    """ Converts days to minutes

    Arguments:
      days (int): number of days as an integer

    Return:
      number of minutes (int)

    Assumptions:
      days must be an int
    """
    return days_to_hours(days) * 60


def days_to_seconds(days):
    """ Converts days to seconds

    Arguments:
      days (int): number of days as an integer

    Return:
      number of seconds (int)

    Assumptions:
      days must be an int
    """
    return days_to_minutes(days) * 60
