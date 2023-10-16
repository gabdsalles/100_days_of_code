print('''
                  ,--.    ,--.
                 ((O ))--((O ))
               ,'_`--'____`--'_`.
              _:  ____________  :_
             | | ||::::::::::|| | |
             | | ||::::::::::|| | |
             | | ||::::::::::|| | |
             |_| |/__________\| |_|
               |________________|
            __..-'            `-..__
         .-| : .----------------. : |-.
       ,\ || | |\______________/| | || /.
      /`.\:| | ||  __  __  __  || | |;/,'
     :`-._\;.| || '--''--''--' || |,:/_.-':
     |    :  | || .----------. || |  :    |
     |    |  | || '----SSt---' || |  |    |
     |    |  | ||   _   _   _  || |  |    |
     :,--.;  | ||  (_) (_) (_) || |  :,--.;
     (`-'|)  | ||______________|| |  (|`-')
      `--'   | |/______________\| |   `--'
             |____________________|
              `.________________,'
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
              |        ||        |
              '--------''--------'
''')
print("Bem-vindo ao Fuja do Robô.")
print("Sua missão é sobreviver ao ataque de um robô assassino.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Você está em uma nave espacial e descobre que um dos robôs que auxiliam na manutenção da nave se rebelou")

choice = input('Você está em um grande corredor com duas portas. Qual você escolhe? Digite "esquerda" ou "direita".\n').lower()

if (choice == "esquerda"):
    print("Você entrou na sala de controle e está a salvo, mas não por muito tempo. O robô está chegando.")
    choice = input ('O que você escolhe: se esconder em um armário de limpeza ou fugir pelo túnel de lixo? Digite "armario" ou "tunel", sem acentos.\n').lower()

    if (choice == "armario"):
        print("O robô tem visão infravermelha. Ele te achou no armário e você morreu. Game Over")
    elif (choice == "tunel"):
        print("Você continua um passo à frente do robô e chegou na sala de armas da nave.\nUma das três armas a seguir vai te ajudar a eliminar o robô facilmente")
        choice = input('As opções são: machado do Minecraft, pulso eletromagnético ou uma bazuca. Escolha sabiamente: digite "machado", "pulso" ou "bazuca".\n').lower()

        if (choice == "machado"):
            print("O robô destruiu seu machado rapidamente e você morreu. Game Over")
        elif (choice == "pulso"):
            print("Você se esconde do robô e ativa o pulso eletromagnético nele. O robô morre.")
            print("Você sobreviveu!! Parabéns :)")
            print('''                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-. ''')
        elif(choice == "bazuca"):
            print("Parabéns, você explodiu o robô! Mas você também se explodiu né kkkkkkkk, Game Over")

elif (choice == "direita"):
    print("Essa porta dá direto para o frio congelante do espaço. Game Over")
