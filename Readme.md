# Master Agent: Multi-Tool on Gemini 3

**One tool for everything.** A unified multimodal intelligence that transforms voice, images, and code into action.

---

## 🚀 Overview
Master Agent is a solo-developed project designed to eliminate "AI fragmentation." Built on the cutting-edge **Gemini 3 Flash** model, it provides a single, high-speed interface for creative storytelling, UI analysis, and code optimization.

---

## 🛠️ Built With
* **Model:** Gemini 3 Flash (`gemini-3-flash-preview`)
* **SDK:** Google GenAI SDK
* **Cloud:** Google Cloud Vertex AI
* **Auth:** Google Cloud IAM (Service Accounts)
* **Frontend:** Streamlit
* **Language:** Python 3.13
* **Images:** Pillow (PIL)

---

## 📖 The Project Story

### ## Inspiration
I was inspired by the incredible speed of **Gemini 3 Flash** to build something that feels like a natural extension of human thought. My vision was to create a **Unified Multimodal Intelligence**—a single, powerful hub where voice, vision, and logic meet. I wanted to move beyond single-purpose bots and build a "Swiss Army Knife" for the digital age that makes complex tasks feel effortless.

### ## What it does
**Master Agent** is my versatile digital companion designed to boost productivity across three key domains:
1.  **Creative Storyteller:** Transforms spoken ideas and audio prompts into rich, immersive narratives.
2.  **UI Navigator:** Provides high-speed visual analysis, interpreting user interfaces and layouts instantly from screenshots.
3.  **Code Architect:** Acts as a lightning-fast pair programmer that refines, debugs, and optimizes code with professional precision.

### ## How I built it
I utilized the **Google GenAI SDK**, specifically optimizing the integration for the Gemini 3 Flash model. I anchored the backend in **Google Cloud Vertex AI** to provide a robust, enterprise-ready foundation. The frontend was designed using **Streamlit**, featuring a custom-designed animated "pulsing" interface for a tactile user experience. To ensure industry-standard protection, I secured the app via **Google Cloud IAM**, utilizing **Service Accounts** for keyless authentication.



### ## Challenges I ran into
Building for the cloud was an exciting engineering journey! I encountered a fascinating "Cryptographic Puzzle" when implementing high-security Service Accounts. Navigating RSA padding requirements taught me the importance of precise configuration. I successfully solved this by engineering a custom **Multi-line Literal String** handler in my secrets management, ensuring my authentication remained rock-solid:

$$\text{Secure RSA String} + \text{Optimized Formatting} = \text{Verified Cloud Access}$$

### ## Accomplishments that I'm proud of
I am incredibly proud of my **"Dual-Mode" engine**, which seamlessly scales from local prototyping using API keys to full-scale **Vertex AI** deployment. I also achieved near-instant multimodal responses, making the interaction between the user and the AI feel truly conversational rather than a series of disjointed prompts.

### ## What I learned
This project was a deep dive into **Enterprise Cloud Architecture**. I mastered the flow of Google Cloud IAM roles and discovered that Gemini 3’s native vision capabilities can interpret complex UI data with far more nuance than traditional libraries. It taught me that the most effective AI agents are built on a foundation of secure, scalable infrastructure.

### ## What's next for Master Agent
The journey doesn't stop here! I am excited to integrate **real-time screen context** for live debugging and explore **Agentic Collaboration**, where multiple instances of Master Agent can coordinate via Google Cloud to solve even larger, more complex engineering challenges.

### ## View the Demo and Proof Videos at:
https://youtu.be/nL8mUalkMWk
https://youtu.be/SXkdnVke4xU

---

## ⚙️ Installation & Setup

You can refer thecommands.txt file of this repository for more detailed Setup instructions.

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/your-username/gemini-master-agent.git](https://github.com/your-username/gemini-master-agent.git)
    cd gemini-master-agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Secrets:**
    Create a `.streamlit/secrets.toml` file with your credentials:
    ```toml
    FREE_GEMINI_API_KEY = "your_key"
    GCP_PROJECT_ID = "your_project_id"
    [gcp_service_account]
    # Paste your service account JSON contents here
    ```

4.  **Launch:**
    ```bash
    streamlit run app.py
    ```
