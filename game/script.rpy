﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Баклажановый
define Will = Character("Уильям", color='#990066', image = "will")
# Лягушка в обмороке (серенький)
define leo = Character("Лайонель", color='#7b917b', image = "leo")
# Макароны и сыр (розовенький)
define g = Character("Грегори", color='#ffbd88', image = "greg")
# Влюбленная жаба (зелененький)
define s = Character("Сара", color='#3caa3c')
# Яйцо дрозда (бирюзовый)
define a = Character("Артур", color='#00cccc')
# Кукурузно желтый
define i = Character("Издатель", color='#e4a010')
# Розовый "Пощекочи меня"
define d = Character("Николас", color='#fc89ac')
# Сигнальный чёрный
define n = Character("Незнакомец", color='#282828')

# переменные
define sc10one = False
define sc10two = False
define sc15two = False
define three = False
define sc17one = False
define sc17two = False

# Иниты (что бы это ни значило!)

init:
    $ noisedissolve = ImageDissolve(im.Tile("images/noisetile.png"), 1.0, 1)
# hide screen daytime with noisedissolve
    $ blod = ImageDissolve(im.Tile("blod.png"), 3.0, 30, reverse=False)
    $ memory = ImageDissolve(im.Tile("memory.png"), 2.0, 20)
    $ flash2 = ImageDissolve(im.Tile("flash.png"), 2.0, 20)
init:
    image koridor2 = "location/koridor"
    image kamin2 = "kamin"
    image kabinet2 = "kabinet"
    $ dt = "ночь"
screen daytime:
    if dt == "пыль":
        add "#7679"
    if dt == "ночь":
        add "#000b"


init:
    image gregory normal = "character/Gregory/gregor normal.png"
    image greg normal = im.MatrixColor ("character/Gregory/gregor normal.png", im.matrix.opacity(0.65))
    image gregor ghost1 = "character/Gregory/greg 2.png"
    image greg ghost = im.MatrixColor ("character/Gregory/greg 2.png", im.matrix.opacity(0.65))
    image gregor ghost2 = "character/Gregory/greg 3.png"
    image greg ghost smile = im.MatrixColor ("character/Gregory/greg 3.png", im.matrix.opacity(0.65))
    image gregor ghost3 = "character/Gregory/greg 1.png"
    image greg ghost evil smile = im.MatrixColor ("character/Gregory/greg 1.png", im.matrix.opacity(0.65))
    image gregor ghost4 = "character/Gregory/greg 4.png"
    image greg ghost enemy = im.MatrixColor ("character/Gregory/greg 4.png", im.matrix.opacity(0.65))
    
    image lionel1 = "character/Lionel/leo normal.png"
    image leo ghost = im.MatrixColor ("character/Lionel/leo normal.png", im.matrix.opacity(0.65))
    image lionel2 = "character/Lionel/leo vspom.png"
    image leo ghost vspom = im.MatrixColor ("character/Lionel/leo vspom.png", im.matrix.opacity(0.65))
    image lionel3 = "character/Lionel/leo pe4alko.png"
    image leo ghost pe4al = im.MatrixColor ("character/Lionel/leo pe4alko.png", im.matrix.opacity(0.65))
    image lionel4 = "character/Lionel/le0_ogon.png"
    image leo ghost fire = im.MatrixColor ("character/Lionel/le0_ogon.png", im.matrix.opacity(0.65))
    image lionel4 = "character/Lionel/le0bezlitsa.png"
    image leo ghost die = im.MatrixColor ("character/Lionel/le0bezlitsa.png", im.matrix.opacity(0.65))
    
    image william1 = "character/William/will na gg.png"
    image will ghost = im.MatrixColor ("character/William/will na gg.png", im.matrix.opacity(0.65))
    image william2 = "character/William/will 3apisi.png"
    image will ghost ob = im.MatrixColor ("character/William/will 3apisi.png", im.matrix.opacity(0.65))
    image william3 = "character/William/will o4ki.png"
    image will ghost o4ki = im.MatrixColor ("character/William/will o4ki.png", im.matrix.opacity(0.65))
    image william4 = "character/William/will vo3m.png"
    image will ghost evil = im.MatrixColor ("character/William/will vo3m.png", im.matrix.opacity(0.65))
    
    image nic1 = "character/nic dead.png"
    image nic ghost = im.MatrixColor ("character/nic dead.png", im.matrix.opacity(0.65))
    
    image sara1 = "character/sara dead.png"
    image sara ghost = im.MatrixColor ("character/sara dead.png", im.matrix.opacity(0.65))
    image sara2 = "character/sara evil.png"
    image sara ghost evil = im.MatrixColor ("character/sara evil.png", im.matrix.opacity(0.65))
    
    image smert = Solid("#980002")

init:
    $ flash = Fade(.25, 0, .75, color="#fff8dc")

