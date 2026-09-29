# Vehicle Rental System

A simple first-year college Python project made using Tkinter and JSON.

## Overview

The Vehicle Rental System is a desktop application that helps a small rental shop manage its vehicles. A user can add, search, rent, return, and remove vehicles. Rental charges are calculated automatically and a simple receipt is displayed.

The project is intentionally kept understandable and modular so that the main Python concepts can be explained during a viva.

## Features

- Add a new vehicle
- Search by ID, name, or vehicle type
- View available/rented status
- Rent a vehicle
- Calculate rental amount
- 5% discount for rentals of 3–6 days
- 10% discount for rentals of 7 or more days
- Return a rented vehicle
- Remove an available vehicle
- Save data in `vehicles.json`
- Basic validation and error messages
- Rental receipt
- Basic tests

## Major Functional Modules

### 1. Vehicle Management
Handles adding, searching, finding, and removing vehicles.

### 2. Rental Management
Handles renting and returning vehicles and calculating the bill.

### 3. Data Management
Stores and loads vehicle data using JSON.

### 4. GUI
Provides the Tkinter desktop interface and connects user actions to the modules.

### 5. Validation and Receipt
Checks user input and creates a simple rental receipt.

## Technologies Used

- Python
- Tkinter
- JSON
- Object-Oriented Programming
- File Handling
- Basic Testing

No third-party package is required.

## Folder Structure

```text
Vehicle_Rental_Project/
│
├── main.py
├── vehicle.py
├── vehicle_manager.py
├── rental_manager.py
├── data_manager.py
├── validators.py
├── receipt.py
├── gui.py
├── test_project.py
├── requirements.txt
├── statement.md
└── README.md
```

## How to Run

1. Install Python 3.10 or newer.
2. Keep all files in the same folder.
3. Open Command Prompt or terminal in that folder.
4. Run:

python main.py


The program creates `vehicles.json` automatically on first run.

## Testing

Run:


python test_project.py


Expected output:


All basic tests passed.


If `pytest` is installed, the same tests can also be run with:


pytest test_project.py


## Input and Output

### Inputs
- Vehicle ID
- Vehicle name
- Vehicle type
- Price per day
- Customer name
- Phone number
- Number of rental days
- Search text

### Outputs
- Vehicle table
- Available/Rented status
- Error or validation messages
- Rental receipt
- Calculated amount, discount and total

## Limitations

- Only local JSON storage is used.
- There is no login system.
- Rental history is not stored separately.
- It is intended for a small academic demonstration.

## Future Enhancements

- Store complete rental history
- Add customer management
- Add login and user roles
- Add reports
- Use SQLite instead of JSON
- Add date and time of rental
