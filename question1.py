class Hw1Q1:
    def timeConvert(input_second):
        if input_second == 60:
            return "1 minute"
        if input_second == 3600:
            return "1 hour"
        if input_second == 86400:
            return "1 day"
        if input_second < 60:
            return str(input_second) + " seconds"
        if input_second > 86400:
            days = input_second//86400
            remaining_seconds = input_second - days * 86400
            hours = remaining_seconds // 3600
            remaining_seconds_for_minutes = remaining_seconds - hours*3600
            minutes = remaining_seconds_for_minutes // 60
            seconds = remaining_seconds_for_minutes % 60
            return str(days) + " days " + str(hours)  + " hour " + str(minutes) + " minute " + str(seconds) + " seconds "

        if input_second > 3600:
            hours = input_second // 3600
            remaining_seconds = input_second - hours * 3600
            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60
            return str(hours) + " hour " + str(minutes) + " minute " + str(seconds) + " seconds "
        if input_second > 60:
             minutes = input_second // 60
             remaining_seconds = input_second % 60
             return str(minutes) + " minute " + str(remaining_seconds) + " seconds"

Value = int(input("ENTER NUMBER OF SECONDS (0 to quit): "))
while Value != 0:
    print(Hw1Q1.timeConvert(Value))
    Value = int(input("ENTER NUMBER OF SECONDS (0 to quit: "))
print("CODE HAS BEEN EXECUTED")