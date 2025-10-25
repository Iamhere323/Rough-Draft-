# Car Rental System

### A simple car rental application for browsing and booking rental vehicles

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)]()

A user-friendly car rental application that allows travelers to browse vehicles, search by type, and make reservations. Built as an educational project for CPSC 362 - Software Engineering at California State University, Fullerton.

![Car Rental Demo](https://via.placeholder.com/800x400?text=Car+Rental+System+Demo)

# Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [System Diagram](#system-diagram)
- [Known Issues](#known-issues)
- [To-Do Items](#to-do-items)
- [Team Members](#team-members)
- [License](#license)

# Project Description

[(Back to top)](#table-of-contents)

The **Car Rental System** is an application designed to simplify the car rental process for travelers. Whether you're a business traveler needing a quick rental for a work trip, a local resident whose car is in the shop, or planning a vacation, our system provides an easy way to browse, search, and reserve rental vehicles.

The system allows users to:
- Browse available rental vehicles with detailed information
- Search and filter cars by type (sedan, SUV, sports car)
- View pricing and vehicle specifications
- Make reservations with flexible date selection
- Manage rental bookings

**Note:** This is an educational project. No real transactions or personal data are processed.

## Features

- **Easy Registration**: Quick account creation to get started
- **Vehicle Catalog**: Browse through available vehicles with photos and specifications
- **Smart Search**: Filter vehicles by type, price range, and features
- **Flexible Booking**: Select rental dates and reserve your preferred vehicle
- **Reservation Management**: View and manage your current and past rentals
- **Rate Information**: Transparent pricing for all vehicle types

# Installation Instructions

[(Back to top)](#table-of-contents)

## System Requirements

- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **Python**: Version 3.8 or higher
- **Internet Connection**: Required for initial download

## Installation Steps

### Option 1: Download from GitHub

1. **Download the application**
   - Visit our [GitHub repository](https://github.com/Iamhere323/Rough-Draft-updated-10.06.25)
   - Click the green "Code" button
   - Select "Download ZIP"
   - Extract the ZIP file to your desired location

2. **Install Python** (if not already installed)
   - Visit [python.org](https://www.python.org/downloads/)
   - Download Python 3.8 or higher
   - Run the installer and check "Add Python to PATH"

3. **Launch the application**
   - Open the extracted folder
   - Double-click `main_menu.py` to start the application
   - Alternatively, open terminal/command prompt in the folder and run:
```bash
     python main_menu.py
```

### Option 2: Quick Start (Future Release)

*A standalone executable with one-click installation will be available in future releases.*

# Usage

[(Back to top)](#table-of-contents)

## Getting Started

When you first launch the application, you'll see the main menu:
```
==========================================
    CAR RENTAL SYSTEM - MAIN MENU
==========================================
1. View Available Cars
2. Rent a Car
3. Return a Car
4. View My Rentals
5. Search Cars by Type
6. View Rental Rates
7. Customer Registration
8. Exit
==========================================
```

## Step-by-Step Guide

### First Time Users

1. **Create an Account**
   - Select option `7` (Customer Registration)
   - Enter your name and email
   - You're now ready to browse and rent!

2. **Browse Available Vehicles**
   - Select option `1` (View Available Cars)
   - Browse through the list of available vehicles
   - Note the vehicle details and pricing

3. **Search for Specific Vehicle Types**
   - Select option `5` (Search Cars by Type)
   - Choose from sedan, SUV, sports car, or electric
   - View filtered results matching your preference

4. **Make a Reservation**
   - Select option `2` (Rent a Car)
   - Choose your desired vehicle
   - Enter pickup and return dates
   - Confirm your reservation

### Managing Your Rentals

- **View Your Rentals**: Select option `4` to see all your current and past reservations
- **Return a Vehicle**: Select option `3` when you've completed your rental period
- **Check Rates**: Select option `6` to view pricing for different vehicle categories

# System Diagram

[(Back to top)](#table-of-contents)

## Application Structure
```
┌─────────────────┐
│      User       │
├─────────────────┤
│ - User ID       │
│ - Name          │
│ - Email         │
│ - Rentals       │
└────────┬────────┘
         │
         │ Makes
         ▼
┌─────────────────┐         ┌─────────────────┐
│   Reservation   │  For    │     Vehicle     │
├─────────────────┤◄────────├─────────────────┤
│ - Booking ID    │         │ - Vehicle ID    │
│ - Start Date    │         │ - Brand         │
│ - End Date      │         │ - Model         │
│ - Vehicle       │         │ - Type          │
│ - Customer      │         │ - Price/Day     │
└─────────────────┘         │ - Available     │
                            └─────────────────┘
```

## User Flow
```
Start → Register/Login → Browse Vehicles → Search/Filter → Select Vehicle → 
Enter Dates → Confirm Booking → View Confirmation → Manage Rentals
```

*[Screenshots and video walkthrough will be added in the next release]*

# Known Issues

[(Back to top)](#table-of-contents)

We're actively working to improve the application. Here are some current limitations:

- **Data Persistence**: Bookings are currently stored temporarily and reset when the application closes
- **Payment Processing**: No actual payment integration (educational simulation only)
- **Limited Availability Tracking**: Real-time availability updates are not yet implemented
- **Single User Sessions**: Only one user can use the application at a time on the same machine
- **Basic Interface**: Console-based interface (GUI version planned for future release)

*If you encounter any issues not listed here, please contact our team or open an issue on GitHub.*

# To-Do Items

[(Back to top)](#table-of-contents)

## Planned Features

We're continuously working to enhance the Car Rental System. Here are some features we plan to add:

### Upcoming Enhancements
- **Database Integration**: Persistent storage of user accounts, vehicles, and reservations
- **Location-Based Search**: Find rental locations near you with interactive maps
- **Advanced Filtering**: Search by price range, fuel efficiency (MPG), vehicle size, and features
- **Corporate Accounts**: Special features for businesses renting multiple vehicles
- **Graphical Interface**: User-friendly web-based interface for easier navigation

### Long-Term Goals
- **Mobile Application**: iOS and Android apps for on-the-go bookings
- **Vehicle Ratings & Reviews**: See what other customers think about each vehicle
- **Real-Time Availability**: Live updates on vehicle availability across all locations
- **Multi-Language Support**: Interface available in multiple languages

*Have a feature request? Let us know through our GitHub repository!*

# Team Members

[(Back to top)](#table-of-contents)

- **Oracio S Miranda** - [@Iamhere323](https://github.com/Iamhere323)  
- **Mohamed Aiad** - [@maiad22](https://github.com/maiad22) 
- **Mohammad Ali Khan** - [@malikhan25](https://github.com/malikhan25) 
- **Cameron Tran** - [@Camerontran71](https://github.com/Camerontran71) 
- **Shigeyasu Kameda** - [@ShigeyasuKameda](https://github.com/ShigeyasuKameda) 

# License

[(Back to top)](#table-of-contents)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Course:** CPSC 362 - Software Engineering  
**Semester:** Fall 2025  
**Institution:** California State University, Fullerton

*This is an educational project developed as part of our Software Engineering coursework. No real personal data, payments, or reservations are processed.*

