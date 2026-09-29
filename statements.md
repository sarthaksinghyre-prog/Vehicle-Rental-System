EHICLE RENTAL SYSTEM

Project Statement

1. Project Title

Vehicle Rental System

2. Project Statement

The Vehicle Rental System is a Python-based desktop application developed to manage the basic operations of a small vehicle rental business. The system provides a graphical user interface using Tkinter and stores vehicle information locally in a JSON file.

The application allows the user to add new vehicles, search for vehicles, view their availability, rent an available vehicle, return a rented vehicle, and remove an available vehicle. It also calculates the rental amount automatically and applies discounts according to the number of rental days.

3. Problem Statement

Managing vehicle rental information manually can make it difficult to keep track of available and rented vehicles. Manual calculations can also result in errors in rental charges and discounts.

This project provides a simple computer-based solution that keeps vehicle information organized, checks vehicle availability, calculates rental charges, and saves updated vehicle data automatically.

4. Objectives

The main objectives of the project are:

To develop a simple vehicle rental management system.

To practice Python classes, objects, functions, and modules.

To create a graphical user interface using Tkinter.

To store vehicle data using JSON file handling.

To allow users to add, search, rent, return, and remove vehicles.

To validate important user inputs.

To calculate rental charges and discounts automatically.

To generate a simple rental receipt.

To organize the application into separate and reusable modules.

5. Technologies Used

Programming Language: Python

GUI: Tkinter

Data Storage: JSON

Programming Concepts: Object-Oriented Programming, Functions, Modules, File Handling

Testing: Basic Python tests

No third-party package is required for the basic application.

6. Main Modules

6.1 Vehicle Module

The vehicle.py file contains the Vehicle class. It stores the vehicle ID, vehicle name, vehicle type, rental price per day, and availability status.

6.2 Vehicle Manager

The vehicle_manager.py file manages vehicle operations such as:

Adding a vehicle

Finding a vehicle by ID

Searching by ID, name, or type

Removing an available vehicle

Saving updated vehicle data

6.3 Rental Manager

The rental_manager.py file handles:

Rental processing

Customer details

Rental-day validation

Rental bill calculation

Discount calculation

Marking a vehicle as rented

Returning a rented vehicle

6.4 Data Manager

The data_manager.py file handles JSON storage. It loads vehicle records from vehicles.json, saves updated records, and creates initial sample vehicle data when required.

6.5 GUI Module

The gui.py file provides the Tkinter graphical interface. It displays vehicles in a table and provides controls for searching, adding, renting, returning, removing, and exiting the application.

6.6 Validation Module

The validators.py file checks:

Vehicle ID

Vehicle name

Vehicle type

Rental price

Number of rental days

Customer phone number

6.7 Receipt Module

The receipt.py file generates a simple rental receipt containing customer information, vehicle information, rental days, price, amount, discount, and final total.

7. Functional Requirements

The system provides the following functions:

Add a new vehicle.

Search for a vehicle using ID, name, or vehicle type.

Display vehicle availability.

Rent an available vehicle.

Enter customer name and phone number.

Enter the number of rental days.

Calculate rental charges.

Apply a 5% discount for rentals of 3–6 days.

Apply a 10% discount for rentals of 7 or more days.

Return a rented vehicle.

Remove an available vehicle.

Save vehicle information to JSON.

Display a rental receipt.

Show validation and error messages.

8. Inputs

The application accepts the following inputs:

Vehicle ID

Vehicle name

Vehicle type

Price per day

Customer name

Customer phone number

Number of rental days

Search text

9. Outputs

The application produces:

Vehicle information table

Available/Rented status

Validation and error messages

Rental receipt

Rental amount

Discount amount

Final rental total

10. Billing Statement

The rental amount is calculated using:

Amount = Price per Day × Number of Days

Discount rules:

If rental days are less than 3: No discount

If rental days are 3–6: 5% discount

If rental days are 7 or more: 10% discount

The final bill is:

Total = Amount − Discount

For example, if the price is Rs. 1000 per day and the customer rents the vehicle for 3 days:

Amount = Rs. 3000

Discount = Rs. 150

Total = Rs. 2850

11. Working of the System

The user starts the application.

The program loads existing vehicle data from vehicles.json.

The vehicle list is displayed in the GUI.

The user can search for a vehicle or display all vehicles.

The user can add a new vehicle by entering its details.

Before a rental, the user selects an available vehicle.

Customer name, phone number, and rental days are entered.

The system validates the entered information.

The rental amount and applicable discount are calculated.

The vehicle status changes from available to rented.

Updated data is saved to the JSON file.

A rental receipt is displayed.

When the vehicle is returned, its status changes back to available.

An available vehicle can also be removed from the system.

12. Data Storage

The project uses a local file named vehicles.json instead of a database.

Each vehicle record contains:

vehicle_id

name

vehicle_type

price

available

Example vehicle records include cars, bikes, and scooters such as Maruti Swift, Hyundai i20, Honda City, Royal Enfield, and Honda Activa.

13. Error Handling

The program handles common invalid situations, including:

Empty vehicle details

Invalid rental price

Invalid number of rental days

Invalid phone number

Duplicate vehicle ID

Vehicle not found

Attempting to rent an already rented vehicle

Attempting to remove a rented vehicle

Attempting to return an already available vehicle

Error and warning messages are displayed using Tkinter message boxes.

14. Project Files

The project is divided into the following files:

main.py — Starts the application.

gui.py — Provides the Tkinter graphical interface.

vehicle.py — Defines the Vehicle class.

vehicle_manager.py — Manages vehicle operations.

rental_manager.py — Handles rentals, returns, and billing.

data_manager.py — Handles JSON data storage.

validators.py — Performs input validation.

receipt.py — Generates rental receipts.

test_project.py — Contains basic tests.

vehicles.json — Stores vehicle information.

15. Testing Statement

Basic tests are included in test_project.py. The tests check vehicle creation, rental bill calculation, discount calculation, and returning a rented vehicle.

The expected successful test output is:

All basic tests passed.

16. Limitations

The current version is designed as a small academic project. It uses local JSON storage and does not include a login system, separate rental history, or a database.

17. Future Enhancements

The system can be improved by adding:

Customer management

Complete rental history

Login and user roles

Reports

SQLite database

Rental date and expected return date

Vehicle categories and filters

18. Conclusion

The Vehicle Rental System demonstrates how Python can be used to create a simple desktop application for managing vehicle rentals. The project combines object-oriented programming, Tkinter GUI development, JSON file handling, input validation, billing calculations, and basic testing in a modular structure.

The project provides the basic functionality required for a small vehicle rental operation while also providing a foundation for future improvements.