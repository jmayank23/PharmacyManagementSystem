# PharmacyManagementSystem

This repository contains code for a project titled, "Pharmacy Management System", completed during undergraduate studies.

## Functionality
This project utilizes sqlite3 to maintain a database (student.db) that contains four tables:
1. student - Student ID, Name, Password
2. medicines - Medicine ID, Medicine Name, Quantity in stock, Price (in Rs.), Expiry Date
3. outofstock_meds - Medicine ID, Medicine Name, Date and Time out of stock
4. transactions - Transaction ID, Medicine ID, Student ID, Count, Date

## Description
When the program is run, the first page asks for the student to login. Next, a page is shown with a list of medicines, upon selecting a medicine from the list, the price is displayed. There is also an option to search for medicine names where the search phrase may or may not be an exact match. For example, to search for "Dollo 650", a user may just enter "Dol" and all results would be populated. Once a medicine is selected, user may click on add and that medicine will be shown in the Cart. Depending on the quantity of medicine in stock, the medicine list will be updated in real time. Upone clicking "Buy", a bill will be generated and details of the transaction stored in the transactions table. Also, at the end of the transaction, the medicines quanities left will be updated in the table. 

## Usage
### Step 1 - Run PharmacyMgtSystem.py
<img width="1351" alt="Screen Shot 2022-07-19 at 9 16 17 PM" src="https://user-images.githubusercontent.com/27727185/179793133-01826008-928f-4688-9b25-5e0b14a90e0b.png">

### Step 2 - Enter Login Credentials
SNU Net ID - mj740 
Password - mayank@123
CLick on 'Login'

### Step 3 - List of Medicines and Cart displayed
Select a medicine and click on 'Add'
<img width="1347" alt="Screen Shot 2022-07-19 at 9 18 47 PM" src="https://user-images.githubusercontent.com/27727185/179793941-42f86ec9-4cc1-4392-9d88-c001865e7fe1.png">

### Step 4 - Search functionality
<img width="1346" alt="Screen Shot 2022-07-19 at 9 19 06 PM" src="https://user-images.githubusercontent.com/27727185/179795006-d7249065-f254-4a5f-9164-d3fdd81db2ef.png">
