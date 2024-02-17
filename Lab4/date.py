from datetime import datetime,timedelta
nowdate=datetime.now()
newdate=nowdate-timedelta(days=5)
print(newdate)  #ex1

today=datetime.now()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("Yesterday: ",yesterday.strftime("%d"))
print("Today: ", today.strftime("%d"))
print("Tomorrow: ",tomorrow.strftime("%d"))   #ex2

now_date=datetime.now()
droptime=now_date.replace(microsecond=0)
print(droptime)   #ex 3

first_date = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S") 
second_date = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
print((second_date-first_date).total_seconds())    #ex 4