# Banking Application

This is a simple banking application written in Python that allows users to create accounts, log in, deposit, withdraw, and transfer funds. The application is designed to be a command-line interface (CLI) program with user interaction via terminal inputs.

## Features

- **Create a New Customer**: Allows users to create a new bank account.
- **Log In**: Users can log in to their account using a PIN.
- **Deposit**: Users can deposit money into their account.
- **Withdraw**: Users can withdraw money from their account.
- **Transfer**: Users can transfer money to other accounts.
- **Display Number of Customers**: Shows the total number of users in the bank.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Set Up Environment**:

    Make sure you have Python installed. You can use a virtual environment to manage dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

1. **Run the Application**:

    Navigate to the `BANK` directory and run:

    ```bash
    python MainApp.py
    ```

2. **Interact with the Application**:

    Follow the on-screen prompts to create a new user, log in, deposit, withdraw, or transfer funds.

## Docker Setup

1. **Build the Docker Image**:

    Navigate to the project root directory (where the `Dockerfile` is located) and build the Docker image:

    ```bash
    docker build -t banking-app .
    ```

2. **Run the Docker Container**:

    Run the application in a Docker container:

    ```bash
    docker run -it banking-app
    ```

