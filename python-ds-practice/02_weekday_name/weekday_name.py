def weekday_name(day_of_week):
    weekdays = ['Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day_of_week >= 1 and day_of_week <= 7:
        return weekdays[day_of_week-1]
    return None


print(f"{weekday_name(1)} should be Sunday")
print(f"{weekday_name(7)} should be Saturday")
print(f"{weekday_name(9)} should be None")
print(f"{weekday_name(0)} should be None")
