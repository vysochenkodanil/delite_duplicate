def main(a, b):
    result = list(dict.fromkeys(b))
    diference = a - len(result)
    result.extend(diference * '_')
    
    return result  

if __name__ == '__main__':
    a = int(input())
    b = list(map(int, input().split()))
    
    result = main(a, b)
    print(' '.join(map(str, result)))