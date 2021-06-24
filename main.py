contacts = [["John", 311, "noemail@email.com"], ["Robert", 966, "uisemali@email.com"], ["Edward", 346, "nonumber@email.ca"]]
menu = """
Main Menu
1. Display All Contacts Names
2. Search Contacts
3. Edit Contact
4. New Contact
5. Remove Contact
6. Exit
"""

def displayContact(): 
    if contacts:
        print("Contact Names are: ")
        for i in range(len(contacts)):
            print(contacts[i][0])
    else:
        print("Sorry, as of right now there are no contacts.")
    callInput()

def searchContact():
    txt = """
    Name: {}
    Phone Number: {}
    Email: {}
    """
    cherch = str(input("Please enter name of individual you would wish to search: "))
    for i in range(len(contacts)):
        for x in contacts[i]:
            if cherch == x:
                print(txt.format(contacts[i][0], contacts[i][1], contacts[i][2]))
    callInput()

def editContact():
    cherch = str(input("Please enter name of individual you would wish to search: "))
    for i in range(len(contacts)):
        for x in contacts[i]:
            if cherch == x:
                contacts[i][0] = str(input("Please enter in a new name for this contact: "))
                contacts[i][1] = int(input("Please enter in a new number for this contact: "))
                contacts[i][2] = str(input("Please enter in a new email for this contact: "))  
    callInput()

def newContact():
    name = str(input("Please enter in a name for this contact: "))
    phone = int(input("Please enter in a number for this contact: "))
    email = str(input("Please enter in an email for this contact: "))  
    contacts.append([name, phone, email])
    callInput()

def removeContact():
    cherch = str(input("Please enter name of individual you would wish to remove: "))
    for i in range(len(contacts)):
            if cherch == contacts[i][0]: 
                del contacts[i]
                break
    callInput()

def callInput():
    print(menu)
    option = int(input("Please select a number from 1 to 6: "))
    if option == 1:
        displayContact()
    elif option == 2:
        searchContact()
    elif option == 3:
        editContact()
    elif option == 4:
        newContact()
    elif option == 5:
        removeContact()
    elif option == 6:
        exit()
    else: 
        option = int(input("Please select a number again from 1 to 6: "))

callInput()
