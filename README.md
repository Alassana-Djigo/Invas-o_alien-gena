# Instalando Python e Pygame

Você precisa instalar o Python e a biblioteca Pygame no seu sistema operacional, siga as instruções abaixo:

---

## 🔹 Linux

### 1️⃣ Instalando o `pip` (gerenciador de pacotes do Python)
```bash
sudo python get-pip.py
```
**Nota:** Se você usa `python3` para iniciar uma sessão no terminal, utilize:
```bash
sudo python3 get-pip.py
```

### 2️⃣ Instalando dependências do Pygame
```bash
sudo apt-get install python3-dev mercurial
sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
```

Caso queira adicionar funcionalidades extras (exemplo: suporte a sons), instale também:
```bash
sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcodec-dev
sudo apt-get install python-numpy
```

### 3️⃣ Instalando o Pygame
Execute o seguinte comando (use `pip3` se necessário):
```bash
pip install --user hg+http://bitbucket.org/pygame/pygame
```

---

## 🔹 Windows

### 1️⃣ Baixando e Instalando o Python
1. Acesse: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe a versão mais recente do Python 3
3. Durante a instalação, **marque** a opção "Add Python to PATH"

### 2️⃣ Instalando o `pip` (caso não esteja instalado)
Abra o **Prompt de Comando (cmd)** e digite:
```cmd
python -m ensurepip --default-pip
```

### 3️⃣ Instalando o Pygame
Depois que o Python estiver instalado, execute:
```cmd
pip install pygame
```

