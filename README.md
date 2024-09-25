# Azure OpenAI GPT-4o Structured Output Demo

[![Watch the demo video](https://img.youtube.com/vi/hjItbqEOO-4/0.jpg)](https://www.youtube.com/watch?v=hjItbqEOO-4)

*Click the image above to watch the demo video.*

## Overview

This sample application demonstrates the **Structured Output** capabilities of GPT-4o (version 2024-08-06) within the Azure OpenAI Service. By leveraging the multi-modal features of GPT-4o, the app allows users to upload an image of a painting or artwork and extracts key information in a structured JSON format that strictly adheres to a provided JSON schema.

## Features

- **Image Upload**: Users can upload an image of a painting or artwork.
- **Image Preview**: Displays a preview of the selected image before processing.
- **Structured Data Extraction**: Utilizes GPT-4o's Structured Output feature to extract information such as title, artist, year, description, and art style.
- **Schema Compliance**: Ensures the JSON output strictly adheres to the predefined schema.
- **Toggle View**: Allows users to switch between a formatted display and the raw JSON output.
- **Simple UI**: A simple and modern Flask interface styled with CSS and utilizing system fonts.

## Prerequisites

- **Azure OpenAI Service**: Access to the Azure OpenAI Service with the GPT-4o model (version 2024-08-06 or later) deployed.
- **Python 3.x**: Ensure Python 3.x is installed on your system.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Required Packages**

   Install the necessary Python packages using pip:

   ```bash
   pip install flask openai python-dotenv
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the project root directory and add your Azure OpenAI credentials:

   ```env
   AZURE_OPENAI_API_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_API_KEY=your_azure_openai_api_key
   AZURE_OPENAI_API_MODEL=your_model_deployment_name
   AZURE_OPENAI_API_VERSION=2024-08-01-preview
   ```

   - Replace `your_azure_openai_endpoint` with your Azure OpenAI endpoint (e.g., `https://your-resource-name.openai.azure.com/`).
   - Replace `your_azure_openai_api_key` with your Azure OpenAI API key.
   - Replace `your_model_deployment_name` with the deployment name of your GPT-4o model.
   - Ensure you're using the correct API version that supports structured outputs.

## Usage

1. **Run the Flask App**

   In your terminal, navigate to the project directory and run:

   ```bash
   python app.py
   ```

2. **Access the Application**

   Open your web browser and go to `http://localhost:5000`.

3. **Upload an Image**

   - Click on "Choose File" and select an image of a painting or artwork.
   - A preview of the selected image will appear.
   - Click on "Upload and Process" to submit the image.

4. **View Extracted Information**

   - The app will display the extracted information in a formatted view.
   - Use the "View JSON" button to toggle to the JSON representation of the data.

## Directory Structure

```
your-project/
├── app.py
├── .env
├── templates/
    ├── index.html
    └── result.html
```

- **app.py**: The main Flask application script.
- **.env**: Environment variables containing Azure OpenAI credentials.
- **templates/**: Folder containing HTML templates.
  - **index.html**: The homepage template where users upload images.
  - **result.html**: The results page displaying extracted information.

## How It Works

This application utilizes the **Structured Output** feature of GPT-4o (2024-08-06) within the Azure OpenAI Service. By providing a JSON schema, GPT-4o is instructed to output data that strictly adheres to the defined structure.

### Key Components

- **Multi-modal input**: The app can send both text and image inputs to GPT-4o (although we only use the image capabilities in this demo).
- **JSON Schema**: A predefined schema specifies the expected structure of the output.
- **Strict Adherence**: GPT-4o ensures the output complies with the provided schema, making the data reliable for further processing.

### Sample JSON Schema

```json
{
  "name": "structured_output",
  "schema": {
    "type": "object",
    "properties": {
      "title": {"type": "string"},
      "artist": {"type": "string"},
      "year": {"type": "string"},
      "short_description": {"type": "string"},
      "art_style": {"type": "string"}
    },
    "required": ["title", "artist", "year", "short_description", "art_style"]
  }
}
```

## Notes

- **Azure OpenAI Access**: Ensure you have deployed an Azure OpenAI Service instance, along with GPT-4o.
- **Model Version**: The app requires GPT-4o version 2024-08-06 or later to support Structured Outputs.
- **API Version**: The API must be 2024-08-01-preview or later to support Structured Outputs.
- **Error Handling**: Basic error handling is included. For production use, consider implementing more robust error handling and input validation.
- **Security**: Keep your API keys secure and do not commit the `.env` file to version control.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

---

*This sample application demonstrates the power of GPT-4o's Structured Output capabilities within the Azure OpenAI Service, enabling strict adherence to provided JSON schemas for reliable and structured data extraction.*

---
