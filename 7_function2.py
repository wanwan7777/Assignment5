import statistics, math

def my_sd(input):
    print(f'Input: {input}')
    length = len(input)
    sum = 0
    mean = statistics.mean(input)
    print(f'Mean: {mean}')
    for x in input:
        sum += (int(x)- mean)**2
    sum = sum / length
    return math.sqrt(sum)
    


#1. Input
input = [10,20,30]

#2. Process
answer = my_sd(input)
answer = round(answer,3)

#3.Output
print(f'Answer: {answer}')