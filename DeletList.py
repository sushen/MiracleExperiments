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

        line_index = 3
        deleteLines = None
        with open('groupCategorized.txt', 'r') as file_handler:
            deleteLines = file_handler.readlines()
        deleteLines.insert(line_index, deletedLink)
        with open('groupCategorized.txt', 'w') as file_handler:
            file_handler.writelines(deleteLines)
        print(input("Press any Key: "))

    print("Total Group :" + str(len(groupLinkList)))


