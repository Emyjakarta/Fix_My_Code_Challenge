#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Defines the user class. """

    def __init__(self):
        """ Initializes the user instance """
        self.email = ""

    @property
    def email(self):
        """Returns the email address of user."""
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets the email address of user """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
