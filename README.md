# Google-Form-Response-Automation
This repository contains code for automating responses to a Google Form using Selenium in Python 3 and ChromeDriver. The automation is designed to interact with a specific Google Form available at this link, which consists of 4 pages with text fields and radio buttons. The automation randomly selects choices for the radio buttons.

Prerequisites
 1. Python 3
 2. Chrome browser installed
 3. ChromeDriver compatible with your Chrome browser version. You can download ChromeDriver from here.

Install the required selenium packages:
  pip install selenium

Usage
  1. Ensure you have downloaded the appropriate ChromeDriver for your Chrome browser version and placed it in your PATH.
  2. Run the Python script autoFormer.py
        => python automate_google_form.py
     
The script will launch a Chrome browser, navigate to the specified Google Form, and automate the form submission process.
Once the form submission is complete, the browser will close automatically.

Note
This automation script is specifically designed for the provided Google Form structure. Any modifications to the form structure may require corresponding changes to the script.
Ensure you have a stable internet connection while running the script to avoid any disruptions during form submission.

License
This project is licensed under the MIT License. Feel free to modify and distribute the code for your own purposes.
