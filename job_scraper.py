import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Email config
EMAIL_SENDER = "ankithcart@gmail.com"
EMAIL_PASSWORD = "dgct fluy pjqp zwrw"
EMAIL_RECEIVER = "ankithgangaclassic@gmail.com"

def generate_naukri_urls():
    skills = {
        ".NET": "https://www.naukri.com/fresher-dot-net-jobs-in-bangalore",
        "Cloud": "https://www.naukri.com/fresher-cloud-fresher-jobs-in-bangalore",
        "JavaScript": "https://www.naukri.com/fresher-javascript-fresher-jobs-in-bangalore",
        "Java": "https://www.naukri.com/fresher-java-fresher-jobs-in-bangalore",
        "C#": "https://www.naukri.com/fresher-c-sharp-fresher-jobs-in-bangalore",
        "Node.js": "https://www.naukri.com/fresher-nodejs-fresher-jobs-in-bangalore",
    }

    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"🕒 Naukri Fresher Jobs – Bangalore – Generated at {today}\n"]

    for skill, url in skills.items():
        lines.append(f"🔹 {skill} Freshers:\n{url}\n")

    return "\n".join(lines)

def main():
    body = generate_naukri_urls()

    # Save to file
    filepath = "D:/JobScraper/job_updates.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(body)

    # Open in Notepad
    os.startfile(filepath)

    # Email it
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = "💼 Naukri Fresher Job Category Links - Bangalore"

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    main()
