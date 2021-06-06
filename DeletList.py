# a = [9, 8, 7, 6]
# del a[1]
# print(a)
#


with open('categoriesGroup.txt') as file:
    lines = file.readlines()

    groupLinkList = []

    for groupLists in lines:
        groupLinkList.append(groupLists)
        groupIndex = (len(groupLinkList) - 1)
        print("Line Number : " + str(groupIndex))
        print("This line will be deleted :" + lines[groupIndex])
        del lines[groupIndex]
        deletedLink = lines[groupIndex]
        with open('groupCategorized.txt', 'w') as f:
            f.write("%s" % deletedLink)
        # print(input("Press any Key: "))

    print("Total Group :" + str(len(groupLinkList)))


