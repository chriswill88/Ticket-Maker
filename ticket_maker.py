#!/usr/bin/env python3
# Made by Christian Williams: Chats Warrior!
# this project is used to make a collection of tickets for the days I work.
# use datetime import to create custom file that will contain tickets for that day.
from datetime import datetime
import os
from os import path
from os import system
import json

if not path.exists('./logs'):
    os.makedirs('./logs')
    
filename = './logs/' + datetime.today().strftime("%d-%m-%Y") + 'log.txt'

"""
This function allow us to view the saved tickets!
@filename: the filename
"""
def ticket_viewer(filename):
    system('clear')
    if not path.exists(filename):
        print("You have no saved tickets!\nMake a ticket Noob!")
        return()

    with open(filename, 'r') as f:
        for i in f:
            a = json.loads(i)
            for n, v in a.items():
                print("{} - {}".format(n, v))
            print()
system('clear')

if input("Welcome to Ticket Maker V1! Press enter to Create a ticket.\nTo view your tickets for the day type v and press enter: ") == 'v':
    ticket_viewer(filename)
else:
    while (1):
        system('clear')
        ticket = {}

        issues = {
            1: 'Driver Reimbursment', 2: 'Bug report', 3: 'Driver Block',
            4: 'Order', 5: 'Billing', 6: 'Store', 7: 'Other'}

        [print("{}: {}".format(x, i)) for i, x in issues.items()]
        print()

        issue = i_n = int(input("Enter number for issue: "))
        issue = input("Enter other issue: ") if issue == 7 else issues[issue]
        print("\nselected issue: {}\n".format(issue))

        driver = input("Enter Driver's name: ")
        account_id = input("Enter Accout_id: ")
        order_id = input("Enter Order_id: ")

        subject_title = input("What would you like to name the subject: ")
        situation_description = input("Enter the situation Description: ")
        proposed_solution = input("Enter your solution: ")

        subject = 'order_id {} - {}'.format(order_id, subject_title)

        if i_n == 2:
            subject = subject_title
        elif i_n == 3:
            subject = '{} - account_id {} - {}'.format(driver, account_id, subject_title)

        ticket = {
            "subject": subject,
            "Type of issue": issue,
            "driver": driver,
            "account_id": account_id,
            "order_id": order_id,
            "description": situation_description,
            "proposed_solution": proposed_solution,
        }

        if i_n == 6:
            sales_associate = input("Enter sales associates name: ")
            store = input("What store was it? ")
            store_code = input("Enter the store code: ")
            ticket["sales assosiate"] = sales_associate
            ticket['store'] = store
            ticket['store code'] = store_code

        other_info = None
        while (1):
            print("Press Enter to continue.")
            other_info = input("What other info would you like to store: ")
            if len(other_info) <= 1:
                break
            info = input("Enter value for {}: ".format(other_info))
            ticket[other_info] = info
            other_info = info = None

        with open(filename, 'a+') as f:
            json.dump(ticket, f)
            f.write('\n')

        done = input("Press Enter to continue, or type in any thing and press Enter to stop: ")
        if done:
            ticket_viewer(filename)
            break
