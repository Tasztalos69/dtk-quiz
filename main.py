#!/usr/bin/env python3
import random
import sys
import signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from termcolor import colored
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def quiz():
    try:
        url = sys.argv[1]
    except:
        print(colored("Please provide the quiz URL.", "red"))
        sys.exit(1)
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
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
        print(colored("Canceled.", "red"))
        sys.exit(0)


if __name__ == '__main__':
    main()

