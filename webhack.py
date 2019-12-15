from selenium import webdriver
import csv
import random

driver= webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.get('http://yourserverip)

def now():
    element=driver.find_elements_by_class_name('jjo-display')
    return element[0].text
def send(message):
    input_tag = driver.find_element_by_xpath('//*[@id="Talk"]')
    input_tag.send_keys(message)
    driver.find_element_by_xpath('//*[@id="ChatBtn"]').click()

f = open('kr_korean.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(f)

result = []
for line in reader:
    result.append(line)

print("데이터의 개수 : " + str(len(result)) + "개")
f.close()

def get_words(start):
    text_list=[]
    for i in result:
        if i[0].startswith(start) and not i[0].endswith('다'):
            if "-" in i[0] or "^" in i[0] or "‧" in i[0] or " " in i[0]:
                continue
            text=i[0]
            if len(text)>=2:
                text_list.append(text)
    text_list.sort(key=lambda item:(len(item),item),reverse=True)
    return text_list


def attack(start):
    my_list = get_words(start)
    if len(my_list) == 0:
        print("사전에서 찾을 수 없습니다")
        return
    length = len(my_list)
    if length > 10:
        length = 5
    i = random.randrange(0, length)
    message = my_list[i]
    print("단어 전송 " + message)
    send(message)


start = now()

if '(' in start:
    start = start.split('(')[0]

if len(start) == 1:
    attack(start)

ID = 'GUEST2611'


def auto():
    while True:
        now_player = driver.find_elements_by_class_name('game-user-current')
        if len(now_player) == 0:
            continue
        target = now_player[0].find_elements_by_class_name('game-user-name')
        if len(target) == 0:
            continue
        player_name = target[0].text
        if len(player_name) > 0 and player_name == ID:
            start = now()

            if '(' in start:
                start = start.split('(')[0]

            if len(start) == 1:
                attack(start)


auto()