import csv
sample_file = 'sample.csv'
file = 'input.csv'

start_point = 50

current = start_point
count = 0
step_count = 0


with open(file,'r',newline='') as csvfile:
    reader = csvfile.readlines()
    for row in reader:
        step_count += 1
        if (step_count > 0 and step_count < 5000):
            direction = row[0]
            step = int(row[1:-1])
            step_remainder = step % 100
            step_rotation = step // 100
            count += step_rotation

            if (direction == 'L'):
                if (step_remainder < current):
                    current -= step_remainder
                elif (step_remainder == current):
                    current = 0
                    count += 1
                else: #step_remainder > current
                    if current > 0:
                        count += 1
                    current = current - step_remainder + 100

                    
            elif (direction == 'R'):
                # max summation = 99 + 99 = 198
                summation = current + step_remainder
                if (summation < 100):
                    current = summation
                elif (summation == 100):
                    current = 0
                    count += 1
                else: #summation > 100
                    if current > 0:
                        count += 1
                    current = summation - 100
               
     
            print("value", step)
            print("step rotation", step_rotation, "count", count)
            print("current", current)
  
    print("Result: ", count)



