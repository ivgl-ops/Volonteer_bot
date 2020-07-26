import vk_api
import random

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType


token = '7c5ce0d5dfeb8c3104d522c567b5910c185a98c937cd0f400db699b6745e32a00e65c28691a134ace8a05'
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
greeting_lst = ['привет','хеллоу','здарова','вассап','здрасте','приветик','начать','Салом алейкум'
                'здравствуйте','добрый день','доброе утро','здравствуй']
print("Бот запущен")

def open_in(x):
    f = open(x, 'r', encoding='Utf-8')
    text = f.read()
    f.close()
    return text

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    if response == 'начать':
        keyboard.add_button('Как стать волонтером? 🙋‍♀', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Мероприятия 🎟', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Чем я могу помочь?🙋‍♂', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('О нас 👩‍💻', color=VkKeyboardColor.PRIMARY )
        keyboard.add_line()
        keyboard.add_button('далее')

    elif response == 'мероприятия 🎟':
        keyboard.add_button('Красноярский экономический форум 2020 💵', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Забег 2020 🤾', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Кейсовый чемпионат «Case Roads» 💼', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_openlink_button('Все мероприятия','http://xn--80aejrhmfbnher.xn--p1ai/events/')
        keyboard.add_line()
        keyboard.add_button('начать', color=VkKeyboardColor.NEGATIVE)

    elif response == 'далее':
        keyboard.add_button('Наш магазин 🔮')
        keyboard.add_line()
        keyboard.add_openlink_button('Наш сайт', 'http://xn--80aejrhmfbnher.xn--p1ai/')
        keyboard.add_line()
        keyboard.add_button('назад',color=VkKeyboardColor.NEGATIVE)

    elif response == 'назад':
        keyboard.add_button('Как стать волонтером? 🙋‍♀', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Мероприятия 🎟', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('О нас 👩‍💻', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('далее')

    elif response == 'забег 2020 🤾':
        keyboard.add_openlink_button('Подать заявку', 'http://xn--80aejrhmfbnher.xn--p1ai/events/2524/')
        keyboard.add_line()
        keyboard.add_button('мероприятия 🎟',color=VkKeyboardColor.NEGATIVE)

    elif response == 'наш магазин 🔮':
        keyboard.add_openlink_button('Перейти в магазин','http://xn--80aejrhmfbnher.xn--p1ai/shop/')
        keyboard.add_line()
        keyboard.add_button('начать', color=VkKeyboardColor.NEGATIVE)

    elif response == 'чем я могу помочь?🙋‍♂':
        keyboard.add_openlink_button('помочь ветеранам','https://today.sberbankvmeste.ru/story/NineMay2020')
        keyboard.add_line()
        keyboard.add_openlink_button('помочь больным детям', 'https://www.detis.ru/')
        keyboard.add_line()
        keyboard.add_openlink_button('помочь бездомным животным', 'https://rayfund.ru/get_involved/')
        keyboard.add_line()
        keyboard.add_button('следующая страница', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('начать', color=VkKeyboardColor.NEGATIVE)

    elif response == 'следующая страница':
        keyboard.add_openlink_button('Стать донором', 'http://www.kkck.ru/')
        keyboard.add_line()
        keyboard.add_button('нaзад',color=VkKeyboardColor.NEGATIVE)

    elif response == 'нaзад':
        keyboard.add_openlink_button('помочь ветеранам', 'https://today.sberbankvmeste.ru/story/NineMay2020')
        keyboard.add_line()
        keyboard.add_openlink_button('помочь больным детям', 'https://www.detis.ru/')
        keyboard.add_line()
        keyboard.add_openlink_button('помочь бездомным животным', 'https://rayfund.ru/get_involved/')
        keyboard.add_line()
        keyboard.add_button('следующая страница', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('начать', color=VkKeyboardColor.NEGATIVE)

    elif response == 'кейсовый чемпионат «case roads» 💼':
        keyboard.add_openlink_button('Подать заявку', 'http://xn--80aejrhmfbnher.xn--p1ai/events/2509/')
        keyboard.add_line()
        keyboard.add_button('мероприятия 🎟', color=VkKeyboardColor.NEGATIVE)

    elif response == 'красноярский экономический форум 2020 💵':
        keyboard.add_openlink_button('Подать заявку', 'http://xn--80aejrhmfbnher.xn--p1ai/events/2496/')
        keyboard.add_line()
        keyboard.add_button('мероприятия 🎟',color=VkKeyboardColor.NEGATIVE)

    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()
    keyboard = keyboard.get_keyboard()
    return keyboard

def send_message(vk_session, id_type, id, message=None, keyboard=None, attachment=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648),
                                       'keyboard': keyboard, 'attachment': attachment })
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "начать" :
                send_message(vk_session, 'user_id', event.user_id, message="Выберите нужный пункт", keyboard=keyboard)

            elif response == "о нас 👩‍💻":
                send_message(vk_session,'user_id', event.user_id, message=open_in("About.txt"), attachment='photo-197331641_457239017')
                send_message(vk_session, 'user_id', event.user_id, message=" ", attachment='video-73778585_456239026')

            elif response == "мероприятия 🎟":
                send_message(vk_session,'user_id', event.user_id,message="Выберите интересующее вас мероприятие", keyboard=keyboard)

            elif response == "забег 2020 🤾":
                send_message(vk_session, 'user_id', event.user_id, message=open_in("Text\zabeg.txt"), keyboard=keyboard, attachment='photo-197331641_457239018')

            elif response == "кейсовый чемпионат «case roads» 💼":
                send_message(vk_session, 'user_id', event.user_id, message=open_in("Text\Champ"), keyboard=keyboard, attachment='photo-197331641_457239019')

            elif response == "как стать волонтером? 🙋‍♀":
                send_message(vk_session, 'user_id', event.user_id, message=open_in("Text\how_registration"),attachment='photo-197331641_457239022')

            elif response == "красноярский экономический форум 2020 💵":
                send_message(vk_session, 'user_id', event.user_id, message=open_in("Text\Celebration"), keyboard=keyboard, attachment='photo-197331641_457239020')
            elif response == "чем я могу помочь?🙋‍♂":
                send_message(vk_session, 'user_id', event.user_id, message="Выберите нужный пункт", keyboard=keyboard)

            elif response == "следующая страница":
                send_message(vk_session, 'user_id', event.user_id, message="Выберите нужный пункт", keyboard=keyboard)

            elif response == "нaзад":
                send_message(vk_session, 'user_id', event.user_id, message="Выберите нужный пункт",keyboard=keyboard)

            elif response == "далее":
                send_message(vk_session, 'user_id', event.user_id, message="Выберите нужный пункт",keyboard=keyboard)
            elif response == "назад":
                send_message(vk_session, 'user_id', event.user_id, message="Выберите нужный пункт",keyboard=keyboard)
            elif response == "наш магазин 🔮":
                send_message(vk_session, 'user_id', event.user_id, message=open_in("Text\Shop"),keyboard=keyboard, attachment='photo-197331641_457239021')
            else:
                send_message(vk_session,'user_id', event.user_id, message='Такой комманды не существует. Попробуйте еще раз!')
