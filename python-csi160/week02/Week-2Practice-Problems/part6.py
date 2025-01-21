# Read an integer:
seconds_past_midnight = int(input())


full_hours_past_midnight = (seconds_past_midnight // 3600) % 24
full_minutes_past_midnight = (seconds_past_midnight // 60) % 1440

print (full_hours_past_midnight, full_minutes_past_midnight)

