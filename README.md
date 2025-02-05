Caso esteja usando outro sistema operativo procure como instalar o python e a sua biblioteca pygame

Linx:

Instalando o pip no Linux
$ sudo python get-pip.py

NOTA: Se você usa o comando python3 para iniciar uma sessão de terminal, utilize
"sudo python3 get-pip.py" aqui.

Se usar Python 3, dois passos são necessários: instalar as bibliotecas das
quais o Pygame depende e fazer o download e a instalação do Pygame.


$ sudo apt-get install python3-dev mercurial
$ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev

Esses comandos instalarão as bibliotecas necessárias para executar a
Invasão Alienígena com sucesso. Se quiser habilitar algumas
funcionalidades mais sofisticadas do Pygame, por exemplo, a capacidade
de adicionar sons, acrescente também as bibliotecas a seguir:

$ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
$ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
$ sudo apt-get install python-numpy

Agora instale o Pygame executando o seguinte (utilize pip3 se for
apropriado ao seu sistema):

$ pip install --user hg+http://bitbucket.org/pygame/pygame
