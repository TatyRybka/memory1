
'''	М2 У3. Приложение Memory Card. Ч1 БЕЗ ANSGROUP'''

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, 
# QRadioButton, QPushButton, QLabel)

# app = QApplication([])
# window = QWidget()
# # Создаем панель вопроса
# window.setWindowTitle('Memory Card')
# btn_OK = QPushButton('Ответить')
# lb_Question = QLabel('Вопрос???')

# RadioGroupBox = QGroupBox("Варианты ответов")
# rbtn_1 = QRadioButton('Энцы')
# rbtn_2 = QRadioButton('Смурфы')
# rbtn_3 = QRadioButton('Чулымцы')
# rbtn_4 = QRadioButton('Алеуты')
# layout_ans1 = QHBoxLayout()   
# layout_ans2 = QVBoxLayout() 
# layout_ans3 = QVBoxLayout()

# layout_ans2.addWidget(rbtn_1) 
# layout_ans2.addWidget(rbtn_2)
# layout_ans3.addWidget(rbtn_3) 
# layout_ans3.addWidget(rbtn_4)
# layout_ans1.addLayout(layout_ans2)
# layout_ans1.addLayout(layout_ans3)

# RadioGroupBox.setLayout(layout_ans1) #панель с вариантами ответов


# line1 = QHBoxLayout()
# line2 = QHBoxLayout()
# line3 = QHBoxLayout()
# line1.addWidget(lb_Question) 
# line2.addWidget(RadioGroupBox) 
# line3.addWidget(btn_OK) 
# # Теперь созданные строки разместим друг под другой:
# layout_card = QVBoxLayout()
# layout_card.addLayout(line1)
# layout_card.addLayout(line2)
# layout_card.addLayout(line3)


# window.setLayout(layout_card)

# window.show()

# app.exec()

'''	М2 У3. Приложение Memory Card. Ч1 C ANSGROUP'''

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, 
# QRadioButton, QPushButton, QLabel)

# app = QApplication([])
# window = QWidget()
# # Создаем панель вопроса
# window.setWindowTitle('Memory Card')
# btn_OK = QPushButton('Ответить')
# lb_Question = QLabel('Вопрос???')

# RadioGroupBox = QGroupBox("Варианты ответов")
# rbtn_1 = QRadioButton('Энцы')
# rbtn_2 = QRadioButton('Смурфы')
# rbtn_3 = QRadioButton('Чулымцы')
# rbtn_4 = QRadioButton('Алеуты')
# layout_ans1 = QHBoxLayout()   
# layout_ans2 = QVBoxLayout() 
# layout_ans3 = QVBoxLayout()

# layout_ans2.addWidget(rbtn_1) 
# layout_ans2.addWidget(rbtn_2)
# layout_ans3.addWidget(rbtn_3) 
# layout_ans3.addWidget(rbtn_4)
# layout_ans1.addLayout(layout_ans2)
# layout_ans1.addLayout(layout_ans3)

# RadioGroupBox.setLayout(layout_ans1) #панель с вариантами ответов
# # Создаем панель результата
# AnsGroupBox = QGroupBox("Результат теста") 
# lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
# lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа

# layout_res = QVBoxLayout()
# layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
# layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)


# line1 = QHBoxLayout()
# line2 = QHBoxLayout()
# line3 = QHBoxLayout()
# line1.addWidget(lb_Question) 
# line2.addWidget(RadioGroupBox) 
# line3.addWidget(btn_OK) 
# # Теперь созданные строки разместим друг под другой:
# layout_card = QVBoxLayout()
# layout_card.addLayout(line1)
# layout_card.addLayout(line2)
# layout_card.addLayout(line3)
# # RadioGroupBox.hide() # СПРЯЧЕМ ПЕРВОЕ ОКНО
# AnsGroupBox.setLayout(layout_res)
# AnsGroupBox.show()# ПРКАЖЕМ 2 ОКНО
# line2.addWidget(AnsGroupBox)  


# window.setLayout(layout_card)

# window.show()

# app.exec()

'''М2 У3. Приложение Memory Card. Ч2.1.'''

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#         QApplication, QWidget, 
#         QHBoxLayout, QVBoxLayout, 
#         QGroupBox, QButtonGroup, QRadioButton,  
#         QPushButton, QLabel)


# app = QApplication([])


# btn_OK = QPushButton('Ответить') 
# lb_Question = QLabel('Алгоритм, составленный на языке программирования и имеющий уникальное имя это?') 


# RadioGroupBox = QGroupBox("Варианты ответов")


# rbtn_1 = QRadioButton('Функция')
# rbtn_2 = QRadioButton('Переменная')
# rbtn_3 = QRadioButton('Класс')
# rbtn_4 = QRadioButton('Метод')


