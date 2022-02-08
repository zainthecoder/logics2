from cats import cat

if __name__ == '__main__':

    while True:
        print("Enter the information about the cat: <color> <breed>. Exit to exit")

        inp = raw_input().split()
        print(inp)

        if inp[0].lower()=='exit':
            break

        
        obj=cat(inp[0],inp[1])
        
        print(obj)
