#To check if a date(DD/MM/YYYY) entered by the user is a valid date or not

def CheckMonth(n):
    if 1 <= n <= 12:
        return True
    else:
        return False


def IsLeapYear(n):
    if n % 100 == 0:
        if n % 400 == 0:
            return True
        else:
            return False
    elif n % 4 == 0:
        return True
    else:
        return False


def FinalCheck(d, m, y):
    if not CheckMonth(m):
        return False
    days31 = [1,3,5,7,8,10,12]
    valid = True
    if m in days31:
        if not 1 <= d <= 31:
            valid = False
    elif m == 2:
        if IsLeapYear(y):
            if not 1 <= d <= 29:
                valid = False
        else:
            if not 1 <= d <= 28:
                valid = False
    else:
        if not 1 <= d <= 30:
            valid = False
    return valid


d, m, y = map(int, input("Enter the day, month number and the year all separated by spaces : ").split())
if FinalCheck(d,m,y):
    print("Valid date")
else:
    print("Invalid date")
