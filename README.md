# Clinic Django RestAPIs Project
The clinic Backend is a Django Rest API designed to serve the clinic frontend
## System requirements
### Python3 installation
To install Python3 on your machine, you can follow these steps:

1. Visit the official Python website at https://www.python.org.

2. On the Python website, navigate to the "Downloads" section.

3. Choose the appropriate installer for your operating system. Python is available for Windows, macOS, and Linux. Click on the download link for your desired version and operating system.

4. Once the installer is downloaded, run it and follow the installation wizard instructions. You may need administrative privileges to install Python on your machine.

5. During the installation, you will have the option to customize the installation settings. The default settings should work fine for most users, but you can choose additional features or customize the installation directory if needed.

6. check the box that says "Add Python to PATH" or a similar option during the installation process. This will ensure that the Python executable is accessible from the command prompt or terminal.

7. After the installation is complete, open a new command prompt or terminal window and verify the installation by running the following command:
   ```shell
   python --version
   ```
   This command will display the installed Python version.

Python3 is now successfully installed on your machine. You can use Python for various purposes, such as running scripts, building applications, or working with data analysis and machine learning.

To check if pip is installed, you can run the following command in the terminal:
```
pip --version
```
If pip is installed, it will display the installed version.

### PostgreSQL installation
To install PostgreSQL, a popular open-source relational database management system, you can follow these steps:

1. Visit the official PostgreSQL website at https://www.postgresql.org.

2. On the PostgreSQL website, navigate to the "Downloads" section.

3. Choose the appropriate installer for your operating system. PostgreSQL is available for Windows, macOS, and various Linux distributions. Click on the download link for your desired version and operating system.

4. Once the installer is downloaded, run it and follow the installation wizard instructions. You may need administrative privileges to install PostgreSQL on your machine.

5. During the installation, you will have the option to customize the installation settings. The default settings should work fine for most users, but you can choose additional features or customize the installation directory if needed.

6. Set the password for the `postgres` user, which is the default superuser account in PostgreSQL. Make sure to remember this password, as you will need it for administrative tasks.

7. Complete the installation process by following the remaining instructions in the installation wizard.

8. After the installation is complete, you can verify the installation by opening a command prompt or terminal and running the following command:
   ```shell
   psql --version
   ```
   This command will display the installed PostgreSQL version.

PostgreSQL is now successfully installed on your machine. You can start using PostgreSQL by connecting to the database using client tools such as `psql` or by using programming languages and frameworks that support PostgreSQL as a backend database.


Therefore ensure the following libraries are in your appropriate operating system.
```
python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

eg. in Linux run the following commands for instalation
```
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```


## Installation

1. Create a virtual environment and activate it:

  ```
  sudo -H pip3 install --upgrade pip
  ```
  ```
  sudo -H pip3 install virtualenv
  ```
  ```
  mkdir ~/myprojectdir
  ```
  ```
  cd ~/myprojectdir
  ```
  ```
  virtualenv env
  ```
  ```
  source env/bin/activate
  ```

  2. Clone the repository to your local machine inside the virtual environment directory:

  ```
https://github.com/rexy09/clinic_backend.git
  ```

3. Install the project dependencies inside the project directory:
 ```
 cd clinic_backend
  ```

  ```
  pip3 install -r requirements.txt
  ```

4. Create a `.env` file inside the project directory from the `example.env` structure.

5. Add SECRET_KEY and DEBUG values inside the `.env` file.
  ```
  # Django Server Configuration
  export SECRET_KEY = ''
  export DEBUG = 'True'
  ```

6. Create a PostgreSQL database and update the DATABASES setting in the `.env` file with your database credentials:
  ```
  # Database Configurations
  export DB_NAME = 'database_name'
  export DB_USER = 'database_user'
  export DB_PASSWORD = 'database_passwd'
  export DB_HOST = '127.0.0.1'
  export DB_PORT = '5432'
  ```
  
7. Navigate inside the project directory:
```
cd clinic_backend
```

8. Run the database migrations:
  ```
  python3 manage.py makemigrations
  ```
  ```
  python3 manage.py migrate
  ```  
9. Start the development server:
  ```
  python3 manage.py runserver
  ```
15. Open your web browser and navigate to http://localhost:8000 to access the application.


