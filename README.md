# MAS
# 📊 Market Analysis Chatbot  

This is an AI-powered chatbot that helps users analyze market conditions for startups. It gathers user inputs and retrieves real-time market data using a search engine API. The chatbot provides market size, marketing insights, SWOT analysis, competitor analysis, and customer segmentation.  

## Features  

- Interactive chatbot that guides users through business analysis questions.  
- Uses **Gradio** for a user-friendly chat interface.  
- Integrates **Hugging Face LLM API** for intelligent responses.  
- Retrieves real-time market insights using **Bing Search API**.  
- Provides **structured market analysis**, including SWOT and competitor analysis.  

## Project Structure  

```
/market_analysis_chatbot
│── app.py                                   # Main entry point with Gradio interface
│── config.py                                # Configuration and environment variables
│── search.py                                # Functions related to Bing search
│── helper.py                                # Utility functions like token counting and limiting history
│── model.py                                 # Functions interacting with the LLM API
│── requirements.txt                         # List of dependencies
│── .env                                     # Our API keys 
│── README.md                                # Project documentation
│── AI MAS - Project Report.pdf              # Project Development Report
```

## Installation  

### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/market-analysis-chatbot.git
cd market-analysis-chatbot
```

### **2. Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Set Up API Keys**  
Create a `.env` file in the project directory and add your API keys:  

```
HF_KEY=your_huggingface_api_key
BING_API_KEY=your_bing_api_key
```

## Running the Application  

Run the chatbot using:
```bash
gradio app.py
```
or using: 
```bash
python app.py
```

This will start a Gradio web interface where users can interact with the chatbot.  

## Future Improvements  

- Add support for multiple languages.  
- Improve the accuracy of search results.
- Add a database to save past analyses.

## 📄 Project Report

The full project report is included in this repository.  
You can find it in the file: `AI MAS - Project Report.pdf`
OR you can view the full project report [here](http://dx.doi.org/10.13140/RG.2.2.36344.15361).


This project is a simple, interactive, and practical tool for anyone looking to start a business.
