# Authentication App User Manual

## Introduction

The Authentication App is a simple application that allows users to input their first name, last name, and email address, and saves this information in a PostgreSQL database. This user manual will guide you through the installation process and explain how to use the application.

## Installation

To install and run the Authentication App, please follow these steps:

1. Install Python: Make sure you have Python installed on your system. You can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Install PostgreSQL: If you don't have PostgreSQL installed, you can download it from the official website: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

3. Clone the repository: Open a terminal or command prompt and navigate to the directory where you want to clone the repository. Then run the following command:

   ```
   git clone https://github.com/your_username/authentication-app.git
   ```

4. Install dependencies: Navigate to the cloned repository directory and install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

5. Configure the database: Open the `database.py` file in a text editor and update the database connection details (host, database name, username, and password) according to your PostgreSQL configuration.

6. Create the database table: Run the following command to create the necessary table in the database:

   ```
   python database.py
   ```

## Usage

To use the Authentication App, follow these steps:

1. Run the application: Open a terminal or command prompt, navigate to the cloned repository directory, and run the following command:

   ```
   python main.py
   ```

2. Enter user information: The application window will open. Enter the user's first name, last name, and email address in the respective input fields.

3. Save user information: Click the "Save" button to save the user's information in the database.

4. Repeat steps 2 and 3 for additional users.

## Closing the Application

To close the Authentication App, simply close the application window or press Ctrl+C in the terminal or command prompt where the application is running.

## Troubleshooting

If you encounter any issues or errors while installing or using the Authentication App, please refer to the following resources:

- Python documentation: [https://docs.python.org/](https://docs.python.org/)
- PostgreSQL documentation: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- GitHub repository: [https://github.com/your_username/authentication-app](https://github.com/your_username/authentication-app)

If you are unable to resolve the issue, please contact our support team for further assistance.

## Conclusion

Congratulations! You have successfully installed and used the Authentication App. This simple application allows you to save user information in a PostgreSQL database. If you have any feedback or suggestions for improvement, please let us know. Thank you for using the Authentication App!