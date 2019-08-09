import time
for h in range(0,24):
    for m in range(0,60):
        for s in range(0,60):
            r=chr(h//10+48)+chr(h%10+48)+':'+chr(m//10+48)+chr(m%10+48)+':'+chr(s//10+48)+chr(s%10+48)
            print(r)
            time.sleep(0.1)
            
