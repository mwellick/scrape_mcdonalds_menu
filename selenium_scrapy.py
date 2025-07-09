import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

with open("menu.json", encoding="utf-8") as f:
    main_data = json.load(f)

dumps = []

for item in main_data:
    url = item["url"]
    driver.get(url)

    try:
        nutrients = driver.find_elements(By.CSS_SELECTOR, ".sr-only.sr-only-pd")
        button = driver.find_element(By.CLASS_NAME, "cmp-accordion__button")
        button.click()
        time.sleep(1)

        name = item["title"]
        description = driver.find_element(By.CLASS_NAME, "cmp-text").text

        data = {
            "name": name,
            "description": description
        }

        energy_value = driver.find_elements(By.CSS_SELECTOR, ".cmp-nutrition-summary__heading-primary-item")

        for block in energy_value:
            try:
                value = block.find_element(By.CSS_SELECTOR, ".value .sr-only").text.strip().lower()
                metric = block.find_element(By.CSS_SELECTOR, ".metric .sr-only").text.strip().lower()

                if "калор" in metric:
                    data["calories"] = value
                elif "жир" in metric:
                    data["fat"] = value
                elif "вуглевод" in metric:
                    data["carbs"] = value
                elif "білк" in metric:
                    data["protein"] = value

            except Exception as e:
                print(f"Error extracting block: {e}")

        extra_blocks = driver.find_elements(By.CSS_SELECTOR, ".label-item")

        for block in extra_blocks:
            try:
                label = block.find_element(By.CSS_SELECTOR, ".metric").text.strip().replace(":", "").lower()
                value = block.find_element(By.CSS_SELECTOR, ".sr-only").text.strip().lower()

                if "нжк" in label:
                    data["saturated_fat"] = value
                elif "цукор" in label:
                    data["sugar"] = value
                elif "сіль" in label:
                    data["salt"] = value
                elif "порц" in label:
                    data["portion"] = value

            except Exception as e:
                print(f"Error extracting block: {e}")

        dumps.append(data)

    except Exception as e:
        print(f"Unexpected error: {e} during parsing this url address: {url}")

driver.quit()

with open("nutrients_data.json", "w", encoding="utf-8") as f:
    json.dump(dumps, f, ensure_ascii=False, indent=4)
