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

3. **Install Dependencies**:

    Install the required Python packages. If you have a `requirements.txt` file, use:

    ```bash
    pip install -r requirements.txt
    ```

    If not, ensure you have the following packages (or any other required ones):

    ```bash
    pip install psycopg2
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

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request with your changes.

1. **Fork the Repository**: Click the "Fork" button on GitHub.
2. **Create a New Branch**:

    ```bash
    git checkout -b feature/your-feature
    ```

3. **Make Your Changes** and **Commit**:

    ```bash
    git add .
    git commit -m "Add your message here"
    ```

4. **Push Your Changes**:

    ```bash
    git push origin feature/your-feature
    ```

5. **Submit a Pull Request**: Go to the GitHub page for your forked repository and click the "New Pull Request" button.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Python and its standard library
- [psycopg2](https://pypi.org/project/psycopg2/) for PostgreSQL integration

For any questions or issues, please contact [your-email@example.com](mailto:your-email@example.com).

