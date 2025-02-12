# Restaurant-Management-System
Python-based restaurant management system designed to streamline food ordering and billing processes.

## Project Overview
The New Age Indian Cafe project is a Python-based restaurant management system
designed to streamline food ordering and billing processes. It allows customers to view
a digital menu, place orders, and receive a detailed bill upon checkout. This project is
well-suited for smaller cafes or restaurants seeking a simple, text-based solution to
manage orders efficiently.

## Project Objectives
● Display an organized menu for customers.<br>
● Handle food ordering in a user-friendly, interactive way.<br>
● Automatically calculate the total bill based on ordered items and generate a
receipt.

## Data Collection
The (new_age_indian_cafe_menu.csv) is a random CSV file generated using the
new age technology of the large language model.
In this two varieties of LLMs were used to create the data,<br>
● ChatGPT<br>
● ClaudeAI

## Key Features and Functionalities
● Menu Display: The view_menu() function reads a CSV file
(new_age_indian_cafe_menu.csv) and displays the menu in a formatted
table using the tabulate library.<br>
● Order Processing: The order() function enables customers to add items to
their order by entering item names. It includes input validation to manage
incorrect entries and allows modifications to the order.<br>
● Billing System: Upon completing the order, the system calculates the total cost,
includes service tax and generates a final bill. It also displays itemized details for
clarity.

## Technical Specifications
### Libraries Used:
○ pandas: Handles data from the CSV menu file.<br>
○ tabulate: Formats menu and billing outputs into readable tables.<br>
○ warnings: Suppresses terminal warnings to maintain a clean user
experience.
### Data Structure:
○ MENU: A global variable storing the restaurant's menu data.<br>
○ ORDER: A global list storing items selected by the customer.
