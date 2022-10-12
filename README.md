<h1 align="center">DTK Quiz filler</h1>
<p align="center"> Automatically fill qualtrics DTK quizes</p>

# ⚠️ Disclaimer ⚠️
This is just a fun hobby project, which only exists as a proof-of-work.
Always fill in the quizes appropriately.

# Requirements
* Python 3
* Firefox / Chrome

# Installation & usage
### 1. Clone repo
```bash
git clone https://github.com/Tasztalos69/dtk-quiz.git && cd dtk-quiz
```

### 2. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

If it throws an error `No module named pip`, make sure to install pip:
```bash
# Linux & macOS
python3 -m ensurepip --upgrade

# Windows
py -m ensurepip --upgrade
```

### 3. Run
```bash
# With Firefox
python3 ./main.py firefox <quiz_url>

# With Chrome
python3 ./main.py chrome <quiz_url>
```
This opens a browser, where you're greeted with the quiz. Fill in any personal data manually, and when on the page with the questions to be filled, **return to the terminal**, and press enter. The script should fill all fields until it reaches the end.

> Don't worry if it pauses between pages, it should continue automatically.

# About
This project emerged in a lunch break, and uses python and selenium. It's by far not complete, but it works.
