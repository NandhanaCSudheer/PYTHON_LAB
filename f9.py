with open("f9.txt", "r") as f:
    for word in f:
        w = word.strip()
        if w == w[::-1]:
            print(w)
            
