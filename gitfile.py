def check_sum(lst):
    check = set()
    current_sum = 0
    for i in lst:
        check.add(current_sum)
        current_sum += i
        if current_sum in check:
            return True
    return False

        
lst = eval(input())
print(check_sum(lst))