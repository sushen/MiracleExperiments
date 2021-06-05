

likeBtnXpathAria = ["apple", "Banana", "Clocolet", "Moris", "Vat", "Whisky", "Bagin", "Borboti"]

likeBtnList = []
try:
    for likeBtn in likeBtnXpathAria:
        likeBtnList.append(likeBtn)

        print(len(likeBtnList))
        print(likeBtnXpathAria[(len(likeBtnList))*2])

except:
    pass
