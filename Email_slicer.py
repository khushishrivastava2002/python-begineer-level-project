"""
    Email Slicer :- 
            An Email slicer is a very useful program for separating the username and domain name of an email address.
            
            To create an email slicer with Python, our task is to write a program that can retrieve the username and the domain name of the email.
            
            For Example:- 
            1)
                Email:- abc@gmail.gom
                ---> Name:- abc
                ---> Domain:- gmail.com
            2)
                Email:- kpathak@hotmail.com
                ---> Name:- Kpathak
                ---> Domain:- hotmail.com
    """
    
# Implementation in python

email = input("Enter Your EmailId: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
a = (f"Your user name is '{username}\n' and your domain is '{domain_name}'")
print(a)