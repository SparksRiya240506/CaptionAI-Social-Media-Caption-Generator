# CaptionAI: AI Powered Social Media Caption Generator

CaptionAI is a web application designed to help content creators, marketers, and businesses instantly generate optimized social media content packages. By leveraging the low-latency inference capabilities of the **Groq API** and a lightweight **Flask backend**, users can generate platform-specific captions, trending hashtags, and targeted calls-to-action in seconds.

---

## 🚀 Features
* **Multi-Platform Optimization:** Custom tailoring for Instagram, LinkedIn, X (Twitter), and Facebook.
* **Tone Selection:** Choose from different voices like Professional, Excited, Casual, or Funny.
* **Complete Content Packages:** Every request returns a tailored caption, 5-10 relevant hashtags, and an engaging Call-to-Action (CTA).
* **High-Speed AI Inference:** Powered by the `llama3-8b-8192` model via Groq.

---

## 💡 How it Works (Application Workflow)
1. **User Input:** The user enters a topic description, selects a target social media network, and chooses an emotional tone.
2. **Backend Processing:** Flask captures the form input and structures a precise engineering prompt.
3. **AI Generation:** The prompt is sent to the Groq SDK, which utilizes high-speed Llama-3 inference to build structured outputs.
4. **UI Rendering:** The frontend parses the clean response data and beautifully displays the text, hashtags, and CTA separately with a "Copy to Clipboard" button.

---

## 📁 Tech Stack & Prerequisites
* **Backend:** Python, Flask
* **AI Framework:** Groq Cloud Python SDK
* **Environment Management:** python-dotenv
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla UI element)