# RadioGroup = QButtonGroup() 
# RadioGroup.addButton(rbtn_1)
# RadioGroup.addButton(rbtn_2)
# RadioGroup.addButton(rbtn_3)
# RadioGroup.addButton(rbtn_4)


# layout_ans1 = QHBoxLayout()   
# layout_ans2 = QVBoxLayout()
# layout_ans3 = QVBoxLayout()
# layout_ans2.addWidget(rbtn_1) 
# layout_ans2.addWidget(rbtn_2)
# layout_ans3.addWidget(rbtn_3) 
# layout_ans3.addWidget(rbtn_4)


# layout_ans1.addLayout(layout_ans2)
# layout_ans1.addLayout(layout_ans3)


# RadioGroupBox.setLayout(layout_ans1)


# AnsGroupBox = QGroupBox("Результат теста")
# lb_Result = QLabel('прав ты или нет?') 
# lb_Correct = QLabel('ответ будет тут!')
# layout_res = QVBoxLayout()
# layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
# layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
# AnsGroupBox.setLayout(layout_res)


# layout_line1 = QHBoxLayout() 
# layout_line2 = QHBoxLayout() 
# layout_line3 = QHBoxLayout() 


# layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# layout_line2.addWidget(RadioGroupBox)   
# layout_line2.addWidget(AnsGroupBox)  
# AnsGroupBox.hide()


# layout_line3.addStretch(1)
# layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
# layout_line3.addStretch(1)


# layout_card = QVBoxLayout()


# layout_card.addLayout(layout_line1, stretch=2)
# layout_card.addLayout(layout_line2, stretch=8)
# layout_card.addStretch(1)
# layout_card.addLayout(layout_line3, stretch=1)
# layout_card.addStretch(1)
# layout_card.setSpacing(5) # пробелы между содержимым


# def show_result():
#     ''' показать панель ответов '''
#     RadioGroupBox.hide()
#     AnsGroupBox.show()
#     btn_OK.setText('Следующий вопрос')


# def show_question():
#     ''' показать панель вопросов '''
#     RadioGroupBox.show()
#     AnsGroupBox.hide()
#     btn_OK.setText('Ответить')
#     RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
#     rbtn_1.setChecked(False)
#     rbtn_2.setChecked(False)
#     rbtn_3.setChecked(False)
#     rbtn_4.setChecked(False)
#     RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана


# def test():
#     ''' временная функция, которая позволяет нажатием на кнопку вызывать по очереди
#     show_result() либо show_question() '''
#     if 'Ответить' == btn_OK.text():
#         show_result()
#     else:
#         show_question()


# window = QWidget()
# window.setLayout(layout_card)
# window.setWindowTitle('Memo Card')
# btn_OK.clicked.connect(test) # проверяем, что панель ответов показывается при нажатии на кнопку
# window.show()
# app.exec()

'''17.11 Начать с проверки и исправления ошибок'''
'''	М2 У4. Приложение Memory Card. Ч2.2'''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, 
QRadioButton, QPushButton, QLabel)
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from random import shuffle
class Question(): #
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3): #
        self.question = question #
        self.right_answer = right_answer #
        self.wrong1 = wrong1 #
        self.wrong2 = wrong2 #
        self.wrong3 = wrong3 #
       

questions_list = []
questions_list.append(Question('Какого времени года не существует?', "веснуль", "лето", "зима", "осень"))
questions_list.append(Question('Какого месяца не существует?', "ноямбрь", "декабрь", "январь", "февраль"))

app = QApplication([])
window = QWidget()
window.setStyleSheet("background-color: rgb(70, 180,90); color: rgb(120,10,200);")
# Создаем панель вопроса
window.setWindowTitle('Memory Card')
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Вопрос')
window.score = 0
window.total = 0
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Ответ')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) #панель с вариантами ответов

# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста") 
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)



line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line1.addWidget(lb_Question) 
line2.addWidget(RadioGroupBox) 
line3.addWidget(btn_OK) 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addLayout(line1)
layout_card.addLayout(line2)
layout_card.addLayout(line3)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
line2.addWidget(AnsGroupBox)  

# RadioGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом

window.setLayout(layout_card)

def show_result(): #панель ответа
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question(): #панель с вопросом и вариантами ответов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #сбросить выбор кнопки

# def test(): ЭТО ВРЕМЕННАЯ ФУНКЦИЯ
#     if "Ответить" == btn_OK.text():
#         show_result()
#     else:
#         if "Ответить" == btn_OK.text():
#             show_question()
        
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) #вопрос
    lb_Correct.setText(q.right_answer) #
    show_question() #функция с панелью
