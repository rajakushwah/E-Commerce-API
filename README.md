# E-commerce API
This is a simple Flask-based e-commerce API that allows users to create products, place orders, and retrieve product information. The application uses SQLite as its database.

## Prerequisites
- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy

   You can install the required packages with the following command:
      ```bash
         pip install -r requirements.txt

## Setting Up the Application

1. **Clone the Repository or Copy the Code**:
   - Clone the repository or copy the code into a new Python file, for example, `app.py`.

2. **Database File**:
   - Ensure you have a SQLite database file named `ecommerce.db` in the same directory, or the application will create one upon first run.

3. **Set the Environment Variable**:
   - Set the environment variable to run the application:
     - On Linux/macOS:
       ```bash
       export FLASK_APP=app.py
       ```
     - On Windows:
       ```cmd
       set FLASK_APP=app.py
       ```

4. **Install Required Packages** (If not done previously):
   - Make sure to install the required packages with the following command:
     ```bash
     pip install Flask Flask-RESTful Flask-SQLAlchemy
     ```
  
## Run the Application**:
   - Execute the following command to run the Flask application:
     ```bash
     flask run
     ```
   - By default, the application will run on `http://127.0.0.1:5000`.

# Flask API Documentation

### 1. Home Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a status message indicating you are at the homepage.

#### Example Request:

    ```bash
    GET http://127.0.0.1:5000/

### Example Response

The response from the Home endpoint will be a JSON object formatted as follows:

    ```json
    {
      "id": "Demo",
      "status": "You are at homepage"
    }


### 2. Order Create Endpoint

- **URL:** `/order` (or the appropriate endpoint you set up for this function)
- **Method:** `POST`
- **Description:** Creates a new order with the specified products.

#### Request

The request body must be a JSON object with the following structure:

     ```json
             {
               "products": [
                 {
                   "id": "product_id_1",
                   "quantity": 2
                 },
                 {
                   "id": "product_id_2",
                   "quantity": 1
                 }
               ]
             }

### Example Request

    ```bash
    POST http://127.0.0.1:5000/order
    Content-Type: application/json
    
    {
      "products": [
        {
          "id": "product_id_1",
          "quantity": 2
        },
        {
          "id": "product_id_2",
          "quantity": 1
        }
      ]
    }

### Responses

#### Success Response

- **Status Code:** `201 Created`
- **Content:** A JSON object containing the order details.

##### Example Success Response:

    ```json
    {
      "id": "new_order_id",
      "status": "Order created successfully"
    }

### Error Responses

#### Insufficient Stock

If the stock for any product is not enough to fulfill the order, the API will respond with a `400 Bad Request`.

- **Status Code:** `400 Bad Request`
- **Content:** A JSON object indicating the error.

##### Example Error Response:

    ```json
    {
      "error": "Not enough stock for product product_id_1"
    }

### 3. Get all Products

## Endpoint

### GET /agetproducts

**Description:**  
Retrieves a list of all available products, including their ID, name, description, price, and stock information.

## Request

- **Method:** `GET`
- **URL:** `/getproducts
  
### Example Request
- endpoint/getproducts


## Response

- **Status Code:** `200 OK`
- **Content-Type:** `application/json`

### Response Format
The API returns a JSON array of product objects. Each product object contains the following fields:

- **id** (integer): The unique identifier for the product.
- **name** (string): The name of the product.
- **description** (string): A brief description of the product.
- **price** (float): The price of the product.
- **stock** (integer): The available stock for the product.

### Example Response
    ```json
    [
        {
            "id": 1,
            "name": "Product A",
            "description": "Description for Product A.",
            "price": 29.99,
            "stock": 100
        },
        {
            "id": 2,
            "name": "Product B",
            "description": "Description for Product B.",
            "price": 49.99,
            "stock": 50
        }
    ]

## Error Responses

In case of errors, the API may return the following status codes:

- **400 Bad Request**: 
  - **Description**: This status code indicates the request is invalid or malformed.
  - **Example Response**:
    ```json
    {
        "error": "Bad Request",
        "message": "The request parameters are invalid."
    }
    ```

- **500 Internal Server Error**: 
  - **Description**: This status code indicates an unexpected error occurred while fetching data from the database.
  - **Example Response**:
    ```json
    {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred."
    }
    ```


### 3. Add Products

## Endpoint
**POST** `/postproduct`

## Description
This endpoint allows you to create a new product in the inventory. It requires specific information about the product including its name, price, and stock level.

## Request

### Headers
- **Content-Type**: `application/json`

### Request Body
The request body must be in JSON format and should include the following fields:

| Field       | Type    | Required | Description                              |
|-------------|---------|----------|------------------------------------------|
| `name`      | string  | Yes      | The name of the product.                 |
| `description` | string | No       | A description of the product (optional).|
| `price`     | number  | Yes      | The price of the product.                |
| `stock`     | number  | Yes      | The number of items available in stock.  |

#### Example Request Body
    ```json
    {
      "name": "Sample Product",
      "description": "This is a sample product.",
      "price": 19.99,
      "stock": 100
    }

## Response

### Success Response
- **Status Code**: `201 Created`
- **Response Body**:
  ```json
  {
    "id": 1
  }


