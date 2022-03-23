from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_cd = CallbackData("show_menu", "level", "language", "main_menu", "questions", "question_id")

def make_callback_data(level, language="0", main_menu="0", questions="0", question_id="0"):
    return menu_cd.new(level=level, 
                        language=language, 
                        main_menu=main_menu, 
                        questions=questions,
                        in_questions = in_questions,
                        question_id=question_id)

async def language_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()

    languages = {"kaz" :"Қазақша", "rus" :"Русский"}
    for key, value in languages.items():

        button_text = value
        callback_data = make_callback_data(level = CURRENT_LEVEL+1, language = key)

        markup.insert(
            InlineKeyboardButton(text = button_text, callback_data=callback_data)
        )
    return markup

async def main_menu_keyboard(language):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    main_menu_data = {
        "kaz": {
            "main_menu_1_kaz": "Оқуға түсудің тәртібі"
        },
        "rus": {
            "main_menu_1_rus": "Правила поступления"
        }

    }

    main_menu = main_menu_data[language]
    for key, value in main_menu.items():
        button_text = value
        callback_data = make_callback_data(level = CURRENT_LEVEL+1, language = language, main_menu = key)

        markup.insert(
            InlineKeyboardButton(text = button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data = make_callback_data(level = CURRENT_LEVEL-1, language = language)
        )
    )

    return markup

async def questions_keyboard(language, main_menu):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)

    questions = {
        "kaz":{
            "main_menu_1_kaz": {
                "main_menu_1_kaz_btn1":"Әскери кафедрада кім оқи алады?",
                "main_menu_1_kaz_btn2":"Іріктеу конкурсына қатысу үшін құжаттарды ұсынудың мерзімдері?",
                "main_menu_1_kaz_btn3":"Әскери кафедраға түсу үшін қандай құжаттар қажет?",
                "main_menu_1_kaz_btn4":"Іріктеу конкурсына қатысу үшін құжаттарды ұсынудың тәртібі қандай?",
                "main_menu_1_kaz_btn5":"Медициналық куәландыруды қай жерде өтуге болады?",
                "main_menu_1_kaz_btn6":"Медициналық куәландырудан өту үшін қандай анықтамалар (құжаттар) жинау қажет?",
                "main_menu_1_kaz_btn7":"Іріктеу конкурсынан кім өтеді?",
                "main_menu_1_kaz_btn8":"Дене даярлығын тексеру үшін қандай нормативтер?"
            }
        },
        "rus":{
            "main_menu_1_rus":{
                "main_menu_1_rus_btn1":"Кто может обучаться на военной кафедре?",
                "main_menu_1_rus_btn2":"Сроки подачи документов для участия в отборочном конкурсе?",
                "main_menu_1_rus_btn3":"Какие документы нужны для поступления на военную кафедру?",
                "main_menu_1_rus_btn4":"Какой порядок подачи документов для участия в отборочном конкурсе?",
                "main_menu_1_rus_btn5":"Где можно пройти медицинское освидетельствование?",
                "main_menu_1_rus_btn6":"Какие справки (документы) нужно собрать для прохождения медицинского освидетельствования?",
                "main_menu_1_rus_btn7":"Как проходит отборочный конкурс?",
                "main_menu_1_rus_btn8":"Какие нормативы для проверки физической подготовленности?"
            }
        }
    }

    for key, value in questions[language][main_menu].items():
        button_text = value
        callback_data = make_callback_data(level = CURRENT_LEVEL+1, language = language, main_menu = main_menu, questions = key)

        markup.insert(
            InlineKeyboardButton(text = button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data = make_callback_data(level = CURRENT_LEVEL-1, language = language, main_menu = main_menu)
        )
    )

    return markup

def question_keyboard(language, main_menu, questions, question_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад", 
            callback_data = make_callback_data(
                level = CURRENT_LEVEL-1, 
                language = language, 
                main_menu= main_menu,
                questions=questions,
                question_id=question_id
            )
        )
    )

    return markup