def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer(): #проверка ответа
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика: \n Всего вопросов: ', window.total, '\n  Правильных ответов: ', window.score )
        print('Рейтинг: ', (window.score/window.total * 100), '%')


    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total * 100), '%')
   




def next_question():
    window.total += 1
    window.cur_question  += 1 #переход к сл вопросу
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 #если список вопосов закончился , то сачала 
    q = questions_list[window.cur_question] #взяли вопрос
    ask(q)
    window.total += 1


def  click_ok():
    if btn_OK.text() == "<b>Ответить</b>'":
        check_answer()
    else:
        next_question()

window.score = 0
window.total = 0
window.cur_question = -1 
next_question()
btn_OK.clicked.connect(click_ok)    
window.show() #показывать окно
app.exec() #сделать окно открытым 

'''Уже переделан под класс, но такое же осталось'''
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, 
# QRadioButton, QPushButton, QLabel)
# from random import shuffle
# class Question(): #
#     def __init__(self, question, right_answer, wrong1, wrong2, wrong3): #
#         self.question = question #
#         self.right_answer = right_answer #
#         self.wrong1 = wrong1 #
#         self.wrong2 = wrong2 #
#         self.wrong3 = wrong3 #
# app = QApplication([])
# window = QWidget()
# # Создаем панель вопроса
# window.setWindowTitle('Memory Card')
# btn_OK = QPushButton('Ответить')
# lb_Question = QLabel('Какое время года не бывает?')

# RadioGroupBox = QGroupBox("Варианты ответов")
# rbtn_1 = QRadioButton('Энцы')
# rbtn_2 = QRadioButton('Смурфы')
# rbtn_3 = QRadioButton('Чулымцы')
# rbtn_4 = QRadioButton('Алеуты')

# RadioGroup = QButtonGroup() 
# RadioGroup.addButton(rbtn_1)
# RadioGroup.addButton(rbtn_2)
# RadioGroup.addButton(rbtn_3)
# RadioGroup.addButton(rbtn_4)

# layout_ans1 = QHBoxLayout()   
# layout_ans2 = QVBoxLayout() 
# layout_ans3 = QVBoxLayout()

# layout_ans2.addWidget(rbtn_1) 
# layout_ans2.addWidget(rbtn_2)
# layout_ans3.addWidget(rbtn_3) 
# layout_ans3.addWidget(rbtn_4)
# layout_ans1.addLayout(layout_ans2)
# layout_ans1.addLayout(layout_ans3)

# RadioGroupBox.setLayout(layout_ans1) #панель с вариантами ответов

# # Создаем панель результата
# AnsGroupBox = QGroupBox("Результат теста") 
# lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
# lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа

# layout_res = QVBoxLayout()
# layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
# layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)



# line1 = QHBoxLayout()
# line2 = QHBoxLayout()
# line3 = QHBoxLayout()
# line1.addWidget(lb_Question) 
# line2.addWidget(RadioGroupBox) 
# line3.addWidget(btn_OK) 
# # Теперь созданные строки разместим друг под другой:
# layout_card = QVBoxLayout()
# layout_card.addLayout(line1)
# layout_card.addLayout(line2)
# layout_card.addLayout(line3)
# AnsGroupBox.setLayout(layout_res)
# AnsGroupBox.hide()
# line2.addWidget(AnsGroupBox)  

# # RadioGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом

# window.setLayout(layout_card)

# def show_result(): #панель ответа
#     RadioGroupBox.hide()
#     AnsGroupBox.show()
#     btn_OK.setText('Следующий вопрос')

# def show_question(): #панель с вопросом и вариантами ответов
#     RadioGroupBox.show()
#     AnsGroupBox.hide()
#     btn_OK.setText('Ответить')
#     RadioGroup.setExclusive(False)    
#     rbtn_1.setChecked(False)
#     rbtn_2.setChecked(False)
#     rbtn_3.setChecked(False)
#     rbtn_4.setChecked(False)
#     RadioGroup.setExclusive(True) #сбросить выбор кнопки

# # def test(): ЭТО ВРЕМЕННАЯ ФУНКЦИЯ
# #     if "Ответить" == btn_OK.text():
# #         show_result()
# #     else:
# #         if "Ответить" == btn_OK.text():
# #             show_question()
        
# answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
# def ask(q: Question): #
#     shuffle(answers) #
#     answers[0].setText(q.right_answer) #
#     answers[1].setText(q.wrong1) #
#     answers[2].setText(q.wrong2) #
#     answers[3].setText(q.wrong3) #
#     lb_Question.setText(q.question) #вопрос #
#     lb_Correct.setText(q.right_answer) #
#     show_question() #функция с панелью
# def show_correct(res):
#     lb_Result.setText(res)
#     show_result()


