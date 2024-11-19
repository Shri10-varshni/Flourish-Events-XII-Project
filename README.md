# Flourish Events

Flourish Events is a simple Event Management Project which allows users to manage and book events with features like user login, event booking, and additional services such as catering, decorations, and invitation cards. The application also provides an estimated cost for the selected services and allows users to check the status of their booked events.

This project developed in 2022 as part of a 12th-grade assignment to understand and implement concepts using Python and MySQL. 

Built with `Python 3.10.8`

## User Roles
- **Manager**: Views Reports & Stats of Booked Events
- **Customer**: Event Booking

## Features

- **User Login**: Secure login system with password-based authentication.
- **Event Booking**: Users can browse and book events they wish to host.
- **Event Hosting**: Full support for hosting events with essential tools and information provided.
- **Add-ons**: 
  - **Food (Catering Services)**: Users can choose from various food options for the event.
  - **Decorations**: Different themes and decoration options for personalizing the event.
  - **Invitation Cards**: Option to choose invitation card designs for the event.
- **Estimated Cost**: An estimated cost is displayed based on the selected services and add-ons.
- **Event Status**: Users can check the status of their booked events (e.g., confirmed, pending, etc.).

## Data Model

The application uses the following data models:

### 1. *User Information*
   - Stores information about the users such as name, contact details, and login credentials.
   
### 2. *User Registry*
   - A record of all users who have registered on the platform.

### 3. *Event Registry*
   - Contains data about the events that have been booked by users, including event name, date, and location.
   
### 4. *Event Addon Registry*
   - Details about the add-ons chosen for an event (food, decorations, invitations).
   
### 5. *Event Type Information* (Constant)
   - A predefined set of event types (e.g., wedding, corporate event, birthday party).
   
### 6. *Add-on Information* (Constant)
   - A predefined set of available add-ons (e.g., food, decorations, invitations).
   
### 7. *Location* (Constant)
   - A list of available locations or venues for hosting events (e.g., banquet halls, outdoor spaces).

## Technology Stack

- **Backend**: Python (using MySQL connector for database management)
- **Database**: MySQL (for storing user and event-related data)
- **Interface**: Command-line based

## Project Structure
- `src/`: Contains all source code.
- `Documents/`: Documentats related to the project.
- `Properties/`: SQL Connection & Scripts.
- `requirements.txt`: List of dependencies for the project.

## Setup Instructions
1. Clone the repository: `git clone https://github.com/username/Flourish-Events.git`
2. Create a virtual environment: `python -m venv env`
3. Activate the environment:
  - Windows: `env\Scripts\activate`
  - Linux/Mac: `source env/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up the Database: 
  - Open the file `SQL Commands - Flourish Events` located in the `Properties` folder.
  - Run the SQL commands in your MySQL Workbench to create the required database, tables, and initial data.
6. Configure Database Connection:
  - Create a config.py file inside the src folder with the following content:
```python
DB_HOST = "localhost"
DB_USER = "ADMIN_USER"
DB_PASSWORD = "Your Password"
DB_NAME = "EVENT_MANAGER"
```
7. Run the Application: `python src/FlourishMain.py`

