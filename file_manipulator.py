command = list(map(str,input().split()))

pathname = command[1]

if command[0] == "reverse":
    content = ""
    with open(pathname) as f:
        content = f.read()
    reverse_content = content[::-1]
    with open("output_text.txt",'w') as output_text:
        output_text.write(reverse_content)

elif command[0] =="copy":
    content = ""
    with open(pathname) as f:
        content = f.read()
    with open("outputpath.txt",'w') as outputpath:
        outputpath.write(content)

elif command[0] == "duplicate-contents":
    content = ""
    n = int(command[2])
    with open(pathname) as f:
        content = f.read()
    with open(pathname,'a') as f:
        for _ in range(n):
            f.write(content)
elif command[0] == "replace-string":
    content = ""
    with open(pathname) as f:
        content = f.read()
    replace_content = content.replace(command[2],command[3])
    with open(pathname,'w') as f:
        f.write(replace_content)

