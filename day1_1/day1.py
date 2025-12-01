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
        direction = row[0]
        step = int(row[1:-1])
        step_remainder = step % 100
        
        step_rotation = int(step // 100)
        if (direction == 'L'):
            if (step_remainder < current):
                current -= step_remainder
            elif (step_remainder == current):
                current = 0;
                count += 1;
            else: #step_remainder > current
                current = current - step_remainder + 100
                
        elif (direction == 'R'):
            summation = current + step_remainder
            if (summation < 100):
                current = summation
            elif (summation == 100):
                current = 0
                count += 1
            else: #summation > 100
                current = summation - 100
       
  
    print("Result: ", count)


#The number of time dial points at is 1071.
