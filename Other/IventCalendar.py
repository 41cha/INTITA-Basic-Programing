def time_str_to_min(time):
    time = time.split(':')
    hours,mins = time
    result = int(hours) * 60 + int(mins)
    return result

def schedule(events):
    if len(events) == 0:
        return []

    events = sorted(events, key=lambda e: time_str_to_min(e[0]))
    result = [events[0]]

    for event in events[1:]:
        time, duration = event
        past_time, past_dur = result[-1]
        end_time_last = time_str_to_min(past_time) + past_dur

        if time_str_to_min(time) >= end_time_last:
            result.append(event)

    return result

plans = schedule([('09:30', 30), ('12:30',30), ('9:00',30), ('10:00', 40), ('10:30', 60), ('11:00', 60)])
for e in plans:
    print(e)