
```markdown
# Vendor Management System

This is a Django-based REST API designed to manage and track vendor performances, purchase orders, and related metrics. This system is essential for businesses looking to optimize their vendor interactions and improve operational efficiencies.

## Setup Instructions

**Requirements:**
- Python 3.8 or newer
- Django 3.2 or later
- Django REST Framework

**Installation Steps:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Deadlymind/Vendor-Management.git
   cd Vendor-Management
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations to your database:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser account for Django admin:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```

   Access the development server at http://127.0.0.1:8000/.

## Authentication Setup

This project uses JSON Web Tokens (JWT) and `dj-rest-auth` for handling authentication. Ensure you have installed the necessary packages.

### Authentication Endpoints

- `/dj-rest-auth/login/` (POST): Log in a user.
- `/dj-rest-auth/logout/` (POST): Log out the current user.
- `/dj-rest-auth/password/change/` (POST): Change the password for the current user.

For JWT token management:
- `/dj-rest-auth/token/` (POST): Obtain a new JWT.
- `/dj-rest-auth/token/refresh/` (POST): Refresh an existing JWT.

## API Endpoints

- **Vendors:**
  - `GET /api/vendors/`: Retrieve a list of all vendors.
  - `POST /api/vendors/`: Create a new vendor.
  - `GET /api/vendors/{vendor_id}/`: Get details about a specific vendor.
  - `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
  - `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.
  - `GET /api/vendors/{vendor_id}/performance/`: Vendor Performance Metrics

- **Purchase Orders:**
  - `GET /api/purchase-orders/`: List all purchase orders.
  - `POST /api/purchase-orders/`: Create a new purchase order.
  - `GET /api/purchase-orders/{po_id}/`: Retrieve a specific purchase order.
  - `PUT /api/purchase-orders/{po_id}/`: Update a purchase order.
  - `DELETE /api/purchase-orders/{po_id}/`: Delete a purchase order.

- **Historical Performance:**
  - `GET /api/historical-performances/`: Retrieve all historical performance records.
  - `POST /api/historical-performances/`: Log new performance data.

## Swagger Documentation
Access the Swagger UI to interact with the API visually at: http://127.0.0.1:8000/swagger/

## Contributing

Interested in contributing? Great! Please fork the project, make your changes, and submit a pull request. We appreciate your input!

## License

This project is licensed under the [MIT License](https://deadlymind.vercel.app/).
```