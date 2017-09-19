# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter
email = str(input("email: "))
def name_from_email(e):
    cut_from_at = e.partition('@')[0]
    last_name = str(cut_from_at.split('.')[0])
    first_name = str(cut_from_at.split('.')[1])
    name = (first_name.title() + " " + last_name.title())
    return name

print(name_from_email(email))
