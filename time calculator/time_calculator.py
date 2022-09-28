
def days_later(n):
    if n == 1:
        return "(next day)"
    elif n > 1:
        return f"({n} days later)"
    return ""


def add_time(start, duration, day = False):
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    new_time = ""
    n = 0

    start_hour = start.split(":")[0]
    start_minute = (start.split(":")[1]).split(" ")[0]
    timezone = (start.split(" ")[1]).strip().lower()
            
    duration_hour = duration.split(":")[0]
    duration_minute = duration.split(":")[1]
    
    s_hour = int(start_hour)
    s_minute = int(start_minute)
    d_hour = int(duration_hour)
    d_minute = int(duration_minute)


    result_minute = int(s_minute) + int(d_minute)
    result_hour = int(s_hour) + int(d_hour) 


    #if result_minute >= 60:
    #    result_minute = result_minute - 60
    #    result_hour += 1

    if result_minute >= 60:
        result_hour += int(result_minute / 60)
        result_minute = int(result_minute % 60)

    if d_hour or d_minute:
        if timezone == 'pm' and result_hour > 12:
            if result_hour % 24 >= 1.0:
                n += 1
        
        if result_hour >= 12:
            hours_left = result_hour / 24
            n += int(hours_left)
        

        ttlh = result_hour

        while True:
            if ttlh < 12:
                break
            if ttlh >= 12:
                if timezone == 'pm':
                    timezone = 'am'
                elif timezone == 'am':
                    timezone = 'pm'
                ttlh -= 12


    remaining_hrs = int(result_hour % 12) or s_hour + 1 
    remaining_min = int(result_minute % 60)

    

    new_time = f'{remaining_hrs}:{remaining_min:02} {timezone.upper()}' 
    if day:
        day = day.strip().lower()
        chosen_day = int((weekdays.index(day) + n) % 7 )
        current_day = weekdays[chosen_day]
        new_time += f', {current_day.title()} {days_later(n)}'
    else:
        new_time = " ".join((new_time, days_later(n)))
        
    return new_time.strip()
