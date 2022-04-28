import datetime


def Cal_Date():
    First_Day_We_Loved = datetime.datetime(2022, 4, 26)
    Today = datetime.datetime.now()
    The_Day_We_Loved = Today - First_Day_We_Loved
    return The_Day_We_Loved.days