# def check_answer(): #ПРИ НАЖАТИИ НА КНОПКУ ПРАВИЛЬНО ИЛИ НЕПРАВИЛЬНО
#     if answers[0].isChecked():
#         show_correct('Правильно!')
#     else:
#         if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
#             show_correct('Неверно!')
# q = Question('Какого времени года не существует?', "веснуль", "лето", "зима", "осень") #
# ask(q) #
# btn_OK.clicked.connect(check_answer)    
# window.show() #показывать окно
# app.exec() #сделать окно открытым 











'''М2 У4. Приложение Memory Card. Ч3''' 
#Задать в случайной кнопке правильный ответ, в остальных –– неправильные.
#Задать текст вопроса и в форме ответа текст правильного ответа.
#Отобразить форму вопроса

# 1 Библиотека
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QButtonGroup, QRadioButton)
# from random import shuffle 
# '''перемешиваем варианты ответа'''

# class Question():
#     '''содержит вопрос, правильный ответ и три неправельных'''
#     def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
#         self.question = question
#         self.right_answer = right_answer
#         self.wrong1 = wrong1
#         self.wrong2 = wrong2
#         self.wrong3 = wrong3

# # 2 приложение
# app = QApplication([])
# # 3 окно приложения
# window = QWidget()
# # 4 Заголовок окна
# window.setWindowTitle('Memo Card')
# # 7 ИНТЕРФЕЙС ПРИЛОЖЕНИЯ Memory card
#             # ВИДЖЕТЫ:

# #СОЗДАЕМ ПАНЕЛЬ ВОПРОСА: 

# # кнопка ответа
# btn_OK = QPushButton('Ответить')
# # надпись с вопросом
# lb_Question = QLabel('Столица Урала?')

# # Группа на экране для переключателей с ответами
# RadioGroupBox = QGroupBox('Варианты ответов')
# # варианты ответов:
# rbtn_1 = QRadioButton('Екатеренбург')
# rbtn_2 = QRadioButton('Тюмень')
# rbtn_3 = QRadioButton('Тобольск')
# rbtn_4 = QRadioButton('Нижневаторовск')

# # ВСЕ ПЕРЕКЛЮЧАТЕЛИ ОБЪЕДИНЯЕМ В СПЕЦ.ГРУППУ, ЧТОБ МОЖНО ВЫБРАТЬ ТОЛЬКО ОДИН:
# RadioGroup = QButtonGroup()
# RadioGroup.addButton(rbtn_1)
# RadioGroup.addButton(rbtn_2)
# RadioGroup.addButton(rbtn_3)
# RadioGroup.addButton(rbtn_4)

# layout_ans1 = QHBoxLayout()   
# layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
# layout_ans3 = QVBoxLayout()
# layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
# layout_ans2.addWidget(rbtn_2)
# layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
# layout_ans3.addWidget(rbtn_4)


# layout_ans1.addLayout(layout_ans2)
# layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке


# RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


# AnsGroupBox = QGroupBox('Результат текста') 

# lb_Rezult = QLabel('Правильно!/Неправильно!') # здесь будет надпись верно или нет решение
# lb_Correct = QLabel('Верно это Екатеренбург!') # здесь пишем ответ, который угодали  

# layout_res = QVBoxLayout()
# layout_res.addWidget(lb_Rezult, alignment=(Qt.AlignLeft | Qt.AlignTop))
# layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch = 2)
# AnsGroupBox.setLayout(layout_res)

# layout_line1 = QHBoxLayout() # вопрос
# layout_line2 = QHBoxLayout() # варианты ответов или результат теста
# layout_line3 = QHBoxLayout() # кнопка "Ответить"


# layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# layout_line2.addWidget(RadioGroupBox)
# layout_line2.addWidget(AnsGroupBox) # включаем панель с ответами, но нужно скрыть с вопросами, чтоб не было все вместе:
# # RadioGroupBox.hide() это делали в 1 день, чтоб скрыть панель, чтоб посмотреть панель с ответами ет
# AnsGroupBox.hide() # скрывает панель ответов

# layout_line3.addStretch(1)
# layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
# layout_line3.addStretch(1)


# # Теперь созданные строки разместим друг под другой:
# layout_card = QVBoxLayout()


# layout_card.addLayout(layout_line1, stretch=2)
# layout_card.addLayout(layout_line2, stretch=8)
# layout_card.addStretch(1)
# layout_card.addLayout(layout_line3, stretch=1)
# layout_card.addStretch(1)
# layout_card.setSpacing(15) # пробелы между содержимым

# # ОБРАБОТКА НАЖАТИЯ ОТВЕТИТЬ или СЛЕДУЮЩИЙ ВОПРОС

# def show_result():
#     ''' показать панель ответов '''
#     RadioGroupBox.hide()
#     AnsGroupBox.show()
#     btn_OK.setText('Следующий вопрос')

