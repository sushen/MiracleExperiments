import collections

with open('FindDuplicateTestBigFile.txt','r') as file:
    groupLinks = file.readlines()
    print(len(groupLinks))
    duplicateLinks = [item for item, count in collections.Counter(groupLinks).items() if count > 1]
    print(len(duplicateLinks))

def categoriesGroup():
    with open('FindDuplicateTestBigFile.txt') as file:
        lines = file.readlines()

        # TODO: Test first Line to total list

        # TODO: Second List Compare to First List

        # TODO: Delete and Save File


categoriesGroup()
