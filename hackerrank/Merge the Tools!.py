def merge_the_tools(string, k):
    strlen = len(string)
    i = 0
    while i < strlen:
        print("".join(list(dict.fromkeys(string[i:i+k]))))
        i += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
