import reply

textList = ["driver.switch_to.active_element",
            "this code is a one of important snippet for facebook automation."]

text_reply = reply.Reply(textList[0])

print(text_reply.text)

text_reply.randomRelpy()
