def userRegistration() :
    print("User registration: ")
    id = input("Enter id: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    try: 
        if validateUser(int(id), name, age, email) :
            print("User registration sccessful")
    except TypeError as e:
        print("Error: ", e)
    except ValueError as e:
        print("value Error: Your input is not of expected type")
    except Exception as e :
        print("Error : ", e)
    
def validateUser(id, name, age, email) :
    if not isinstance(id, int) :
        raise TypeError("Only integers are allowed in name")
    if not isinstance(name, str) :
        raise TypeError("Name should be string only")
    if not int(age) >= 18 and int(age) <= 100 :
        raise Exception("Age should be between 18 and 100 years")
    if not "@" in email :
        raise Exception("Email is not valid")
    return True

userRegistration()