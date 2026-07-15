import datetime

with open("server_logs.txt", "r") as file:
    for line in file:
        date = line.split()[0]
        time = line.split()[1]
        date_time_str = f"{date} {time}"
        date_time_object = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        print(date_time_object, type(date_time_object))

        required_logs_date = datetime.datetime(2026, 7, 15)
        # print(required_logs_date, type(required_logs_date))

        if required_logs_date.date() == date_time_object.date():
            print(line)