pwd1 =input("Enter new password: ") 
pwd2 =input("Re-enter new password: ")
# TODO: Write the password logic using if..else conditional statements
if pwd1 == pwd2:#quick comparison of both passwords
    print("Password Changed")#successful change message
elif pwd1.lower() == pwd2.lower() and pwd1 != pwd2:#case sensitivity check
    print("Please check cases and try again")#case error message
else:
    print("Password do not match")#mismatch error message