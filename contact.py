def add_contact(contact_list):

    def adder(name,phone):
        contact_list[name] = phone
    return adder

def delete_contact(contact_list):

    def deleter(name):
        if name in contact_list:
            del contact_list[name]
        else:
            print('there is no such contact in "contact list"')
    return deleter

def search_contact(contact_list):

    def searcher(name):
        if name in contact_list:
            print(f"{name} : {contact_list[name]}")
        else:
            print('no such contact in "contact list"')
    return searcher

def view_contacts(contact_list):

    def viewer():
        if contact_list:
            for name,phone in contact_list.items():
                print(f"{name} : {phone}")
        else:
            print("contact_list is empty")
    return viewer


def main():
    contact_list = {}
    while True:
        print("Menu")
        print("enter 1 for adding contact")
        print("enter 2 for deleting contact")
        print("enter 3 for searching contact")
        print("enter 4 for vieweing contacts")
        print("enter 5 for finishing")

        click = input("enter number: ")

        if click == '1':
            name = input("enter contact name: ")
            phone = input("enter contact phone: ")
            add_contact(contact_list)(name,phone)

        elif click == '2':
            name = input("enter contact name: ")
            delete_contact(contact_list)(name)

        elif click == '3':
            name = input("enter contact name: ")
            search_contact(contact_list)(name)

        elif click == '4':
            view_contacts(contact_list)()

        elif click == '5':
            print("good bye")
            break
        else:
            print('wrong input')

if __name__ == "__main__":
    main()

    
























