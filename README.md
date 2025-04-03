# Online Store

## Project Description
Online Store is a web application developed with Django that allows efficient management of clients, products, and orders. It includes features such as a contact form, product search, and a user-friendly interface for data management.

## Technologies Used
This project was developed using the following technologies:

- **Python** and **Django**: For the backend and business logic.
- **PostgreSQL**: Database for storing information.
- **HTML, CSS, and JavaScript**: For the user interface.
- **Bootstrap / Tailwind CSS**: For design and styling.
- **Django Forms**: For form management.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_user/your_repository.git
    ```
2. Navigate to the project directory:
    ```sh
    cd OnlineStore
    ```
3. Create a virtual environment:
    ```sh
    python -m venv env
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```
5. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

## Usage

1. Start the development server:
    ```sh
    python manage.py runserver
    ```
2. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application in action.

## Features

- **Client Management**: Allows adding, editing, and deleting clients.
- **Product Management**: Allows adding, editing, and deleting products.
- **Order Management**: Allows adding, editing, and deleting orders.
- **Contact Form**: Allows users to send messages.
- **Product Search**: Allows users to search for products by name.

## Main Files

- `models.py`: Defines the application models.
- `views.py`: Defines the application views.
- `forms.py`: Defines the application forms.
- `settings.py`: Django project configuration.
- `urls.py`: Defines the application routes.

5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
