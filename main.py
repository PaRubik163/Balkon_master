from aiogram import Bot, Dispatcher,executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import ReplyKeyboardMarkup


bot = Bot('6921746848:AAHkrqMHothtZy9gfSITxqRKWbhZzILFNxI')
dp = Dispatcher(bot=bot)

                                                                # KNOPKI
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Остекление балкона') \
    .add('Отделка балконов') \
    .add('Объединение с комнатой') \
    .add('Контакты') \
    .add('Сроки')

                                                        # Кнопки видов остекления
osteklenie_main = ReplyKeyboardMarkup(resize_keyboard=True)
osteklenie_main.add('Холодное остекление') \
    .add('Теплое остекление') \
    .add('Вернуться назад')

                                                                # Веб - Кнопки
holod_osteklenie = ReplyKeyboardMarkup(resize_keyboard=True)
holod_osteklenie.add(types.KeyboardButton('Холодное остекление', web_app=WebAppInfo(
    url='https://www.panokna.ru/osteklenie-balkonov/holodnoe/')))
holod_osteklenie.add('Вернуться назад')

teploe_osteklenie = ReplyKeyboardMarkup(resize_keyboard=True)
teploe_osteklenie.add(types.KeyboardButton('Тёплое остекление', web_app=WebAppInfo(
    url='https://www.panokna.ru/osteklenie-balkonov/teploe/')))
teploe_osteklenie.add('Вернуться назад')

otdelkabalkon = ReplyKeyboardMarkup(resize_keyboard=True)
otdelkabalkon.add(
    types.KeyboardButton('Отделка балконов', web_app=WebAppInfo(url='https://www.panokna.ru/otdelka_balkonov/')))
otdelkabalkon.add('Вернуться назад')

obidenenie = ReplyKeyboardMarkup(resize_keyboard=True)
obidenenie.add(types.KeyboardButton('Объединение с комнатой', web_app=WebAppInfo(
    url='https://www.panokna.ru/stati/obedinenie_balkona_s_komnatoj/')))
obidenenie.add('Вернуться назад')


                                                                        # ОБРАБОТЧИКИ
@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, это сервис по ремонту балконов.', reply_markup=main)

                                                                        # Остекление


@dp.message_handler(text='Остекление балкона')
async def ostekl_func(message: types.Message):
    await message.answer(f'Выберите, что именно вы хотите.',
                         reply_markup=osteklenie_main)


@dp.message_handler(text='Холодное остекление')
async def holod_ostek_func(message: types.Message):
    await message.answer(f'Используется алюминиевый профиль, который не защищает от холода как пластиковые окна, '
                         f'но являются надежной преградой для осадков, ветра, пыли, птиц.\n'
                         f'Все вопросы okno@panokna.ru или 84952418116', reply_markup=holod_osteklenie)


@dp.message_handler(text='Теплое остекление')
async def teploe_osteklen_func(message: types.Message):
    await message.answer('Осуществляется с использованием пластиковых окон,'
                         ' которые эффективно защитят от осадков, уличной пыли, '
                         'а при грамотном утеплении позволят использовать помещение с комфортом круглый год.\n'
                         f'Все вопросы okno@panokna.ru или 84952418116', reply_markup=teploe_osteklenie)

                                                            # Отделка балконов


@dp.message_handler(text='Отделка балконов')
async def otdelka(message: types.Message):
    await message.answer(f'Утепление, объединение с комнатой, вынос, монтаж крыши. Любые виды работ по внутренней '
                         f'и внешней отделке.Сможем воплотить любые дизайнерские решения или подстроиться под ограниченный бюджет.\n'
                         f'Все вопросы okno@panokna.ru или 84952418116'
                         , reply_markup=otdelkabalkon)


@dp.message_handler(text='Объединение с комнатой')
async def komnata_gang(message: types.Message):
    await message.answer(
        f'Объединение кухни и комнаты, нескольких комнат, балкона с комнатой – популярный современный способ увеличить жилую площадь квартиры.'
        f' Особенно, это касается небольших квартир в старых домах. '
        f'При объединении балкона и комнаты Вы получаете лишние квадратные метры площади, которые можно использовать для создания игровой комнаты для детей, '
        f'кабинета или помещения для отдыха.\n'
        f'Все вопросы okno@panokna.ru или 84952418116'
        , reply_markup=obidenenie)

                                                                    # Вернуться назад


@dp.message_handler(text='Вернуться назад')
async def vernutsi(message: types.Message):
    await message.answer(f'Выберите, что именно вы хотите.', reply_markup=main)


@dp.message_handler(text='Сроки')
async def srok(message: types.Message):
    await message.answer(f'СРОКИ ВЫПОЛНЕНИЯ РАБОТ ПО ОСТЕКЛЕНИЮ, ОТДЕЛКЕ И УТЕПЛЕНИЮ БАЛКОНОВ И ЛОДЖИЙ.\n'

                         f'1 день Производство оконных конструкций.\n'

                         f'1 день Доставка отделочных материалов.\n'

                         f'1 день Доставка и остекление.\n'

                         f'1-2 дня Работы по утеплению и обшивке (в зависимости от объема работ).')


@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer('E-mail: okno@panokna.ru\n'
                         f'Наш телефон: 84952418116\n'
                         f'Мы ждём Ваших звонков 7 дней в неделю. \n'
                         f'Пн - Пт 8:00 - 20:00\n'
                         f'Сб - Вс 9:00 - 19:00')


@dp.message_handler()
async def all(message: types.Message):
    await message.reply(f'Я вас не понимаю')


if __name__ == '__main__':
    executor.start_polling(dp)



# 1] Сделанно для сайта - 'https://www.panokna.ru/osteklenie-balkonov/?utm_source=Yandex.Direct&utm_medium=cpc&utm_campaign=Moskva%7CPoisk%7CKategoriya%7COsteklenie_Balkonov&utm_content=4520497624&utm_term=ST:search%7CS:none%7CAP:no%7CPT:premium%7CP:1%7CDT:desktop%7CRI:213%7CCI:28820391%7CGI:2817338584%7CPI:10442716845%7CAI:4520497624%7CRT:10442716845%7CKW:холодное%20остекление%20балконов%7CRN:Москва&yclid=10401149862690160639'

# 2] Создатель: 1) +79151850797 - номер телефона
#               2) rubengevorkan40203@gmail.com - почта
#               3) @ooyble - телеграмм

# 3]P.S Разработка телеграмм ботов и Django проектов под ключ