# def show_question():
#     ''' показать панель вопросов'''
#     RadioGroupBox.show()
#     AnsGroupBox.hide()
#     btn_OK.setText('Ответить')
#     RadioGroup.setExclusive(False)# Снимаем ограничения для сброса выбора. 
#     # Снимаем выбор всех переключателей:
#     rbtn_1.setChecked(False)
#     rbtn_2.setChecked(False)
#     rbtn_3.setChecked(False)
#     rbtn_4.setChecked(False)
#     RadioGroup.setExclusive(True) # Вернели ограничения, чтоб только одна кнопка м.б. выбрана
# '''Создаем список с ответами:'''
# answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# def ask(q: Question):
#     '''Функция записывает значения вопроса и ответов  в соответствующие 
#     виджеты, при этом варианты ответов распределяются случ.образом '''
#     shuffle(answers)
#     answers[0].setText(q.right_answer)
#     answers[1].setText(q.wrong1)
#     answers[2].setText(q.wrong2)
#     answers[3].setText(q.wrong3)
#     lb_Question.setText(q.question)
#     lb_Correct.setText(q.right_answer)
#     show_question()

# def show_correct(res):
#     '''показать результат - установим переданный текст в надпись "результат"
#     и покажем новую панель'''
#     lb_Rezult.setText(res)
#     show_result()

# def check_answer():
#     '''если выбран вариант ответа, то проверить и показать панель ответов''' 
#     if answers[0].isChecked():
#         show_correct('Правильно!')
#     else:
#         if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
#             show_correct('Неверно!')

# window.setLayout(layout_card)
# q = Question('Столица Урала?', 'Екатеренбург', 'Тюмень', 'Тобольск', 'Нижневаторовск')
# ask(q)
# btn_OK.clicked.connect(check_answer) # проверяем, что панель ответов показывает при нажатии на кнопку

# window.resize(400,300)

# window.show()# 5 Показать окно
# app.exec_()# 6 оставить открытым пока не нажата кнопка входа




''' Часть 3 - 3_ДЕНЬ ч2 добавляем в список разные вопросы и переключение на сл вопрос''' 
## Задать в случайной кнопке правильный ответ, в остальных –– неправильные.
## Задать текст вопроса и в форме ответа текст правильного ответа.
## Отобразить форму вопроса

## 1 Библиотека
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QButtonGroup, QRadioButton)
# from random import shuffle 
# '''перемешиваем варианты ответа'''

# class Question():
#     '''содержит вопрос, правильный ответ и три неправельных'''
#     def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
#         self.question = question
#         self.right_answer = right_answer
#         self.wrong1 = wrong1
#         self.wrong2 = wrong2
#         self.wrong3 = wrong3
# '''Создаем список для разных вопросов'''
# questions_list = []
# questions_list.append(Question('Столица Урала?', 'Екатеренбург', 'Тюмень', 'Тобольск', 'Нижневаторовск'))
# questions_list.append(Question('Столица России?', 'Москва', 'Санкт-Питербург', 'Казань', 'Омска'))
# questions_list.append(Question('Столица Армении', 'Ереван', 'Москва', 'Ташкент', 'Двин'))


# # 2 приложение
# app = QApplication([])
# # 3 окно приложения
# window = QWidget()
# # 4 Заголовок окна
# window.setWindowTitle('Memo Card')
# # 7 ИНТЕРФЕЙС ПРИЛОЖЕНИЯ Memory card
#             # ВИДЖЕТЫ:

# #СОЗДАЕМ ПАНЕЛЬ ВОПРОСА: 

# # кнопка ответа
# btn_OK = QPushButton('Ответить')
# # надпись с вопросом
# lb_Question = QLabel('Столица Урала?')

# # Группа на экране для переключателей с ответами
# RadioGroupBox = QGroupBox('Варианты ответов')
# # варианты ответов:
# rbtn_1 = QRadioButton('Екатеренбург')
# rbtn_2 = QRadioButton('Тюмень')
# rbtn_3 = QRadioButton('Тобольск')
# rbtn_4 = QRadioButton('Нижневаторовск')

# # ВСЕ ПЕРЕКЛЮЧАТЕЛИ ОБЪЕДИНЯЕМ В СПЕЦ.ГРУППУ, ЧТОБ МОЖНО ВЫБРАТЬ ТОЛЬКО ОДИН:
# RadioGroup = QButtonGroup()
# RadioGroup.addButton(rbtn_1)
# RadioGroup.addButton(rbtn_2)
# RadioGroup.addButton(rbtn_3)
# RadioGroup.addButton(rbtn_4)

