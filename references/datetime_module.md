# datetime Module

python creator: Guido van Rossum 

---
## module
---
from datetime import datetime


---
## classes
---
1. date
    1. max = date(9999,12,31)
    2. min = date(1,1,1)
2. time
3. datetime
4. timedelta
5. timezone
6. tzinfo

---
## syntax
---
- *date(yyyy, m, d)*
- *time(HH, MM, SS)*
- *datetime(yyyy, m, d, HH, MM, SS)*

---
## built-in methods
---
- day1.***year***
- day1.***month***
- day1.***day***

- time1.***hour***
- time1.***minute***
- time1.***second***

- dt.***year***
- dt.***month***
- dt.***day***
- dt.***hour***
- dt.***minute***
- dt.***second***
- dt.***microsecond***
- dt.***today()***
- dt.***strptime(*** <date_string>,<expected_format> ***)***

---
## add & subtract dates
---
` day1 = date(2000,1,1) `
` dt = timedelta(100) ` *#num of days --> positive increase, negative decrease*
` day2 = day1 + dt `

---
## format dates
```
GVR_bday = date(1956, 1, 31) 
GVR_bday.strftime("%A, %B %d, %Y") 
date_formatted_text = "GVR was born on {:%A, %B %d, %Y}." 
print(date_formatted_text.format(GVR_bday)) 
```
-> GVR was bord on Tuesday, January 31, 1956

---
### directives
---
|   Directive   |   Example |   Description |
|:-------------:|:---------:|:-------------:|
%a  |   Wed |   Weekday, short version, usually three characters in length  |
%A  |   Wednesday	|   Weekday, full version   |
%w  |   3	|   Weekday as a number 0-6, 0 is Sunday    |
%d  |   31	|   Day of month 01-31  |
%b  |   Dec	|   Month name, short version, usually three characters in length   |
%B  |   December	|   Month name, full version    |
%m  |   12	|   Month as a number 01-12, January is 01  |
%y  |   21  |	Year, short version, without century (2021) |
%Y  |   2021    |	Year, full version  |
%H	|   17	|   Hour 00-23 (24 hour format) |
%I	|   05	|   Hour 00-12 (12 hour format) |
%p	|   PM	|   AM/PM   |
%M	|   35	|   Minute 00-59    |
%S	|   14	|   Second 00-59    |
%f	|   638745  |	Microsecond 000000-999999   |
%z	|   +0530	|   UTC offset  |
%Z	|   CST	|   Timezone    |
%j	|   182	|   Day number of year 001-366 (366 for leap year, 365 otherwise)    |
%U	|   47	|   Week number of year, Sunday as the first day of week, 00-53    |
%W	|   51	|   Week number of year, Monday as the first day of week, 00-53    |
%c	|   Tue Dec 10 17:41:00 2019	|   Local version of date and time    |
%x	|   12/10/19	|   Local version of date (mm/dd/yy)    |
%X	|   17:41:00    |   Local version of time (hh:mm:ss)    |
%%	|   %   |   A % character    |