def greeting(name, age=18):
    print(f"Hello {name.title()}!, you are {age} years old")

greeting('alex', 21)
greeting('alan')
name = input("Enter your name: ")    
greeting(name,32)