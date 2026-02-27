import secrets
import string
generated_otp= None
def otp_generation():
    global generated_otp 
    generated_otp = ''.join(secrets.choice(string.digits) for i in range(6))
    return generated_otp  
print("*********** OTP GENERATION SYSTEM ***********")
while True:
    print("1.OTP GENERATION!")
    print("2.OTP VERIFICATION!")
    print("3.EXIT")

    choice=input("Enter an option to proceed:")

    if choice == "1":
        print("The generated OTP is:",otp_generation())
    elif choice == "2":
        if generated_otp is None:
            print("Please generate an OTP first!")
            continue

        while True:
            user_otp=input("Enter an OTP to verify:")
            if user_otp:
                if user_otp == generated_otp:
                    print("Your OTP has been verified successfully!!")
                    break
                else:
                    print("The OTP you entered is invalid. Please try again")
            else:
                print("You didn't enter anything!")
    elif choice == "3":
        print("Exiting...:)")
        break
    else:
        print("Invalid choice!Try Again.. :(")