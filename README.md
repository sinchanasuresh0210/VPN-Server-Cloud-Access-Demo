
Highlight the most important aspects of your application:

  * **AI-Powered Mobile Assistant:** Integrated AI chat via the `/api/ai-assistant` endpoint, using the `google-generativeai` library to provide concise answers about VPNs, security, and cloud access.
  * **Secure User Authentication:** Login functionality with hardcoded credentials ().
  * **VPN Dashboard:** A protected route (`/vpn-details`) that displays simulated session statistics, including data usage and battery impact.
  * **Multi-Client Support:** Includes both a Flask web application and a standalone Python Tkinter desktop client that communicates with the same AI backend.
  * **Modern Web UI:** Responsive design using HTML and CSS (as seen in `index.html`, `login.html`, etc.).

### 3\. Getting Started (Installation & Setup)

This tells users how to run your code.

#### Prerequisites

  * Python 3.8+

#### Setup

1.  **Clone the Repository:**

    ```bash
    git clone [your-repo-link]
    cd VPN-CLOUD-AI-Assistant
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure the Gemini API Key:**
    You must set your Gemini API key as an environment variable for the AI assistant to function.

    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY_HERE"
    # Optional: Change the model
    # export GEMINI_MODEL="gemini-1.5-flash"
    ```

4.  **Run the Flask Application:**

    ```bash
    python app.py
    ```

    The web server will be running at `http://127.0.0.1:5000`.

### 4\. Usage

#### Web Dashboard

1.  Open your browser to `http://127.0.0.1:5000`.
2.  Login using the demo credentials:
      * **Username:** 
      * **Password:** 
3.  Access the AI Assistant on the home page (`/`) or the VPN details page (`/vpn-details`).

#### Desktop Client

1.  While the Flask server is running, open a new terminal.
2.  Run the desktop client:
    ```bash
    python desktop_client.py
    ```
3.  Chat with the AI Assistant through the Tkinter interface.

### 5\. Project Structure

A brief overview of the files you included:

  * `app.py`: The main Flask application, handling routes, session management, and the Gemini API interaction.
  * `desktop_client.py`: A standalone Python Tkinter application for chatting with the AI backend.
  * `index.html`: The main landing page with the hero section and embedded AI chat.
  * `login.html`: The user login page.
  * `vpn_details.html`: Displays simulated VPN usage and login count after successful authentication.
  * `requirements.txt`: Project dependencies, including `flask` and `google-generativeai`.

### 6\. Technologies Used

  * Python
  * Flask
  * Jinja2 (Templating)
  * Tkinter (Desktop Client)
  * Google Gemini API (`google-generativeai`)

Acknowledgements

Special thanks to [Ayush S](https://github.com/ayush007-lio) for guidance and support.
