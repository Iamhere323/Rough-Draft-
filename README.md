# Rough-Draft-
Oracio S Miranda, Github username: IAMHERE323


Mohamed Aiad, github username: maiad22


Mohammad Ali Khan, github username: malikhan25


Cameron Tran, github username: Camerontran71


Shigeyasu Kameda, github username: Shigeyasu Kameda


prompt ##


Travel booking system


inception = We want to create a user friendly system to book and search 

            target customer : travelers anyone looking for rental
            
            nature user for try : user friendly application that can help you search based on location


Eliciation = Functional : what rentals will be available 
                          search functions
                          reservations
                          payments
            non - function: run 24/7 
                            code be change easily(maintenance ability)
                            we want it to run on multiple device
                            security/write encryte code
                            updates

            for user_stories: traveler needs a car rental
                              local car been in an accident/totaled
                              a business looking to rent multiple vehicle 
                              a businesses looking to list vehicles for personal use

Elaboration = classes : Travelers, vehicle, business, user_interface, customer_information, payment_processing, time_frame

            
                            
# final_draft--




Section 1: Prompt Selection
Our group has selected the Car Rental System prompt for our project.
Github link : https://github.com/Iamhere323/Rough-Draft-/blob/main/README.md 

NAMES:
Oracio S Miranda, Github username: IAMHERE323
Mohamed Aiad, github username: maiad22
Mohammad Ali Khan, github username: malikhan25
Cameron Tran, github username: Camerontran71
Shigeyasu Kameda, github username: Shigeyasu Kameda
Section 2: Requirements Solicitation


1. Inception
Company Background: RentaCar Express is a 40-year-old car rental company that has recently been acquired by new ownership. The company currently generates $25 million in annual revenue through traditional brick-and-mortar locations across 15 major metropolitan areas. However, the company is losing market share to competitors like Enterprise, Hertz, and emerging digital-first platforms like Turo.
Business Opportunity: The digital transformation represents a critical strategic opportunity to:
Increase Revenue: Projected 30% revenue increase within 18 months through online bookings and expanded customer reach
Market Share Recovery: Recapture lost customers who have migrated to competitors' online platforms
Competitive Positioning: Establish tech that competes with industry leaders in digital customer experience
Operational Efficiency: Reduce customer wait times and staffing costs at physical locations
This is a time-bound opportunity; competitors are already dominant in the online space, and RentaCar Express risks losing its existing market share and becoming obsolete if it doesn't adapt within the next 12 to 18 months.
Market Research: The company's newly formed Digital Strategy Department conducted:
Customer survey of 2,500 existing customers revealing 78% prefer online booking
Competitive analysis showing all major competitors have comprehensive online platforms
Industry trend analysis indicating 65% of car rentals are now booked online
Target Customer Segments:
Business Travelers (40% of target market)
Existing customers who frequently rent for work trips
Need quick, efficient booking and modification capabilities
Value integration with corporate accounts and expense systems
Leisure Travelers (35% of target market)
Mix of existing and new customers planning vacation rentals
Want to compare vehicle options and prices before arriving
Prefer advance booking for peace of mind
Local Emergency Renters (15% of target market)
New customer segment: locals whose cars are in accidents/repair
Need immediate availability checking and quick booking
Price-sensitive with shorter rental durations
Corporate Fleet Customers (10% of target market)
Businesses needing multiple vehicle rentals
Existing high-value customers requiring bulk booking capabilities
Need administrative controls and reporting features
Nature of Solution
Framework: 
Website: Flask (Python) + HTML/CSS/JavaScript frontend + SQLite database 
Mobile App: Kivy (Python-based Cross-platform mobile framework)
Scalability: Support for 10,000 concurrent users during peak times
Uptime Target: 99.9% availability (maximum 8.7 hours downtime per year)
Security: SSL encryption, PCI DSS compliance for payment processing
User Experience Features:
Account Management: User registration/login with profile management
Intelligent Search: Location-based vehicle search with filters (brand, type, model, color, mpg(fuel), size, price, features)
Recommendation Algorithm/Engine: Personalized vehicle suggestions based on rental history
Real-time Availability: Live inventory updates across all locations
Flexible Booking: Modification and cancellation capabilities
Mobile Responsive: Optimized for desktop, tablet, and mobile devices


3. Elicitation
Project Goals:
Functional Requirements (4): 
1. The system must allow users to search for available vehicles based on location, dates, and vehicle type. 
2. The system must process secure online payments for reservations. 
3. The system must allow users to create and manage their profiles and reservations. 
4. The system must provide an administrative dashboard for managing information, vehicle inventory and reservations.
Non-Functional Requirements (4):
Reliability: The system must be available 24/7 with minimal downtime for maintenance.
Maintainability: The codebase must be well-documented and modular to allow for easy updates and bug fixes.
Cross-Platform Compatibility: Responsive design supporting desktop, tablet, and mobile devices
Security: All user data, including personal information and payment details, must be encrypted and protected from unauthorized access.



User Stories:
Actor: Business Traveler
1. The traveler logs into the RentaCar Express website/app with credentials.
2. The traveler enters pickup location, return location, and rental dates.
3. The system displays available vehicles with prices and features.
4. The traveler selects their preferred vehicle and reviews rental details.
5. The traveler enters card information for billing.
6. The system processes the reservation and displays confirmation with booking reference.
Actor: Local Emergency Renter
The local resident opens the mobile app and creates a new account.
The system detects current location and displays nearby rental locations.
The resident selects the closest location and chooses rental duration.
The resident enters payment information and accepts rental terms.
The system confirms booking and sends pickup instructions with location details.
Actor: Business Client Renting
1. The business owner logs into the corporate dashboard and creates a company account.
2. The owner enters employee information and assigns vehicle access permissions.
3. The system displays a bulk booking interface with corporate discount pricing.
4. The owner selects multiple vehicles for different employees and time periods.
5. The system applies bulk discount and processes the corporate reservation.
6. The system generates individual booking confirmations for each employee.
Actor: Business/Client Listing
1. The user registers as a vehicle provider on the platform.
2. The user enters fleet details including vehicle specifications and pricing.
3. The system verifies vehicle documentation and insurance requirements.
4. The user sets availability, schedules, and rental rates for each vehicle.
5. The system activates the fleet listings and displays them to customers.
6. The user receives booking notifications and manages reservations through the portal.
3. Elaboration
Grammatical Parse Analysis (nouns underlined, verbs italicized) using the second user story: Local Emergency Rental: The local resident opens the mobile app and creates a new account. The system detects current location and displays nearby rental locations. The resident selects the closest location and chooses rental duration. The resident enters payment information and accepts rental terms. The system confirms booking and sends pickup instructions with location details.
Extracting Potential Classes:

Potential Class
General Classification
Local resident
Role or external entity
Mobile app
External entity
Account
Thing
System
Thing
Location
Place
Rental locations
Place
Resident
Role or external entity 
Rental duration
Thing
Payment information
Thing
Rental terms
Thing
Booking
Occurrence
Pickup instructions
Thing
Location details
Thing


