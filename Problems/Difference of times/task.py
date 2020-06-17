# put your python code here
first_hour = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hour = int(input())
second_minutes = int(input())
second_seconds = int(input())
result = (second_seconds - first_seconds) \
         + (second_minutes - first_minutes) * 60 \
         + (second_hour - first_hour) * 3600
print(result)
