def categoriesGroup():
    with open('FindDuplicateTestBigFile.txt') as file:
        lines = file.readlines()

        # TODO: Test first Line to total list

        # TODO: Second List Compare to First List

        # TODO: Delete and Save File



        # groupLinkList = []
        # for groupLists in lines:
        #     groupLinkList.append(groupLists)
        #     groupIndex = (len(groupLinkList) - 1)
        #     print("Line Number : " + str(groupIndex))
        #     print("This line will be deleted :" + lines[groupIndex])
        #     del lines[groupIndex]
        #     deletedLink = lines[groupIndex]
        #
        #     line_index = 3
        #     deleteLines = None
        #     with open('FindDuplicateTestBigFile.txt', 'r') as file_handler:
        #         deleteLines = file_handler.readlines()
        #     deleteLines.insert(line_index, deletedLink)
        #     with open('FindDuplicateTestSmallFile.txt', 'w') as file_handler:
        #         file_handler.writelines(deleteLines)
        #     print(input("Press any Key: "))


categoriesGroup()
