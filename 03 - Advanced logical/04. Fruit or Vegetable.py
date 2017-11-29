userInput=input().lower()
if userInput  in ("banana", "apple", "kiwi", "cherry", "lemon", "grapes"):
    print("fruit")
elif userInput  in ("tomato", "cucumber", "pepper", "carrot"):
    print("vegetable")
else:
    print("unknown")