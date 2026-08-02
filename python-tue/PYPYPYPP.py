def calculate_stats(number):
 total_sum =(number)
 average = total_sum / len (number)
 maximum = max(number)
 minimum = min (number)
 return total_sum , average, maximum,minimum
number = [1,2,3,4,5,]
total, avg, max_num, min_num = calculate_stats(number)
print(f"total sum: {total}")
print(f"average: {avg}")
print(f"maximum: {max_num}")
print(f"minimum: {min_num}")