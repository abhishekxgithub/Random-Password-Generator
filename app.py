import random
import string

print(" WELCOME TO OUR RANDOM PASSWORD GENERATOR")
def main():
    length=int(input(" Enter the length of the password: "))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    symbolD=string.punctuation
    digitD=string.digits
    combine=lowerD+upperD+symbolD+digitD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()