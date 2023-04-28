import csv
import requests

# Set your Mailgun API key and domain
API_KEY = 'your_api_key'
MAILGUN_DOMAIN = 'your_mailgun_domain'

# Set the Mailgun API endpoint for sending messages
MAILGUN_ENDPOINT = 'https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN)

# Define the message subjects and bodies for each category
category1_subject = 'Category 1 email subject'
category1_body = 'Category 1 email body'
category2_subject = 'Category 2 email subject'
category2_body = 'Category 2 email body'

# Read customer data from CSV file
with open('customers.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Categorize customers based on email domain
        if row['email'].endswith('category1.com'):
            subject = category1_subject
            body = category1_body
        else:
            subject = category2_subject
            body = category2_body

        # Set the Mailgun message parameters
        message_params = {
            'from': 'sender@example.com',
            'to': row['email'],
            'subject': subject,
            'text': body
        }

        # Send the message using the Mailgun API
        response = requests.post(
            MAILGUN_ENDPOINT,
            auth=('api', API_KEY),
            data=message_params
        )

        # Print the Mailgun API response status code and message
        print('Mailgun API response for {}:'.format(row['email']), response.status_code, response.text)
