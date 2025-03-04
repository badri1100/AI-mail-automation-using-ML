import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to send messages using Selenium
def send_whatsapp_message(phone_number, message):
    # Initialize Chrome WebDriver (Make sure you have Chrome installed and chromedriver in your PATH)
    driver = webdriver.Chrome()
    
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    
    # Wait for 20 seconds to give time for the user to log in
    time.sleep(20)

    # Locate the search box and enter the recipient's phone number
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(phone_number)
    time.sleep(2)

    # Select the first search result (assuming it's the correct contact)
    first_result = driver.find_element_by_xpath('//span[@title="{}"]'.format(phone_number))
    first_result.click()
    time.sleep(2)

    # Locate the message input box and send the message
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(message)
    time.sleep(1)
    message_box.send_keys(Keys.ENTER)

    # Close the browser window
    driver.quit()

# Read phone numbers from CSV file and send messages
def send_bulk_whatsapp_messages(csv_file, message):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present
        for row in reader:
            phone_number = row[0]
            send_whatsapp_message(phone_number, message)
            time.sleep(2)  # Add a small delay between sending messages

# Example usage
csv_file = 'contacts.csv'  # Path to your CSV file containing phone numbers
message = "Hello! This is a test message sent using Python and Selenium."

send_bulk_whatsapp_messages(csv_file, message)