# layout_ans1 = QHBoxLayout()   
# layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
# layout_ans3 = QVBoxLayout()
# layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
# layout_ans2.addWidget(rbtn_2)
# layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
# layout_ans3.addWidget(rbtn_4)


# layout_ans1.addLayout(layout_ans2)
# layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке


# RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


# AnsGroupBox = QGroupBox('Результат текста') 

# lb_Rezult = QLabel('Правильно!/Неправильно!') # здесь будет надпись верно или нет решение
# lb_Correct = QLabel('Верно это Екатеренбург!') # здесь пишем ответ, который угодали  

# layout_res = QVBoxLayout()
# layout_res.addWidget(lb_Rezult, alignment=(Qt.AlignLeft | Qt.AlignTop))
# layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch = 2)
# AnsGroupBox.setLayout(layout_res)

# layout_line1 = QHBoxLayout() # вопрос
# layout_line2 = QHBoxLayout() # варианты ответов или результат теста
# layout_line3 = QHBoxLayout() # кнопка "Ответить"


# layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# layout_line2.addWidget(RadioGroupBox)
# layout_line2.addWidget(AnsGroupBox) # включаем панель с ответами, но нужно скрыть с вопросами, чтоб не было все вместе:
# # RadioGroupBox.hide() это делали в 1 день, чтоб скрыть панель, чтоб посмотреть панель с ответами ет
# AnsGroupBox.hide() # скрывает панель ответов

# layout_line3.addStretch(1)
# layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
# layout_line3.addStretch(1)


# # Теперь созданные строки разместим друг под другой:
# layout_card = QVBoxLayout()


# layout_card.addLayout(layout_line1, stretch=2)
# layout_card.addLayout(layout_line2, stretch=8)
# layout_card.addStretch(1)
# layout_card.addLayout(layout_line3, stretch=1)
# layout_card.addStretch(1)
# layout_card.setSpacing(15) # пробелы между содержимым

# # ОБРАБОТКА НАЖАТИЯ ОТВЕТИТЬ или СЛЕДУЮЩИЙ ВОПРОС

# def show_result():
#     ''' показать панель ответов '''
#     RadioGroupBox.hide()
#     AnsGroupBox.show()
#     btn_OK.setText('Следующий вопрос')

# def show_question():
#     ''' показать панель вопросов'''
#     RadioGroupBox.show()
#     AnsGroupBox.hide()
#     btn_OK.setText('Ответить')
#     RadioGroup.setExclusive(False)# Снимаем ограничения для сброса выбора. 
#     # Снимаем выбор всех переключателей:
#     rbtn_1.setChecked(False)
#     rbtn_2.setChecked(False)
#     rbtn_3.setChecked(False)
#     rbtn_4.setChecked(False)
#     RadioGroup.setExclusive(True) # Вернели ограничения, чтоб только одна кнопка м.б. выбрана
# '''Создаем список с ответами:'''
# answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# def ask(q: Question):
#     '''Функция записывает значения вопроса и ответов  в соответствующие 
#     виджеты, при этом варианты ответов распределяются случ.образом '''
#     shuffle(answers)
#     answers[0].setText(q.right_answer)
#     answers[1].setText(q.wrong1)
#     answers[2].setText(q.wrong2)
#     answers[3].setText(q.wrong3)
#     lb_Question.setText(q.question)
#     lb_Correct.setText(q.right_answer)
#     show_question()

# def show_correct(res):
#     '''показать результат - установим переданный текст в надпись "результат"
#     и покажем новую панель'''
#     lb_Rezult.setText(res)
#     show_result()

# def check_answer():
#     '''если выбран вариант ответа, то проверить и показать панель ответов''' 
#     if answers[0].isChecked():
#         show_correct('Правильно!')
#     else:
#         if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
#             show_correct('Неверно!')

# def next_question():
#     '''задать слепдующий вопрос из списка'''
#     # 'этой функции нужна переменная, в которой будет указываться номер текущего вопроса
#     # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта"(app или window)
#     # мы заведем ниже свойство window.cur_question
#     window.cur_question = window.cur_question + 1 # переходим к сл.вопросу
#     if window.cur_question >= len(questions_list):
#         window.cur_question = 0 # если список вопросов закончился, то идем сначала с 0
#     q = questions_list[window.cur_question] # взяли воспрос
#     ask(q)  # спросили

# def click_OK():
#     '''определяет, надо ли показывать др воспрос, либо проверить ответ на этот'''
#     if btn_OK.text() == 'Ответить':
#         check_answer() # проверка ответа
#     else:
#         next_question() # следующий вопрос 

