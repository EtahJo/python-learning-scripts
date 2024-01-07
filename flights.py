#!/usr/bin/env python3


def time_difference(scheduled_time, estimated_time):
    """
    (number, number)-> str
    returns the amount of gap between the scheduled time (scheduled_time)
     and the estimated time (estimated_time) of a flight .

     >>> time_difference(14.3,14.3)
     0
     >>> time_difference(12,11.3)
    0.7
    >>> time_difference(3,8)
    5
    """

    return abs(scheduled_time - estimated_time)


def report_status(scheduled_time, estimated_time):
    """(number,number)-> tuple or str
    returns the flight status(on time, delayed, early) and the time difference for a flight that was
    scheduled to arrive at scheduled_time but is now going to arrive at estimated_time

    precondition: 0<=scheduled_time <=24 and 0<=estimated_time<=24

    >>> report_status(14.3,14.3)
    ("on time",0)

    >>> report_status(12,11.3)
    ("early",0.7)

    >>> report_status(3,8)
    ("delayed",5)
    """

    if scheduled_time < estimated_time:
        return ("delayed", time_difference(scheduled_time, estimated_time))
    elif scheduled_time > estimated_time:
        return("early", time_difference(scheduled_time, estimated_time))
    else:
        return "on time"


print(report_status(14.3, 14.3))
print(report_status(12, 11.3))
print(report_status(3, 8))
