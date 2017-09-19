# Create a function that takes a list of GitHub handles as input and returns a
# list of strings that represents
# GitHub url's under Green Fox Academy organization in the following format:
# "https://github.com/greenfox-academy/teststudent"

# example:
# input: ["ghhandle1", "ghhandle2"]
# output: ["https://github.com/greenfox-academy/ghhandle1", "https://github.com/greenfox-academy/ghhandle2"]

names = ["ghhandle1", "ghhandle2", "Tofiz"]

def urls_from_handles(users):
    url = []
    for i in range(len(users)):
        url.append("https://github.com/greenfox-academy/" + users[i])
    return url




# urls_from_handles(names)
print(urls_from_handles(names))