# window.setLayout(layout_card)
# # Это мы убрали в список: q = Question('Столица Урала?', 'Екатеренбург', 'Тюмень', 'Тобольск', 'Нижневаторовск') 
# window.cur_question = - 1 
# # по-хорошему такие переменные должны быть свойствами, 
#                             # только надо писать класс, экземпляры которого получат такие свойства, 
#                             # но python позволяет создать свойство у отдельно взятого экземпляра
# # убрали в def next_question(): ask(q)
# btn_OK.clicked.connect(click_OK) # проверяем, что панель ответов показывает при нажатии на кнопку
# # все настроено, осталось задать вопрос и показать окно:
# next_question()
# window.resize(400,300)
# window.show()# 5 Показать окно
# app.exec_()# 6 оставить открытым пока не нажата кнопка входа








# '''Часть 4 - 4_ДЕНЬ ч1 добавляем Перемешать вопросы и подсчет правильных ответов.''' 
# # # Задать в случайной кнопке правильный ответ, в остальных –– неправильные.
# # #  Задать текст вопроса и в форме ответа текст правильного ответа.
# # #  Отобразить форму вопроса.'''

# # 1 Библиотека
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QButtonGroup, QRadioButton)
# from random import randint, shuffle 
# '''перемешиваем варианты ответа'''


# class Question():
#     '''содержит вопрос, правильный ответ и три неправельных'''
#     def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
#         self.question = question
#         self.right_answer = right_answer
#         self.wrong1 = wrong1
#         self.wrong2 = wrong2
#         self.wrong3 = wrong3
# '''Создаем список для разных вопросов'''
# questions_list = []
# questions_list.append(Question('Столица Урала?', 'Екатеренбург', 'Тюмень', 'Тобольск', 'Нижневаторовск'))
# questions_list.append(Question('Столица России?', 'Москва', 'Санкт-Питербург', 'Казань', 'Омска'))
# questions_list.append(Question('Столица Армении', 'Ереван', 'Москва', 'Ташкент', 'Двин'))


# # 2 приложение
# app = QApplication([])
# # 3 окно приложения
# window = QWidget()
# # 4 Заголовок окна
# window.setWindowTitle('Memo Card')
# # 7 ИНТЕРФЕЙС ПРИЛОЖЕНИЯ Memory card
#             # ВИДЖЕТЫ:

# #СОЗДАЕМ ПАНЕЛЬ ВОПРОСА: 

# # кнопка ответа
# btn_OK = QPushButton('Ответить')
# # надпись с вопросом
# lb_Question = QLabel('Столица Урала?')

# # Группа на экране для переключателей с ответами
# RadioGroupBox = QGroupBox('Варианты ответов')
# # варианты ответов:
# rbtn_1 = QRadioButton('Екатеренбург')
# rbtn_2 = QRadioButton('Тюмень')
# rbtn_3 = QRadioButton('Тобольск')
# rbtn_4 = QRadioButton('Нижневаторовск')

# # ВСЕ ПЕРЕКЛЮЧАТЕЛИ ОБЪЕДИНЯЕМ В СПЕЦ.ГРУППУ, ЧТОБ МОЖНО ВЫБРАТЬ ТОЛЬКО ОДИН:
# RadioGroup = QButtonGroup()
# RadioGroup.addButton(rbtn_1)
# RadioGroup.addButton(rbtn_2)
# RadioGroup.addButton(rbtn_3)
# RadioGroup.addButton(rbtn_4)

# layout_ans1 = QHBoxLayout()   
# layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
# layout_ans3 = QVBoxLayout()
# layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
# layout_ans2.addWidget(rbtn_2)
# layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
# layout_ans3.addWidget(rbtn_4)


# layout_ans1.addLayout(layout_ans2)
# layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке


# RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


# AnsGroupBox = QGroupBox('Результат текста') 

# lb_Rezult = QLabel('Правильно!/Неправильно!') # здесь будет надпись верно или нет решение
# lb_Correct = QLabel('Верно это Екатеренбург!') # здесь пишем ответ, который угодали  

# layout_res = QVBoxLayout()
# layout_res.addWidget(lb_Rezult, alignment=(Qt.AlignLeft | Qt.AlignTop))
# layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch = 2)
# AnsGroupBox.setLayout(layout_res)

# layout_line1 = QHBoxLayout() # вопрос
# layout_line2 = QHBoxLayout() # варианты ответов или результат теста
# layout_line3 = QHBoxLayout() # кнопка "Ответить"


# layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# layout_line2.addWidget(RadioGroupBox)
# layout_line2.addWidget(AnsGroupBox) # включаем панель с ответами, но нужно скрыть с вопросами, чтоб не было все вместе:
# # RadioGroupBox.hide() это делали в 1 день, чтоб скрыть панель, чтоб посмотреть панель с ответами ет
# AnsGroupBox.hide() # скрывает панель ответов

# layout_line3.addStretch(1)
# layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
# layout_line3.addStretch(1)


