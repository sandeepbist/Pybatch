
# 1 logic
sapids = [123,234324,345345,4545]
def id2email(id):
    return f"{ id }@stu.upes.ac.in"
    
emails=[]
for id in sapids:
    email = id2email(id)
    emails.append(email)

list_of_emails = emails
list_of_emails


sapids = [123,234324,345345,4545]
def id2email(id):
    return str(id) + "@stu.upes.ac.in"

list_of_emails = list( map(id2email,sapids)) 
list_of_emails

# 2 Logic using map
sapids = [123,234324,345345,4545]

list_of_emails = list(map(lambda id: str(id) + "@stu.upes.ac.in" , sapids)) # for python3
list_of_emails

# 3 using list comprehension

sapids = [123,234324,345345,4545]

list_of_emails = [ f"{ id }@stu.upes.ac.in" for id in sapids ]
list_of_emails

sap = [123,122,234,45,234,645,43]
emails = [ f"{i}@stu.upes.ac.in" for i in sap]
emails