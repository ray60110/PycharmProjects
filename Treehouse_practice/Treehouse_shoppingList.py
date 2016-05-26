#just to create a shopping list

shopping_list=[]

def get_help():
    print("""
Enter 'done' to stop adding your to buy items.
Enter 'help' to see this instruction again.
Enter 'show' to see your present shopping list.

""")

get_help()

def add_to_list(item):
    shopping_list.append(item)
    print("You added {} it is the  {} items".format(item, len(shopping_list)))


while True:
    new_item= input(">> ")

    if new_item.lower() == "done":
        print("Here is your item: {}".format(", ".join(shopping_list)))
        break
    elif new_item.lower() == "help":
        get_help()
        continue
    elif new_item.lower() == "show":
        for item in shopping_list:
            print(item)
        continue

    add_to_list(new_item)
