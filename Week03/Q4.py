monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday Class: {monday_class}")
print(f"Wednesday Class: {wednesday_class}")
print(f"Both Classes: {monday_class & wednesday_class}")
print(f"Attended either classes: {monday_class | wednesday_class}") # | = pipe, shift + \
print(f"Only Monday : {monday_class - wednesday_class}")
print(f"Only one class : {monday_class ^ wednesday_class}") # ^ = Caret, Shift + 6
all_students = monday_class | wednesday_class
print("Is Monday subset of all students: ", monday_class <= all_students)