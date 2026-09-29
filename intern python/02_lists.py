subjects = ["Python", "AI", "ML","Mathematics", "Physics" ]         #List

print(subjects[0])                                                  #call 0th index
print(subjects[3])                                                  #call 3rd index
print(subjects[4])                                                  #call 4th index
subjects.append("English")                                          #add a element to list

print(subjects)

subjects.remove("Mathematics")                                      #by value
subjects.pop(0)                                                     #by  index

print(subjects)