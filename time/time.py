import time

time_obj = time.localtime()
time_str = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)

print(time_obj)
print(time_str)