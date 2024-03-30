# Project Setup Instructions

## Prerequisites

- Ensure you have Python installed. If not, download and install it from [Python's official website](https://www.python.org/downloads/)

## Installation Steps For Windows

1. **Check Python Installation**

   Open your terminal and run the following command to check if Python is installed:

   ```bash
   python --version
   ```

2. **Install Pipenv**

   Pipenv is used to manage the project's dependencies and virtual environment. Install it using pip:

   ```bash
   pip3 install pipenv
   ```
   
   Verify the installation with:

   ```bash
   pipenv --version
   ```
   > **Note:** If the above step doesn't work, you may need to add Python and Python Scripts directory to your PATH environment variable.
   >    ```
   >    Your directory path might look similar to this:
   >    C:\Users\(Your logged in User)\AppData\Local\Programs\Python\Python312\
   >    C:\Users\(Your logged in User)\AppData\Local\Programs\Python\Python312\Scripts\
   >    ```
   >  After adding Python Scripts to your PATH, try running ```pipenv --version```
   
3. **Clone the Repository**

   In Visual Studio Code (or your preferred IDE), clone the repository into your desired directory:

   ```bash
   git clone https://github.com/moisespal/assignment-3.git
   cd assignment-3/fuelvisionary
   ```
   
4. **Set Up the Virtual Environment and Dependencies**

   While in the `fuelvisionary` directory, set up your virtual environment and install the necessary dependencies:

   ```bash
   pipenv install
   ```

   This command reads the `Pipfile` and installs the required Python packages.

5. **Activate the Virtual Environment**

   To activate the virtual environment, run:

   ```bash
   pipenv shell
   ```
6. **Create a `.env` file in the `fuelVisionary` directory**

   For testing purposes:
      - Add the following line to the `.env` file, replacing `number` with any integer, then save the file:

        SECRET_KEY='number'
   
7. **Run the Development Server**

   Start the Django development server with:

   ```bash
   python manage.py runserver
   ```

   You should see output indicating that the server is running. Now, you can visit http://127.0.0.1:8000/ in your web browser.
   
## Handling Migration Prompts

If the terminal prompts you to apply migrations, please stop the server by pressing `Ctrl + C` and then run the following command:

```bash
python manage.py migrate
```

This command applies all the database migrations required for your project to function correctly.

## Troubleshooting

- If you encounter any issues, make sure you're in the correct directory (`fuelvisionary`) when running `pipenv` commands.
- Ensure that your Python version matches the project's requirements. If necessary, use a tool like `pyenv` to manage multiple Python versions.
- if you're missing any packages try running ```pip install -r requirements.txt```
