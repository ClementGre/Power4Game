def format_time_ms(time):
    minutes = int(time / 60)
    seconds = int(time % 60)

    ms = int(time * 100) % 100
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    if ms < 10:
        ms = "0" + str(ms)

    return f"{minutes}:{seconds}:{ms}"
