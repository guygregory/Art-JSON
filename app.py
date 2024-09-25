import os
import base64
import json
from dotenv import load_dotenv
from flask import Flask, request, render_template
from openai import AzureOpenAI

load_dotenv()

app = Flask(__name__)

# Azure OpenAI configuration (unchanged)
endpoint = os.environ["AZURE_OPENAI_API_ENDPOINT"]
deployment = os.environ["AZURE_OPENAI_API_MODEL"]
key = os.environ["AZURE_OPENAI_API_KEY"]
version = os.environ["AZURE_OPENAI_API_VERSION"]

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=key,
    api_version=version,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    image_file = request.files['image']
    if image_file.filename == '':
        return 'No image selected', 400

    # Read the image file and encode it to base64
    image_bytes = image_file.read()
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    # Prepare the prompt and send the request to Azure OpenAI
    try:
        completion = client.chat.completions.create(
            model=deployment,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract the key information from this painting."},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                            "detail": "high"
                        },
                    ]
                }
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "structured_output",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "artist": {"type": "string"},
                            "year": {"type": "string"},
                            "short_description": {"type": "string"},
                            "art_style": {"type": "string"},
                        },
                        "required": ["title", "artist", "year", "short_description", "art_style"],
                    }
                }
            }
        )

        completion_json = completion.to_json()
        completion_text = json.loads(completion_json)
        content = completion_text['choices'][0]['message']['content']
        result = json.loads(content)

        # Create a JSON string with indentation
        result_json = json.dumps(result, indent=4)

        # Pass the base64 image and JSON string to the template
        return render_template('result.html', result=result, result_json=result_json, image_data=base64_image)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
