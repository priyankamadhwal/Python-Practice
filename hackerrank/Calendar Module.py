from calendar import weekday
m, d, y = map(int,input().split())
print(['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY'][weekday(y,m,d)])
