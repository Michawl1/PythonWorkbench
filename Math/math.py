MINUTE = 60


def printStatment(time, week):
    print("Week: {}, Time {} minutes".format(week, (time / MINUTE)))


if __name__ == "__main__":
    start = 60

    week = 1
    for i in range(0, 4):
        printStatment(start, week)
        week += 1

    while start < 3600:
        start = start + (start * 0.1)

        for i in range(0, 4):
            printStatment(start, week)
            week += 1