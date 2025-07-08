from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time

# Email configuration
EMAIL_SENDER = "ankithcart@gmail.com"
EMAIL_PASSWORD = "dgct fluy pjqp zwrw"
EMAIL_RECEIVER = "ankithgangaclassic@gmail.com"

# Job search queries (for masters freshers in Bangalore)
keywords = [
    "site:naukri.com software developer fresher masters Bangalore",
    "site:glassdoor.com full stack developer fresher masters Bangalore",
    "site:careers.google.com backend developer Bangalore fresher masters",
    "site:careers.microsoft.com cloud engineer Bangalore fresher masters",
    "site:jobs.linkedin.com software engineer Bangalore fresher masters",
]

def fetch_jobs():
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    job_results = [f"🕒 Jobs fetched at: {today}"]

    # Configure Edge for headless browsing
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--log-level=3")

    driver_path = "D:/JobScraper/msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(driver_path), options=edge_options)

    total_jobs = 0

    for query in keywords:
        driver.get("https://duckduckgo.com/")
        search = driver.find_element(By.NAME, "q")
        search.send_keys(query)
        search.send_keys(Keys.RETURN)

        time.sleep(2)
        results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")

        job_results.append(f"\n🔍 Results for: {query}")
        count = 0

        for link in results:
            title = link.text.strip()
            href = link.get_attribute("href")

            if href and href.startswith("http"):
                job_results.append(f"🔹 {title}\n{href}")
                count += 1
                total_jobs += 1

            if count >= 5:
                break

        if total_jobs >= 15:
            break

    driver.quit()

    job_text = "\n".join(job_results)

    # Save to local file
    with open("D:/JobScraper/job_updates.txt", "w", encoding="utf-8") as f:
        f.write(job_text)

    # Open in Notepad
    os.startfile("D:/JobScraper/job_updates.txt")

    # Send email
    send_email(job_text)

def send_email(body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = "💼 15+ Master's Fresher Jobs in Bangalore"

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    fetch_jobs()