# # Теперь созданные строки разместим друг под другой:
# layout_card = QVBoxLayout()


# layout_card.addLayout(layout_line1, stretch=2)
# layout_card.addLayout(layout_line2, stretch=8)
# layout_card.addStretch(1)
# layout_card.addLayout(layout_line3, stretch=1)
# layout_card.addStretch(1)
# layout_card.setSpacing(15) # пробелы между содержимым

# # ОБРАБОТКА НАЖАТИЯ ОТВЕТИТЬ или СЛЕДУЮЩИЙ ВОПРОС

# def show_result():
#     ''' показать панель ответов '''
#     RadioGroupBox.hide()
#     AnsGroupBox.show()
#     btn_OK.setText('Следующий вопрос')

# def show_question():
#     ''' показать панель вопросов'''
#     RadioGroupBox.show()
#     AnsGroupBox.hide()
#     btn_OK.setText('Ответить')
#     RadioGroup.setExclusive(False)# Снимаем ограничения для сброса выбора. 
#     # Снимаем выбор всех переключателей:
#     rbtn_1.setChecked(False)
#     rbtn_2.setChecked(False)
#     rbtn_3.setChecked(False)
#     rbtn_4.setChecked(False)
#     RadioGroup.setExclusive(True) # Вернели ограничения, чтоб только одна кнопка м.б. выбрана
# '''Создаем список с ответами:'''
# answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# def ask(q: Question):
#     '''Функция записывает значения вопроса и ответов  в соответствующие 
#     виджеты, при этом варианты ответов распределяются случ.образом '''
#     shuffle(answers)
#     answers[0].setText(q.right_answer)
#     answers[1].setText(q.wrong1)
#     answers[2].setText(q.wrong2)
#     answers[3].setText(q.wrong3)
#     lb_Question.setText(q.question)
#     lb_Correct.setText(q.right_answer)
#     show_question()

# def show_correct(res):
#     '''показать результат - установим переданный текст в надпись "результат"
#     и покажем новую панель'''
#     lb_Rezult.setText(res)
#     show_result()
# window.score = 0 # подсчет верных ответов
# window.total = 0 # подсчет всего вопросов
# def check_answer():
#     '''если выбран вариант ответа, то проверить и показать панель ответов''' 
#     if answers[0].isChecked():
#         show_correct('Правильно!')
#         window.score += 1
#         print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
#         print('Рейтинг: ', (window.score/window.total*100), '%')
#     else:
#         if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
#             show_correct('Неверно!')
#             print('Рейтинг: ', (window.score/window.total*100), '%')


# def next_question():
#     '''задать следующий вопрос из списка'''
#     # 'этой функции нужна переменная, в которой будет указываться номер текущего вопроса
#     # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта"(app или window)
#     # мы заведем ниже свойство window.cur_question
#     # Убераем переключение по порядку и делаем верно:  window.cur_question = window.cur_question + 1 # переходим к сл.вопросу
#     # if window.cur_question >= len(questions_list):
#     #     window.cur_question = 0 # если список вопросов закончился, то идем сначала с 0
#     ''' задает СЛУЧАЙНЫЙ ВОПРОС ИЗ СПИСКА (МЫ РАНЕЕ ЗАДАВАЛИ СЛЕДУЮЩИЙ)'''
#     window.total += 1
#     print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
#     cur_question = randint(0, len(questions_list) - 1)  # нам не нужно старое значение, 
#                                                         # поэтому можно использовать локальную переменную! 
#             # случайно взяли вопрос в пределах списка
#             # если внести около сотни слов, то редко будет повторяться


    
#     q = questions_list[cur_question] # взяли воспрос
#     ask(q)  # спросили

# def click_OK():
#     '''определяет, надо ли показывать др воспрос, либо проверить ответ на этот'''
#     if btn_OK.text() == 'Ответить':
#         check_answer() # проверка ответа
#     else:
#         next_question() # следующий вопрос 

# window.setLayout(layout_card)
# # Это мы убрали в список: q = Question('Столица Урала?', 'Екатеренбург', 'Тюмень', 'Тобольск', 'Нижневаторовск') 
# # Убрали: window.cur_question = - 1 
# # по-хорошему такие переменные должны быть свойствами, 
#                             # только надо писать класс, экземпляры которого получат такие свойства, 
#                             # но python позволяет создать свойство у отдельно взятого экземпляра
# # убрали в def next_question(): ask(q)
# btn_OK.clicked.connect(click_OK) # проверяем, что панель ответов показывает при нажатии на кнопку
# # все настроено, осталось задать вопрос и показать окно:
# next_question()
# window.resize(400,300)
# window.show()# 5 Показать окно
# app.exec_()# 6 оставить открытым пока не нажата кнопка входа