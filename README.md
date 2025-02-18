WeatherEmailScraper:

This project is a Python script that uses Selenium to collect weather forecast information from a website and then sends that information as an HTML email. It scrapes the page, gathers data such as the current temperature and forecast for the next few days, and uses Jinja2 to generate the email content. Finally, the email is sent through Gmail's SMTP server.

Features:

• Data Retrieval: Uses Selenium to access the tempo.com website, input the city, and extract current temperature, weather condition, and the forecast for the next 3 days.
• Email Sending: Formats the obtained data into an HTML email and sends it to a configured recipient.
• Scheduling: Uses the schedule library to schedule the daily execution of the script.

Requirements:

Python 3x
Necessary Python Libraries: selenium, webdriver_manager, schedule, smtplib, email, dotenv
Gmail email account for sending.
Setup:

• Install the necessary dependencies: pip install selenium webdriver_manager schedule
• Run the script to test email sending: python app.py

Notes: Ensure that the Chrome WebDriver is installed and configured correctly.
