from stylepy import h4
call_count = 0

def greet():
    global call_count
    call_count += 1
    h4(call_count,'. hello buddy!')
    greet()

greet()