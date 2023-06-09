# date = (day, month, year)

day_per_mon = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31};
day_per_mon_leap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31};


def input_date():

    date_lst = [];

    date_lst.append(int(input("Enter day: ")) - 1);
    date_lst.append(int(input("Enter month: ")) - 1);
    date_lst.append(int(input("Enter year: ")));

    return tuple(date_lst);


def print_date(date):

    print(f"{date[0] + 1}.{date[1] + 1}.{date[2]}");

def is_less(date1, date2):
    
    if (date1[2] < date2[2]):
        return True;
    elif (date1[1] < date2[1] and date1[2] == date2[2]):
        return True;
    elif (date1[0] < date2[0] and date1[1] == date2[1] and date1[2] == date2[2]):
        return True;

    return False;

def next_day(date):
    day = date[0] + 1;
    cal = day_per_mon_leap if is_leap(date[2]) else day_per_mon;
    return (day % cal[date[1] + 1], ( date[1] + (day // cal[date[1] + 1]) ) % 12, date[2] + (( date[1] + (day // cal[date[1] + 1]) ) // 12));


def is_leap(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0);
