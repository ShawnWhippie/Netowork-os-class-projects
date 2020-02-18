phone_number = int(input())

area = phone_number // 10000000
first_h = phone_number // 10000
first_h = first_h % 1000
second_h = phone_number % 10000
print(area)
print(first_h)
print(second_h)
