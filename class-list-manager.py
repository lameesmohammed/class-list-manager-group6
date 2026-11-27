# Class List Manager - Group6
# MIS 211 Bonus Assignment (GitHub Teamwork)
 
names = ["Lames", "Layan", "Dona", "Yara",]
 
 
# ===== Each student adds her function BELOW this line =====
 
# Written by: Lames Almarshad
def count_names(names):
    count = 0
    for name in names:
        count = count + 1
    return count 
 # Written by: Lames Almarshad
def search_name(names, name):
    if name in names:
        return True
    else:
        return False
 # Written by: Yara Alqurun
def sort_names(names):
    return sorted(names)
# Written by: Yara Alqurun
def names_starting_with(names, letter):
    result = []
    for name in names:
        if name.lower().startswith(letter.lower()):
            result.append(name)
    return result
 # Written by: Dona
def to_upper(names):
    result = []
    for name in names:
        result.append(name.upper())
    return result
 # Written by: Dona
def count_vowels(name):
    count = 0
    for letter in name.lower():
        if letter in "aeiou":
            count = count + 1
    return count
 
# Written by: Layan
def remove_duplicates(names):
    result = []
    for name in names:
        if name not in result:
            result.append(name)
    return result
 
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Number of names:", count_names(names))
    print("Is Lames in the list?", search_name(names, "Lames"))
    print("Sorted names:", sort_names(names))
    print("Names starting with Y:", names_starting_with(names, "Y"))
    print("Uppercase names:", to_upper(names))
    print("Vowels in Dona:", count_vowels(names[4]))
    print("Without duplicates:", remove_duplicates(names))
main()
