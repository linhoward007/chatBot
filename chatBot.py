import chatBot_module as m

question = ''
answer = ''
QA = {'你是誰' : '我是聊天機器人', '聽不懂' : '請再說一次'}         

while True:
    print("請說話")
    question = m.bot_listen()
    print(question)   
    if question in QA:
        answer = QA[question]
        m.bot_speak(answer, 'zh-tw')
        print(answer)
    else:
        keyword = m.bot_get_google(question)
        content = m.bot_get_wiki(keyword)
        if content != None:
            print("要結束請連續按 ctrl+c")
            m.bot_speak_re(content)
        else:
            print("找不到相關的維基百科資料")
