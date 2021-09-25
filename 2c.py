def generate_n_chars(i,c):
    counter = 0
    answer = ""
    while counter < i:
        counter += 1
        answer += c
        print(answer)
i = int(input("Please enter an integer: "))
c = input("Please enter a character: ")
generate_n_chars(i,c)
