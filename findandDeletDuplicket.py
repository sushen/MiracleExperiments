import collections

with open('FindDuplicateTestBigFile.txt','r') as file:
    groupLinks = file.readlines()
    groupLinkSet =set(groupLinks)

    print(groupLinkSet)
    print(len(groupLinks))

    duplicateLinks = [item for item, count in collections.Counter(groupLinks).items() if count > 1]
    duplicateLinkSet = set(duplicateLinks)

    print(duplicateLinkSet)
    print(len(duplicateLinks))

    uniqueFile = groupLinkSet - duplicateLinkSet
    print(uniqueFile)
    print(len(uniqueFile))

    with open('FindDuplicateTestSmallFile.txt', 'r') as file:
        sortedGroupLinks = file.readlines()
        sortedGroupLinksSet = set(sortedGroupLinks)
        print(sortedGroupLinksSet)
        print(len(sortedGroupLinks))

    with open('FindDuplicateTestBigFile.txt', 'w') as file:
        sortedUniqueFile = groupLinkSet - sortedGroupLinksSet
        file.writelines(sortedUniqueFile)
        print(sortedUniqueFile)
        print(len(sortedUniqueFile))

# t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
t = ["mango","mango","mango","banana","apple"]
tSet = set(t)
print(list(set(t)))

# s = [1, 2, 3]
s= ["mango","banana","Grap"]
sSet = set(s)
list(tSet - sSet)

print(tSet - sSet)