init:
    $ timer_range = 0
    $ timer_jump = 0
    $ renpy.music.register_channel("bgloop", mixer="sfx", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgloop2", mixer="sfx", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgsfx1", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgsfx2", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgsfx3", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgsfx4", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)


init:
    transform cred_up:
        yalign -1.5
        linear 10 yalign 0.5

label splashscreen:
    scene black
    with Pause(1)

    show text "Content Warning: Offensive language" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene news

    # Газета

    a "Вчера полиция обнаружила моего деда мертвым."
    a "Испытываю ли я по этому поводу какие-либо чувства? Нет."
    a "Мой дед был знаменитым писателем. Славу ему принесла публикация первой книги, затем последовали сплошные творческие неудачи. Критики и пресса издевались над ним и его новыми нелепыми романами."
    a "Одни писали, что всему виной какая-то девушка-хиппи и наркота, другие сплетничали о тяжелом алкоголизме."
    a "Мне, если честно, все равно."

    scene dom photo with flash2

    a "Я не видел его с самого детства. Все воспоминания о нем - светлые, но ребенку все люди кажутся хорошими."
    a "Факт в том, что дед бросил нас с матерью, когда нам было очень тяжело после смерти отца. Мама не говорила мне, но она часто писала деду, просила о помощи."
    a "Он не снизошел."
    a "Не соизволил даже ответить."
    a "А я, видимо, слишком быстро подрос и перестал напоминать милого питомца. Родство ведь не повод для сострадания?"

# Сам особняк

    scene dom with memory

    a "Теперь я - единственный наследник этого... человека. После смерти матери меня в этом захолустном городишке ничего не держит."
    a "Кроме плохих воспоминаний."
    a "Надо скорее продать этот мрачный особняк и уехать. Думаю, этих денег должно хватить, чтобы начать новую жизнь. Всегда хотел погрузиться в египтологию."

# Звук звонка
    $ renpy.music.set_volume(1.0, delay=0, channel='bgloop')
    play bgloop "audio/call.ogg"
    ""
    stop bgloop fadeout 1.0
    a "Алло."
    i "Артур, я звоню выразить свои соболезно..."
    a "Вы звоните не за этим."
    i "Да, тебя не проведешь."
    i "В общем, слушай, за год до своей кончины твой дед Николас сделал заявление в прессе. Мол, теперь-то у него точно будет шедевр."
    i "Мы в нашем бизнесе таким хвастливым обещаниям верить не привыкли - особенно от тех, кто не оправдывает доверие. Но и упускать возможную прибыль мы себе позволить не можем."
    i "Год - хороший срок, чтобы довести книгу до ума."
    i "Да и знаешь ли, книги авторов из свежих могил продаются лучше всего."
    i "В общем, найдешь рукопись старика - получишь отличный гонорар. Если что, я на связи."
    a "Это меняет дело. Так денег хватит даже на целую экспедицию..."

# Каминная светлая
    show screen daytime
    scene kamin
    $ dt = "пыль"

    a "Тут... довольно мило, и довольно пыльно. Надо осмотреться."

# scene Фото на камине

    a "Он... хранил нашу фотографию? Но зачем? Любовался теми, кого бросил?"
    a "Похоже, сплетни не врали. Старый развратник. На вид она ничего так... Не ради ли тебя наш дед забыл о нашей семье? Хотя... если он так легко выкинул нас из сердца, то проблема тут явно не в ней... "
    # a " Дед... служил? Никогда не слышал об этом. Наверно, просто бутафория."
    a "А там - недопитые бутылки. Значит, и это правда. Вот и истина в вине... Жалкий оказался человек..."

    scene royal

    a "Хм... толстый слой пыли на клавишах. Никто не играл на нем уже много лет. Очередной бессмысленный предмет."
    play sound "audio/thunder.ogg"
    scene royal

# Удар грома

    with flash
    $ dt = "ночь"
# Темная каминная

    ""
    a "Черт, только этого не хватало. Теперь еще щитки искать..."
    stop sound fadeout 1.0
# Темный камин
    $ renpy.music.set_volume(.7, delay=0, channel='bgloop')
    play bgloop "audio/creak_steps_slow.ogg"
    $ renpy.music.set_volume(.3, delay=0, channel='bgsfx1')
    play bgsfx1 "audio/breath.ogg" loop
    scene koridor
# Дыхание ГГ и скрип половиц

    a "Где же они? Черт!"


# Шепот
    $ renpy.music.set_volume(.4, delay=0, channel='bgsfx2')
    play bgsfx2 "audio/whispering.ogg" loop
    a "Что это такое... Здесь никого не должно быть!"
    stop bgsfx1 fadeout 1.0

    a "Эй, кто здесь?"

    stop bgloop fadeout 1.0
# Усиление шепота
    stop music
    play music "audio/sound_piano.ogg"
    play audio "audio/rain.ogg"
    $ renpy.music.set_volume(.7, delay=0, channel='bgsfx2')

# Кабинет со свечей

    scene kabinet no light with fade:
        alpha 1.0
        time 1.5
        linear 3.0 alpha 1.0

    a "Это напрягает."
    scene kabinet light
    hide screen daytime
    a "Кто, черт возьми, зажег эту свечу?{w} Сюда что, кто-то вломился? Надо звонить копам."
    a "Черт, мобильная связь тоже накрылась. Что за жесть тут происходит? Лучше поскорей убраться отсюда. Возьму свечу, а то с лестницы можно и навернуться ненароком."

# Тихий смех и еще более громкий шепот

    $ renpy.music.set_volume(1.0, delay=0, channel='bgsfx2')
    play audio "audio/laugh.ogg"
    scene koridor

    a "Кажется, в каминном зале на первом этаже кто-то есть. Выйти из дома можно только там. Черт, почему в этом доме нет черного хода?"
    a "Придется выяснить, кто там бродит. Надеюсь, он один и не вооружен."
    stop bgsfx2 fadeout 1.0
# без огня

    scene kamin
    show leo ghost at right

    n "Как же она красива..."
    a "Эй! Ты кто такой? Как ты сюда забрался вообще? А ну..."
    n "Ты когда-нибудь любил?"
    a "Слушай, мне сейчас не до романтики. Сюда уже едет полиция. Медленно подними руки. Это ты вырубил свет?"
    n "Нет, это Грегори. А я - Лайонель, к слову."
    a "Какой к черту Грегори? Где он?"
    leo @ ghost vspom "Стоит прямо за тобой."

# Дверь с расстворяющимся призраком

    scene dver
    with wiperight

    show greg normal at center:
        alpha 0.45


    a "Твою..."
    hide greg normal with dissolve

    scene kamin with wipeleft

    a "Что это было?! Что? Он... он не мог просто исчезнуть! Я отвернулся лишь на секунду. Что за?.. Черт, надо убираться отсюда."

# Дверь. Слышим звуки судорожно поворачиваемой ручки
    play sound "audio/door_knob_rattling.ogg" loop
    scene dver:
        alpha 1.0
        time 2.0
        linear 3.0 alpha 1.0

    a "Черт, она заперта! Как? Как это возможно?"
    stop sound fadeout 1.0

# Слышатся звуки ударов героя по двери.
    play bgsfx3 "audio/breaking_door.ogg"
    a "Крепкая, выбить почти нереально. Так, надо успокоиться. Паника убивает быстрее всего."
    stop bgsfx3 fadeout 1.0

# Мы слышим звуки частого дыхания героя.
    play bgsfx1 "audio/breath.ogg" loop
    a "В детстве кто-то учил...{w} кажется на фехтовании...{w} короткий вдох, продолжительный выдох."
    stop bgsfx1 fadeout 2.0
    a "Надо осмотреть комнаты, может удастся найти ключ."

    menu:
        "Надо внимательнее исследовать кабинет":
            $ sc10one = True
            scene kabinet
            show will ghost ob at left
            a "Ты... ты кто вообще такой? Что ты тут забыл?"
            n "Тише, тише, молодой человек, не надо так орать, будто вы до мертвых добудиться хотите.{w} Позвольте представиться: Уильям, мастер слова и пера."
            Will "Кстати, как вам этот отрывок:" 
            Will "«Ход его рассуждений прервался, и он увидел бесконечную тьму ее разума, лишенного всяческого сострадания. Она была безжалостным хищником, мифической сиреной, одержимой неутолимой жаждой губить души...»"
            a "Вы знакомый моего деда Николаса?"
            show will ghost at left
            Will "Конечно, я знал его всю свою жизнь."
            Will "Ах, бедный, бедный Николас. Какое счастье, что он покинул свою скорбную юдоль позора..."
            a "Тогда, может, поможете мне выйти отсюда?"
            Will "Выйти? Так спешите в суету мира, молодой человек? А могли бы испить из источника подлинного творчества."
            Will "Как прискорбно, еще один обыватель, хоть и внук Николаса."
            a "Откуда вы это знаете?"
            Will "Ключ вон там, на стене, видите? Не смею задерживать."
            scene kabinet:
                yalign 0.5 subpixel True
                zoom 2.3
            a "Но... там нет никакого ключа!"
        "Будет лучше пойти еще дальше по коридору второго этажа":
            $ sc10two = True
            scene orujka
            show greg ghost
            a "Ты еще кто такой?"
            g "Я - Грегори, а ты - мерзкий вор!"
            g "Думал, раз людишки вроде тебя свели Николаса в могилу, то ты можешь спокойно шнырять по его дому?!"
            g "Позарился на чужое?!"
            g ghost smile "Убирайся отсюда!"
 
            scene orujka
            with fade

    show screen daytime
    scene koridor:
        alpha 1.0
        time 2.0
        linear 3.0 alpha 1.0
    $ dt = "ночь"

# Мы слышим сильное сердцебиение за кадром.
    play bgsfx1 "audio/heartbeat.ogg" loop
# Темный экран
    ""
# Также, слышатся звуки (громкость постепенно увеличивается): то неразборчивый шепот, то скрежет затачиваемого металла, то тихий женский смех. 
    $ renpy.music.set_volume(.3, delay=0, channel='bgsfx2')
    $ renpy.music.set_volume(.4, delay=0, channel='bgloop')
    play bgsfx2 "audio/whispering.ogg" loop
    play bgloop "audio/sharpening.ogg"
    $ renpy.music.set_volume(.8, delay=5.0, channel='bgsfx2')
    $ renpy.music.set_volume(.9, delay=5.0, channel='bgloop')
    a "Я что, схожу с ума?! Этого не может быть... Это все нереально."
    play audio "audio/female_laugh.ogg"
    a "Боже, как же мне холодно... какой-то озноб...{w} надо сначала... срочно найти что... чем согреться."
    stop bgsfx2 fadeout 1.0
    stop bgloop fadeout 1.0
    stop bgsfx1 fadeout 1.0

# разожженный камин.

    scene kamin fire
    hide screen daytime

# Тяжелое дыхание
    play bgsfx1 "audio/breath.ogg" loop
    a "Хорошо, вроде получше... не так холодно."
    a "Все не могу понять:{w} я брежу? Я сплю?{w} Или с этим местом что-то не так?"
    a "Они же выглядят неживыми...{w} гниющими?"
    a "Они прокляты? Я проклят? Черт..."
    stop bgsfx1 fadeout 1.0
    a "В камине, среди углей, были какие-то обгоревшие бумаги."

# Письмо

    scene bumaga with noisedissolve
    
    menu:
        "... подтверждает расщепление личности на фоне тяжелого депрессивного расстройства. Вероятно, генезисом или триггером данного феномена послужила травля новых книг пациента в прессе, кроме того, на нескольких сеансах пациент упоминал смерть некоего близкого человека, которая, по его мнению, произошла по его вине. Временами говорит прямо «я убил», иногда «мы убили», иногда «он убил» - что это? Навязчивые диссоциативные галлюцинации? Пациент, однако, отказывается углубляться в подробности.":
            a "Любопытно. Значит, дед был серьезно болен... Это, конечно, его не оправдывает, но..."
    menu:
        "Очевидно, что субличности пациента играют роль гипертрофированных защитных барьеров психики. Так, Уильям - это, несомненно, идеальный образ себя как автора, способного творить выдающиеся произведения искусства. Грегори защищает хрупкое эго автора от нападок критики и, в целом, внешней среды. Но какую функцию играет редко появляющийся Лайонель? Пока неясно. Надеюсь, увеличение дозы антидепрессантов поможет избежать повторения попыток суицида и параноидальных приступов маломотивированной агрессии...":
            a "И что, эти его субличности смогли как-то воплотиться после смерти? Жуть какая."

    scene kamin fire

    a "Похоже, и вправду попал в дом с привидениями. Или в готический роман. Эдгар, ты балуешься?"
    a "Ха. А дед и из могилы смог доставить хлопот. Но, похоже, сошел с ума все-таки не я."
    a "Ну, видимо, все по классике: разгадай загадку дома, чтобы выйти.{w} Надеюсь, бледная хрупкая красотка по канону жанра тоже будет."
    a "Пойду в кабинет, может найду записи.{w} Надо взять свечу."

    scene kabinet

# Слышен звук скрипящего пера.
    play bgsfx1 "audio/pencil.ogg" loop



    if sc10one:
        show will ghost o4ki at left
        Will "О, вы вовремя! Сейчас, послушайте монолог моего героя о тщетности бытия! Только что написал."
        stop bgsfx1 fadeout 1.0
        $ q = []
        while len(q) < 2:
            menu:
                "Ты знаешь Грегори или Лайонеля?" if not 1 in q:
                    $ q.append(1)
                    $ renpy.block_rollback()
                    Will ghost "Это кто? Имена будто у персонажей каких-то второсортных новелл."
                "Ты знаешь что-то про девушку с портрета внизу на каминной полке?" if not 2 in q:
                    $ q.append(2)
                    $ renpy.block_rollback()
                    Will ghost "Молодой человек, мой ум постоянно вовлечен в сложную интеллектуальную деятельность."
                    Will ghost "Мне некогда рассматривать каких-то девиц. Даже на портретах."      
    else:
        show will ghost o4ki at left
        n "О, вы вовремя! Сейчас, послушайте монолог моего героя о тщетности бытия! Только что написал."
        stop bgsfx1 fadeout 1.0
        menu:
            "Ты кто?":
                n "Мне кажется, любой обладатель мало-мальски среднего интеллекта уже бы сообразил, что я писатель."
                n "Зовут меня Уильям."
                Will "Близкий друг Николаса, некогда - хозяина этого прекрасного кабинета.{w} К вашим услугам."
        $ q = []
        while len(q) < 2:
            menu:
                "Ты знаешь Грегори или Лайонеля?" if not 1 in q:
                    $ q.append(1)
                    $ renpy.block_rollback()
                    Will ghost ob "Это кто? Имена будто у персонажей каких-то второсортных новелл."
                "Ты знаешь что-то про девушку с портрета внизу на каминной полке?" if not 2 in q:
                    $ q.append(2)
                    $ renpy.block_rollback()
                    Will ghost ob "Молодой человек, мой ум постоянно вовлечен в сложную интеллектуальную деятельность."
                    Will ghost evil "Мне некогда рассматривать каких-то девиц. Даже на портретах."

    scene kabinet
    show will ghost ob at left
    $ q = []
    while len(q) < 2:
        menu:
            "Ты не в курсе, Николас никого не убивал?" if not 1 in q:
                $ q.append(1)
                $ renpy.block_rollback()
                Will @ ghost o4ki "Молодой человек! Николас хоть и был посредственным писателем, но человеком был весьма приличным."
                Will @ ghost o4ki "Как вы вообще могли такое о нем подумать?"
            "Тебе заняться больше нечем, как сидеть тут и заниматься «интеллектуальной деятельностью» в темноте?" if not 2 in q:
                $ q.append(2)
                $ renpy.block_rollback()
                Will "Молодой человек, не разочаровывайте меня окончательно."
                Will "Писательский труд суть чистое творение разумом вселенной."
                Will "Вы чувствуете метафизическое очарование подобного определения?"
                Will ghost o4ki "Кто знает, быть может и мы - всего лишь персонажи чьей-то пьесы или прозы и говорим лишь то, что кто-то неведомый вложил нам в уста."
                menu:
                    "Хочешь, расскажу тебе то, что ты не осознаешь?":
                        jump two3
            "Вы не знаете, Николас дописал перед смертью ту книгу, про которую делал объявление в прессе?":
                Will "Да, Николас успел закончить свой скорбный и не самый изысканный труд."
                menu:
                    "Я - внук Николаса и его прямой наследник. Эта книга теперь принадлежит мне. Прошу отдать ее.":
                        jump two1
                    "Почему вы все время оскорбляете моего деда? Он тоже был великим писателем. И вы еще называете себя его другом?":
                        $ sc15two = True
                        jump two2

 

    return

label two1:

    scene kabinet
    show will ghost o4ki at left

    Will "Однако, вы умудрились истощить мое долгое терпение и окончательно меня разочаровать."
    Will ghost evil "Вы могли бы прочесть здесь произведения истинного гения, но предпочли писанину вашего деда."
    Will "Что ж, прах к праху. Признаюсь, когда я прочитал последний труд вашего деда, я ужаснулся.{w} Из всех книг, что он написал - это худшая, без сомнения."
    Will "Ради его репутации, я ее немножко подправил, точнее, основательно переписал."
    Will "Я отдам ее вам, но исключительно для того, чтобы вы оставили меня в покое."
    Will @ ghost ob "Берите и идите, прошу вас! Продайте ее и живите сытой жизнью за счет плодов чужого ума, как и полагается людям вашего сорта."
    Will @ ghost ob "Прощайте."

    hide will ghost o4ki with dissolve

# Герой листает книгу (мы слышим шорох страниц).
    play bgsfx1 "audio/pages.ogg" loop
# Страница
    menu:
        "Получена книга вашего деда":
            scene kniga
            a "Тут... одно и то же..."

    stop bgsfx1 fadeout 1.0

    scene kabinet

    a "По нему я точно не буду скучать. Он действовал мне на нервы."
    a "Теперь надо разобраться с другими осколками непутевого деда."

    jump three

    return

label two2:

    scene kabinet
    show will ghost ob at left

    Will "Я понимаю, сложно смотреть объективно из-за уз родства,{w} но прошу вас, не стоит быть таким наивным."
    a "Дед написал минимум один бестселлер, общепризнанно вошедший в классику литературы."
    Will "Там вот какая прелюбопытнейшая история."
    Will "Видите ли, у Николаса был дед, предыдущий хозяин этого дома."
    Will "Говорили, он был буйнопомешанным и даже зарезал какую-то девчонку.{w} А еще он был писателем-неудачником."
    Will "Однако, в конце жизни он все же смог написать нечто шедевральное.{w} Но издать не успел."
    Will "И Николас, тогда еще молодой, получил его книгу в наследство."
    Will "Близким друзьям он говорил, что книгу ему вручил призрак...{w} Чушь для впечатлительных дам и легковерных глупцов!"
    Will "Недолго думая, ваш дед присвоил себе авторство, став в момент известным и богатым."
    Will ghost o4ki "Вот только сам он уже не смог создать что-либо стоящее."
    Will "Я, конечно, многому пытался его научить, но, увы, его потолок - бульварные детективчики."
    a "Интересная история. Скажите, а что издали вы?"
    Will "Помилуйте, как некультурно спрашивать такое..."
    a "И все же, я настаиваю."
    Will @ ghost evil "Подите прочь..."
    a "Вы ничего никогда не издавали и не писали."
    a "Ведь вы - всего лишь маска.{w} Вы - иллюзия гениальности."
    a "Вас создал мой дед и создал весьма занудным.{w} Ваша роль - быть барьером от страшной для него правды. Той правды, что он никогда не был достоин этого статуса и славы."
    a "Он умер, а вы так и остались его марионеткой.{w} Как вам такой поворот сюжета?"
    Will ghost "Вы... вы... правы."
    Will "Да, теперь я вижу всю картину целиком."
    Will "Прискорбно признавать, но похоже, я - лишь красивая обложка, за которой тщетная пустота."
    Will "Это так больно.{w} Но в то же время...{w} Я чувствую, что наконец-то свободен."
    Will "Парадоксально, но я благодарен вам.{w} Без вас, кто знает, сколько бы я еще был прикован к этому месту."
    Will "Прощайте."

    hide will ghost with dissolve

    a "По нему я точно не буду скучать. Он действовал мне на нервы."
    a "Теперь надо разобраться с другими осколками непутевого деда."

    jump three

    return

label two3:

    scene kabinet
    show will ghost o4ki at left

    Will "Дешевая интрига, молодой человек.{w} Дешевая интрига и неподобающий тон."
    Will "Ну что же, попробуйте, поразите меня."
    a "Ты - просто призрак моего выжившего из ума деда Николаса."
    Will ghost evil "Это возмутительно!{w} Как вы смеете! Вы перешли все границы!"
    Will "Убирайтесь отсюда, я больше не собираюсь лицезреть вашу отвратительную физиономию."

    hide will ghost evil with dissolve

    a "По нему я точно не буду скучать.{w} Он действовал мне на нервы."
    a "Теперь надо разобраться с другими осколками непутевого деда."

    jump three

    return

label three:

    scene orujka
    show greg ghost smile

    if sc10two:
        n "Такая изысканная шпага так долго лежала без дела.{w} Это неправильно."
        n "Оружие должно отнимать жизни.{w} А этой шпагой я уже давно никого не убивал."
        n "Но, вижу, сегодня настал ее час.{w} Страшно?{w} Страшно, я же вижу."
        a "Ты кто?"
        n "Я? Меня зовут Грегори, неприятно познакомиться."
        g ghost evil smile "Я - уничтожитель всего, что смело когда-либо причинять боль несчастному Николасу."
        g "Теперь я охраняю его наследство.{w} А еще я твой будущий убийца."
    else:
        g "Такая изысканная шпага так долго лежала без дела. Это неправильно."
        g "Оружие должно отнимать жизни. А этой шпагой я уже давно никого не убивал."
        g "Но, вижу, сегодня настал ее час. Страшно? Страшно, я же вижу."
        g ghost enemy "Ну давай, закрой глазки ручками, это поможет..."

    menu:
        "Ублюдок, ты не смеешь так со мной разговаривать! А ну пошел прочь!":
            g ghost enemy "Сейчас ты заплатишь за эти слова! Защищайся!"
            transform alpha_dissolve:
                alpha 0.0
                linear 0.5 alpha 1.0
                on hide:
                    linear 0.5 alpha 0
            screen countdown:
                timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
                bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
            $ time = 0.7
            $ timer_range = 0.7
            $ timer_jump = 'deadone'
            show screen countdown
            menu:
                "Уклониться":
                    hide screen countdown
                    $ sc17one = True
                    jump for
        "Эта шпага кого-то уже отнимала чью-то жизнь?":
            g ghost enemy "Да, какая-то тварь не отсюда. Пыталась предать Николаса, плела тут вокруг свои сети коварства."
            g "Я даже не потрудился запомнить, как ее звали."
            g "Думаю, тебя я тоже не запомню..."
            a "Ты убил... женщину?"
            g "Если ты еще хотя бы слово о ней скажешь, я отправлю тебя прямо к ней.{w} Там ты вдоволь насытишь свое любопыство..."
            menu:
                "Я - внук Николаса и его законный наследник. Я пришел за своим.":
                    $ sc17two = True
                    g ghost smile "Надо же. Внук, наследник..."
                    g "Где же ты был, внук, когда твоему деду было так плохо?{w} Когда все ополчились против него?{w} Отчего не навестил?"
                    g "Зато стоило миленькому дорогому особнячку освободиться, и наш герой уже здесь."
                    g ghost evil smile "Что ж, прошу вас, наследник, возьмите то, что вам причитается. Удачного владения!"
                    menu:
                        "Получены документы на дом":
                            scene doc
                            a "Да он просто издевается!"
                    # Документ в дырках
                "И что, хорошо ли ты защитил моего деда, раз он страдал до самой смерти?":
                    $ three = True
                    g ghost evil smile "Что ты знаешь вообще?"
                    a "Знаю то, что ты - лишь инструмент. Как эта шпага."
                    a "Дед пользовался тобой, чтобы и дальше себя жалеть."
                    show greg ghost
                    a "За твоей агрессией так удобно было прятать слабость."
                    a "Из-за тебя его бросили все, ты всех распугал, и дед много лет выл от одиночества."
                    a "Так кого ты защитил, Грегори?{w} И от того ли надо было защищать?"
                    a "Ты не справился."
                    a "Ты должен был научить деда защищаться самостоятельно."
                    g ghost smile "Ты... я ненавижу тебя, но ты, черт возьми, прав."
                    g "Спасибо.{w} Ты показал мне правду, и теперь я свободен."
                    g "Ты будешь хорошим наследником."
                    g "Надеюсь, ты найдешь книгу Николаса, и все войдет в привычную колею."
                    g "Для меня было честью встретить тебя,{w} хотя для нас обоих эта встреча и не была приятной."
                    g normal "Прощай."
                    hide greg normal with dissolve
    jump for

    return


label deadone:

    # Звуки пронзания
    play audio "audio/flesh_penetration.ogg"
    scene smert with blod:
        alpha 1.0
        time 1.5
        linear 3.0 alpha 1.0
    "Вы не успели уклониться. Похоже, шпага пронзила ваше сердце."
    jump end
    
    return

label for:

    if sc17one:
        scene koridor
        
        a "Он чуть меня не убил. Бешеный ублюдок!"
        a "Сам не ожидал, что смогу так ловко увернуться. Как будто в детстве меня учили вольтам. Может дед и учил? И этим спас меня от своей же агрессивной части?"
        a "Ладно, черт с этим Грегори, пойду в каминный зал, может третий будет адекватнее."
    else:
        scene orujka

        a "Ну, хотя бы не пырнули."
        a "Пора ставить точку в этой затянувшейся драме."
        a "Третий должен быть в каминном зале, я его видел именно там."
        a "Черт, призраки, привязанные к одному месту - какое клише!"

    scene kamin fire

    show leo ghost at right

    leo "Так странно.{w} Этот камин не разжигали уже очень давно."
    leo @ ghost vspom "Я все-таки узнал тебя.{w} Ты - внук Николаса, верно?"
    leo "Я... он испытывает к тебе сильную привязанность.{w} Ты должен уйти. "
    leo "Пойми же, Николас... мы не можем, не должны находиться рядом с теми, кто нам дорог. Поэтому я просил Николаса прекратить общение с тобой."
    leo "Мы разрушаем все, что любим. Мы... я - настоящее чудовище..."

    menu:
        "Перебить":
            a "Дед, мне надоели твои игры и не нужны твои оправдания."
            a "Ты оставил меня, забыв о моих чувствах, поэтому не требуй от меня заботы о твоих."
            a "Тебя никогда не интересовал кто-либо кроме себя самого.{w} Ты и сюда прибежал, чтобы жалеть себя."
            a "Ты сам во всем виноват и заслужил все, что с тобой произошло."
            leo "Ты прав. Абсолютно."
            show leo ghost die with move:
                xalign 0.2
            leo "Я эгоист. Я ничтожество. Я убийца. Я заслужил муки."
            show leo ghost fire with dissolve:
                xalign 0.1
            leo "Пора перестать прятаться и принять свою участь в адском пламени."
            # INT Дверь в особняк.
            scene dver with wiperight
            # Слышны звуки ударов в дверь.
            play bgsfx3 "audio/breaking_door.ogg"
            a "Нет! Чертов урод! Давай же, поддавайся."
            stop bgsfx3 fadeout 1.0
            play bgsfx3 "audio/coughing.ogg"
            scene smert with blod
            "Похоже, вы умерли от удушья даже раньше, чем от огня."
            jump end

        "Не вмешиваться":
            leo ghost vspom "Я не должен жить."
            leo "Я пытался... уйти... но эти двое так и не дали мне довести ту попытку до конца."
            leo "Мне пришлось жить и мучаться. Жить и каждый день ненавидеть себя."
            leo "Ты можешь себе представить, каково это?"
            a "Дед, я сейчас обращаюсь к тебе."
            a "Хватит. Больше незачем прикидываться кем-то другим."
            a "Прошу, прими уже ответственность за все."
            leo ghost "Ты не понимаешь..."
            leo "Я не могу. Слишком велика моя вина."
            leo "Мне нет прощения.{w} Я ведь убил мою Сару... сам убедись, как это было ужасно."
            # INT каминная много лет назад.
            hide leo ghost
            # Слышен женский смех.
            play audio "audio/female_laugh.ogg"
            scene kamin memory with memory
            show sara live:
                xalign 0.2
            
            show nic:
                xalign 0.6
            s "А ну, не смей поддаваться!"
            s "Ну же, защищайся достойно! Я хочу поразить тебя в честной борьбе."
            d "Ты уже поразила меня однажды, любовь моя, и теперь ты всегда здесь, в моем сердце."
            s "Ах, ты невыносимо галантен."
            s "Я так рада, что ты снова счастлив. Как дела с твоей новой книгой?{w} Верю, у тебя все получится!"
# Дед стоит лицом к камину, сжимает шпагу в руках.
            s "Почему ты молчишь? Что не так?"
            d "Ты издеваешься надо мной?{w} Как я могу написать хотя бы строчку чего-то стоящего, если я все время провожу с тобой?"
            s "Что ты такое говоришь? Я не требую твоего внимания постоянно!"
            s "Николас, ты что перестал принимать препараты? Тебе же помогала терапия!"
            d "Ты... ты такая же как они все. Ты хочешь сделать из меня послушную марионетку? Напичкать таблетками?"
            s "Николас, милый, нет! Это не ты... это не ты говоришь... сопротивляйся ему, прошу!"
            g "Ты... это ты портишь все мои замыслы!{w} Смеешься втайне надо мной!"
            g "Хочешь прибрать к рукам мой дом? Уже сговорилась со своими грязными дружками?"
            g "Лживая шлюха, я убью тебя!"
            scene royal with noisedissolve
            show leo ghost pe4al at left
            leo ghost pe4al "Теперь ты понимаешь? Она верила в меня. Она единственная поддерживала меня... До конца."
            leo "Я никогда не смогу простить себя."
            # Мы слышим звуки игры на рояле.
            stop music
            play music "audio/piano_loop.ogg"
            show sara ghost with dissolve:
                xalign 0.8
            s "Ты не виноват, и я тебя никогда не винила."
            s "Это был не ты, а твой недуг, выпестованный жестоким миром. Ты помнишь, как много боли тебе причинили?"
            leo "Сара... я был слишком слаб.{w} Я должен был справиться..."
            s "Милый, ты не мог этим управлять. Прими это."
            s "Ты был сильным и сделал все что мог. Именно такого сильного человека я и полюбила, такого я хочу сейчас."
            s "Пойдем со мной..."
            if sc15two and three:
                hide leo ghost pe4al with fade
                show nic ghost at left
                d "Я рад видеть тебя вновь. Ты... возмужал."
                d "Я горжусь тобой, Артур. Ты спас меня и сделал то, чего не смог я за всю свою жизнь."
                d "Я знаю, я никогда не смогу по достоинству отблагодарить тебя. Прости же меня за все."
                menu:
                    "Получены документы на дом и книга":
                        d "Вот, я отдаю эти документы. Теперь ты - хозяин этого дома. И я хочу отдать тебе свою последнюю книгу, посмертный труд."
                        d "Распорядись этим так, как сочтешь нужным. Ты доказал, что умеешь принимать мудрые решения."
                        show nic ghost with move:
                            xalign 0.4
                        d "Теперь, позволь мне уйти с любимой."
                show sara ghost with move:
                        xalign 0.5
                s "Как же долго я ждала этого пиршества. И вот оно наступило."
                s "Хотя из-за твоего несмышленого внука я так и не получила всего Николаса, но и ты сгодишься, сладкий."
            else:
                show sara ghost with move:
                    xalign 0.5
                leo ghost vspom "Благодарю тебя. Без тебя я никогда не решился бы."
                leo "Спасибо, что никто из тех двоих мне больше не мешает уйти."
                leo "Я так и не смог обрести целостность, но я и не заслужил."
                leo "Впервые я чувствую облегчение. Я не знаю, сможешь ли ты простить меня... нас."
                leo "Возьми это:"
                if sc17two:
                    menu:
                        "Получен ключ":
                            leo "Это место больше не держит тебя. Ты свободен. Как и я."
                else:
                    menu:
                        "Получены документы на дом":
                            leo "Прошу тебя, избавься от этого дома. Найди свой путь и свое место в мире."
                show sara ghost evil with move:
                    xalign 0.5
                s "Как же долго я ждала этого пиршества. И вот оно наступило."
                s "Хотя из-за твоего несмышленого внука я так и не получила всего Николаса, но и ты сгодишься, сладкий."

            # исчезновение
            # Конец. Титры.

    jump end

    return
    
    
label end:

    scene black with dissolve #или твоя сцена
    show text "Project manager:{p}{p}Анна Большекова vk.com/machaonorientis{p}{p}Leading scriptwriter:{p}{p}Святослав Жиленко{p}{p}Scriptwriters:{p}{p}Rimux vk.com/rimuxs{p}Наташа Титоренко{p}{p}Developers:{p}{p}Анна Большекова vk.com/machaonorientis{p}Giglemash github.com/Giglemash{p}{p}Sound designer:{p}{p}Vlad Ulrich github.com/Wedmer{p}{p}Artists:{p}{p}Надежда Татаренкова vk.com/id233584860{p}satifobia artstation.com/satifobia{p}Матвей Гробовой vk.com/theory_of_ninja{p}Дарья Волкова{p}{p}Translators:{p}{p}Святослав Жиленко{p}{p}Thanks for the help:{p}{p}Оксана Мельникова{p}Andrew «Prol» Ponomarev author.today/u/andrewponomarev{p}{p}{p}{p}{p}Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)" at cred_up
    $ renpy.pause(14, hard = True)
    
    return
