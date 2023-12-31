call_count = 0

def greet():
    global call_count
    call_count += 1
    print(call_count,'. hello buddy!')
    greet()

greet()