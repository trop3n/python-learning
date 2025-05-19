# Pro7
API endpoints and scripts for modify ProPresenter 18

# Instructions for Use

## 1. Enable the ProPresenter API

  - Open ProPresenter and go to Preferences.
  - Navigate to the **API** or **Remote Control**
  - Note the **IP address, port**, and any **authentication credentials** (username/password or API key) if required.

---

## 2. Understand the ProPresenter API

  - ProPresenter's API is typically REST-based or WebSocket-based, depending on the version.
  - Refer to the official ProPresenter API documentation for details on available endpoints, methods, and data formats. You can find this in the ProPresenter user manual or on their website.

---

## 3. Install Required Python Libraries

  - To interact with the API, you'll need libraries like `requests` for REST APIs or `websockets` for WebSocket APIs.
  - Install them using `pip`:
  ```bash
     pip install requests websockets
  ```
