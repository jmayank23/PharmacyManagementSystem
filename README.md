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
SNU Net ID - mj740\
Password - mayank@123\
Click on 'Login'

### Step 3 - List of Medicines and Cart displayed
Select a medicine and click on 'Add'

<img width="1347" alt="Screen Shot 2022-07-19 at 9 18 47 PM" src="https://user-images.githubusercontent.com/27727185/179793941-42f86ec9-4cc1-4392-9d88-c001865e7fe1.png">

### Step 4 - Search functionality
<img width="1346" alt="Screen Shot 2022-07-19 at 9 19 06 PM" src="https://user-images.githubusercontent.com/27727185/179795006-d7249065-f254-4a5f-9164-d3fdd81db2ef.png">

### Step 5 - Medicine List updated based on quantity available
Dollo 650 available in stock is 5. Once 5 of them have been added, the medicine will no longer be displayed in the medicine list. 

<img width="1346" alt="Screen Shot 2022-07-19 at 9 19 48 PM" src="https://user-images.githubusercontent.com/27727185/179796655-6fed820a-4679-46e9-8a75-f286a14eb90a.png">

### Step 6 - Click on Buy to generate bill
<img width="1006" alt="Screen Shot 2022-07-19 at 9 33 43 PM" src="https://user-images.githubusercontent.com/27727185/179797288-0ffbb802-e58b-4ba3-b31c-4cc60301bf72.png">

### Status of database after transaction is complete
<img width="375" alt="Screen Shot 2022-07-19 at 9 34 48 PM" src="https://user-images.githubusercontent.com/27727185/179798021-2bbb3588-bc6d-4c0b-ae85-a25ad7986ed9.png"><img width="282" alt="Screen Shot 2022-07-19 at 9 34 24 PM" src="https://user-images.githubusercontent.com/27727185/179798067-9f828074-df31-4c32-b5a6-c8df0b188e56.png">

