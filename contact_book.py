"""
    Contact book:- 
                 This is a command-line project where you will design a contact book application that users can use to save and find contact details. The application should also allow users to update contact information, delete contacts, and list saved contacts.     
"""



# Implementation in python

contacts ={}

def display_contacts():
    print("Name\t\tcontact number")
    for key in contacts:
        print("{}\t\t{}".format(key,contacts.get(key)))
    
    
    
    
while True:
    choice = int(input("\n 1. Add New Contact \n 2. Search Contact \n 3. Display Contact \n 4. Edit Contact \n 5. Delete Contact \n 6. Exit \n Please Enter Your choice:- "))
    
    if choice == 1:
        name = input("Enter the contact name :-  ")
        phone = int(input("Enter the mobile number:- "))
        contacts[name] = phone
        
    elif choice == 2:
        search_name = input("Enter the contact name:- ")
        if search_name in contacts:
            print(search_name,"'s contact number is ",contacts[search_name])
        else:
            print("Name is not found in contact book")
            
    elif choice == 3:
        if not contacts:
            print("Empty Contact Book")
        
        else:
            display_contacts()
            
    elif choice ==4:
        edit_contanct = input("Enter the contact to be edited ")
        if edit_contanct in contacts:
            phone = int(input("Enter Mobile Number "))
            contacts[edit_contanct] = phone
            print("Contact updated")
            display_contacts()
            
        else:
            print("Name is not found in contact book!!")
            
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted")
        if del_contact in contacts:
            confirm = input("Do you want to delete this contact y/n ?  ")
            if confirm == 'y' or confirm =='Y' :
                contacts.pop(del_contact)
            display_contacts()
        else:
            print("Name is not found in contact book")
            
    else:
        break
            
    