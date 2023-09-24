# Authentication App User Manual

## Introduction

The Authentication App is a simple web application that allows users to input their first name, last name, and email address. The app then saves this information in a PostgreSQL database. This user manual will guide you through the installation process and explain how to use the app.

## Installation

To install and run the Authentication App, please follow these steps:

1. Clone the repository from GitHub: `git clone https://github.com/your-repo/authentication-app.git`
2. Navigate to the project directory: `cd authentication-app`
3. Install the required dependencies:
   - Node.js: Install Node.js from the official website (https://nodejs.org) if you haven't already.
   - PostgreSQL: Install PostgreSQL from the official website (https://www.postgresql.org) if you haven't already.
4. Set up the PostgreSQL database:
   - Create a new database in PostgreSQL.
   - Update the `db.js` file in the project with your PostgreSQL database credentials.
5. Install the Node.js dependencies:
   - Run `npm install` in the project directory to install the required Node.js packages.

## Usage

To use the Authentication App, please follow these steps:

1. Start the backend server:
   - Run `npm run dev` in the project directory to start the backend server.
2. Access the web application:
   - Open your web browser and navigate to `http://localhost:3000`.
3. Input user details:
   - Enter your first name, last name, and email address in the respective input fields.
4. Save user details:
   - Click the "Save" button to save the user details.
5. Verify user details:
   - You will see an alert message indicating whether the user details were saved successfully or if there was an error.
6. Check the database:
   - Verify that the user details are saved in the PostgreSQL database.

## Troubleshooting

If you encounter any issues while installing or using the Authentication App, please try the following troubleshooting steps:

1. Ensure that you have installed all the required dependencies correctly.
2. Double-check your PostgreSQL database credentials in the `db.js` file.
3. Make sure that the PostgreSQL database is running and accessible.
4. Check the console logs for any error messages.
5. If the issue persists, please contact our support team for further assistance.

## Conclusion

Congratulations! You have successfully installed and used the Authentication App. If you have any further questions or need additional support, please don't hesitate to reach out to our support team. Thank you for choosing our product!