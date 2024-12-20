# Fitness Tracker CLI

A command-line interface (CLI) application to manage fitness activities, users, and goals. The application allows users to add, update, delete, and view activities, as well as manage user profiles and set fitness goals.

## Author

Caleb Kiune

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/fitness_tracker_cli.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd fitness_tracker_cli
    ```

3. **Install the dependencies:**

    ```bash
    pipenv install
    ```

4. **Setup the database:**

    ```bash
    alembic upgrade head
    ```

## Usage

1. **Activate the virtual environment:**

    ```bash
    pipenv shell
    ```

2. **Run the CLI application:**

    ```bash
    python lib/cli.py
    ```

3. **Follow the on-screen prompts to add, update, delete, and view activities, users, and goals.**

## Features

- **User Management:**
  - Add a new user
  - View all users
  - Delete a user

- **Activity Management:**
  - Add a new activity
  - Update an existing activity
  - Delete an activity
  - View all activities

- **Goal Management:**
  - Add a new goal
  - View all goals
  - Delete a goal

## Technology Stack

- **Python**: Programming Language
- **SQLAlchemy**: ORM (Object Relational Mapper)
- **Alembic**: Database migrations
- **Pipenv**: Python dependency management

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to update the documentation as needed.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please reach out to calebkiune@gmail.com.


