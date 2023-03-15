user_input = int(input())
first = 1
pattern = 6
room = 1

if user_input == 1:
    print(1)

else:
    while True:
        first = first + pattern
        room += 1
        if user_input <= first:
            print(room)
            break
        pattern += 6