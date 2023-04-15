#!/usr/bin/env python3
import random
import sys
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def quiz():
    try:
        parser = sys.argv[1]
        if parser != "chrome" and parser != "firefox":
            raise NameError
    except:
        print(colored("Please provide a parser (chrome / firefox).", "red"))
        sys.exit(1)
    try:
        url = sys.argv[2]
    except:
        print(colored("Please provide the quiz URL.", "red"))
        sys.exit(1)
    if parser == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.get(url)

    # Wait for user data fill-in
    input(colored("Fill in your data, then press enter.", "blue"))

    while True:
        # Table processing
        rows = driver.find_elements(By.CLASS_NAME, "ChoiceRow")
        max_options = len(rows[0].find_elements(By.TAG_NAME, "td"))
        for r in rows:
            rnd = random.randint(4, 4 + max_options - 1)
            r.find_element(By.CLASS_NAME, f"c{rnd}").click()

        driver.find_element(By.ID, "NextButton").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "QuestionBody")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "LoadingPage")))

        try:
            driver.find_element(By.ID, "EndOfSurvey")
            print(colored("Successfully filled quiz!", "green"))
            driver.quit()
            sys.exit()
        except:
            pass


def main():
    try:
        quiz()
    except KeyboardInterrupt:
        print(colored("\nCanceled.", "red"))
        sys.exit(0)


if __name__ == '__main__':
    main()

