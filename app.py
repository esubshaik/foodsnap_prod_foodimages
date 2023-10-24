import os
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route to handle image requests
@app.route('/get_images', methods=['GET'])
def get_images():
    food_name = request.args.get('food_name')
    images = []
    food_folder = os.path.join('myfoodimages', food_name)  # Replace with your data folder path

    if not os.path.exists(food_folder):
        return jsonify({'error': 'Food not found'})

    for filename in os.listdir(food_folder):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            with open(os.path.join(food_folder, filename), 'rb') as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
                images.append(image_data)

    if not images:
        return jsonify({'error': 'No images found'})

    return jsonify({'images': images})

if __name__ == '__main__':
    app.run()
