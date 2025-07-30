import math as math

def solution(n):
    tenery = []
    answer = 0
    while n > 0:
         tenery.append(n%3)
         n //= 3

    for i in range(len(tenery)):
        answer += int(tenery[i]) * int(math.pow(3, len(tenery) - (i+1)))

    return answer

if __name__ == "__main__":
    number = 45
    result = solution(number)
    print(result) # Output the answer as a string