<h1 align="center">DTK Quiz filler</h1>
<p align="center"> Automatically fill qualtrics DTK quizes</p>

# ⚠️ Disclaimer ⚠️
This is just a fun hobby project, which only exists as a proof-of-work.
Always fill in the quizes appropriately.

# Requirements
* Python 3
* Firefox

# Installation & usage
### 1. Clone repo
```bash
git clone https://github.com/Tasztalos69/dtk-quiz.git
```

### 2. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 3. Run
```bash
python3 ./main.py <quiz url>
```
This opens a browser, where you're greeted with the quiz. Fill in any personal data manually, and when on the page with the questions to be filled, **return to the terminal**, and press any key. The script should fill all fields until it reaches the end.

# About
This project emerged in a lunch break, and uses python and selenium. It's by far not complete, but it works.
