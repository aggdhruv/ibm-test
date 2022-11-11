if __name__  == '__main__':
    n = int(input())
    tshirts = list(input().split())
    m = int(input())
    requests = list(input().split())
    # print(tshirts, requests)

    sizes = {'S':[], 'M':[], 'L': []}
    for shirt in tshirts:
        count = shirt.count('X')
        main_size = shirt[-1]
        if main_size == "M" or main_size == 'L':
            sizes[main_size].append(count)
        else:
            sizes[main_size].append(count*-1)
    sizes['S'].sort()
    sizes['L'].sort()
    # print(sizes)

    flag = "Yes"

    for shirt in requests:
        main_size = shirt[-1]
        count = shirt.count('X')
        if main_size == 'L':
            if sizes[main_size][-1] < count:
                flag = "No"
                break
        elif main_size == 'M':
            if len(sizes['L']) == 0 and len(sizes['M']) == 0:
                flag = "No"
                break
        else:
            if len(sizes['L'])== 0 and len(sizes['M']) == 0 and sizes[main_size][-1] < count*-1:
                flag = "No"
                break

    print(flag)

    
    
