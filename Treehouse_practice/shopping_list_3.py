# show_help function
# show_list function
# welcome message
# main function

shopping_list=[]

def show_help():
    print("\nUse common to separate each item."
          "Type 'done' to quit,'show' to see the current list, 'help' to get some help.")

def show_list():
    print('\n')
    count= 1
    for item in shopping_list:
        print("{}. {}".format(count, item))
        count+= 1

def welcome():
    print("Welcome! this is a tool that help you remember your shopping list!")
    print("Please give me a list you want to shop for.")

welcome()

while True:
    newStuff = input(">  ")
    print("Please type in words.")
    if newStuff.lower()== 'done':
        print("\nHere is your list:")
        show_list()
        print("Bye!")
        break
    elif newStuff.lower()== 'show':
        show_list()
        continue
    elif newStuff.lower()== 'help':
        show_help()
        continue
    else:
        new_list= newStuff.split(',')
        index= input("You are want to put this at a certain spot? we have {} items\n".format(len(shopping_list)))
        if index:
            seq= int(index)-1
            for item in new_list:
                shopping_list.insert(seq,item.strip())
                seq+=1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
