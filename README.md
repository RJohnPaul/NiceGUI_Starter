---

# Simple Authentication Starter Example with NiceGUI

<div align="center">
  <br>
      <img src="https://github.com/RJohnPaul/NiceGUI_Starter/blob/832aea08fa2f6bddd55c1676991881a115e0ceda/Frame%207.png" alt="Project Banner">
  </br>
</div>

<div align="center">
  <br>
      <img src="https://github.com/RJohnPaul/CryptDeCrypt/blob/3848b5636b76ee1a6f3326550d99547d78f8ff1c/Frame-5(1).png" alt="Project Banner">
  </br>
</div>

<br/>

This is a simple authentication example using FastAPI and NiceGUI. It stores session IDs in memory and does not involve password hashing. This example is meant for demonstration purposes and may not be suitable for production use. For a more robust authentication system, consider implementing OAuth2 or using the Authlib package.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/RJohnPaul/NiceGUI_Starter.git
cd NiceguiSimpleAdminPanel
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your own secret key:

```bash
export MY_SECRET_KEY=<your_secret_key>
```

## Required Modules and Software

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python.
- [NiceGUI](https://github.com/zauberzeug/nicegui): A Python library for creating beautiful and interactive user interfaces.
- [Uvicorn](https://www.uvicorn.org/): ASGI server that powers FastAPI.

## Running the Application

Run the following command to start the FastAPI application:

```bash
uvicorn main:ui --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## Features

- **Main Page:** Displays a welcome message and navigation tabs.
- **Login Page:** A stylish login page with a glassmorphic design.
- **Logout Page:** Allows users to log out and redirects to the login page.

## Usage

1. Open the application in your web browser.
2. Navigate to the login page.
3. Enter valid credentials (e.g., username: `system`, password: `sys`).
4. Upon successful login, you will be redirected to the main page.
5. To log out, click the "Log out" button.

Feel free to customize the code and design according to your needs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

<div align="center">
  <br>
      <img src="https://github.com/RJohnPaul/CryptDeCrypt/blob/a047c7dc5028c1c24c4f73e301c189cdbe3e006a/Frame%207.png" alt="Project Banner">
  </br>
</div>

---
