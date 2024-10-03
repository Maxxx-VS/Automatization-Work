import pandas as pd

def ext():
    # загрузка данных
    df = pd.read_excel("Python/Книга1.xlsx")

    list = ['Вальцы И-2222Б :: Гибка на вальцах', 'FG evo 2000 :: Сверление отверстий, фрезерование, маркировка', 'Машина для термической резки труб "Орбита" :: Резка трубы',
            'Машина для термической резки труб "Орбита" :: Резка трубы под углом', 'Машина для термической резки труб "Орбита" :: Резка трубы, фаска, врезка',
            'Дрель ручная :: Сверление отверстий', 'Листогиб :: Гибка', 'Машина для правки уголка ASM200 :: Правка', 'Накатной станок :: Накатка на круге',
            'ОГМ :: Механическая обработка', 'ОГМ :: Сборка', 'ОГМ :: Слесарная обработка', 'П/а резьбонарезной станок :: Нарезка резьбы', 'Пила ленточная :: Резка под углом',
            'Пила ленточная ОГМ :: Резка', 'Пост УЗК :: Проверка на сплошность УЗК', 'Пост газовой резки :: Ручная газовая резка', 'Пост гибки :: Гибка ручная с подогревом по радиусу',
            'Пост маркировки :: Маркировка', 'Пост сборки-стыковки ЗУ :: Стыковка', 'Пост сварки-стыковки ЗУ :: Стыковка', 'Пост стыковки :: Стыковка', 'Пресс :: Вырубка сегмента',
            'Пресс :: Гибка', 'Пресс :: Маркировка', 'Пресс :: Подрезка скосов', 'Пресс :: Размалковка уголков', 'Пресс :: Смалковка уголков', 'Пресс :: Штамповка листа',
            'Токарновинтор. Станок :: Нарезка резьбы', 'Токарновинтор. Станок :: Токарная обработка', 'Углошлифовальная машина :: Резка',
            'Радиально-сверлильный станок :: Сверление отверстий', 'Ручная сверлильная машина :: Сверление отверстий',
            'Телега транспортировочная :: Сквозная передача из ЦС в ЦГЦ', 'Углошлифовальная машина :: Разделка кромки под сварку',
            'Углошлифовальная машина :: Резка', 'Установка ручной плазменной резки КЕДР CUT 100 PRO :: Резка скосов',
            'Установка ручной плазменной резки КЕДР CUT 100 PRO :: Вырезка сегмента', 'Фрезерный станок Marghina :: Фрезерование']

    list_2 = ['Voortman V304', 'Гильотина', 'Пила ленточная', 'Пресс',
                'Уголковая линия 2030AA',
                'Уголковая линия VP-164 8D',
                'Уголковая линия VP-184 6D',
                'Уголковая линия VPX-94 2G',
                'Установка лазерной резки']

    total_m = 0
    total_s = 0

    # удаление лишних столбцов и начальных строк
    df.drop(df.columns[[1,3,4,5,6,7]], axis=1, inplace=True)
    df = df.drop(index=[0,1])

    # замена названий столбцов
    df.rename(columns={'Отчет по невыполненным ССЗ по РЦ ЗУ в разрезе металлопроката':'Центр'}, inplace=True)
    df.rename(columns={'Unnamed: 2':'ССЗ'}, inplace=True)
    df.rename(columns={'Unnamed: 8':'Итого'}, inplace=True)

    # удаление всех лишних строк циклом
    for i in list:
        df.drop(df.index[df['Центр'] == i], inplace=True)

    # работа с данными (отбрасываем лишнии токены)
    df['Центр'] = (df['Центр']).apply(lambda x: str(x).split(' ::')[0])

    # вывод результата
    print("\n", "* * * * * * * * * * * * НА РУКАХ ССЗ: * * * * * * * * * * * *", '\n')
    for i in list_2:
        df_new = df[df['Центр'] == i]
        count = len(df_new["ССЗ"].unique())
        total_s += count
        print(i, "=>", count, "штук.")
        
    print(f'\nВСЕГО => {round(total_s, 1)} штук\n')
    
    
    print("* * * * * * * * * * * * ОБЩАЯ МАССА ССЗ: * * * * * * * * * * * *", "\n")
    for i in list_2:
        resalt = round((df.loc[df["Центр"] == i, "Итого"].sum())/1000, 1)
        total_m += resalt
        print(f'{i} => {resalt} тонн')

    print(f'\nВСЕГО => {round(total_m, 1)} тонн\n')


ext()