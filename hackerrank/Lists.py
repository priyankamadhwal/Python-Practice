if __name__ == '__main__':
    N = int(input())
    L= []
    for _ in range(N):
        s = input().split()
        cmd,args = s[0],s[1:]
        if cmd == 'print':
            print(L)
        else:
            cmd += "("+",".join(args)+")"
            eval("L."+cmd)
