import fireworks.client
import base64

fireworks.client.api_key = "fw_3Zj2zWvgHnju9iLwYGsFGuvb"

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# The path to your image
image_path = "mounts.jpeg"

# The base64 string of the image
image_base64 = encode_image(image_path)

response = fireworks.client.ChatCompletion.create(
  model = "accounts/fireworks/models/phi-3-vision-128k-instruct",
  messages = [{
    "role": "user",
    "content": [{
      "type": "text",
      "text": "Can you describe this image?",
    }, {
      "type": "image_url",
      "image_url": {
        "url": f"data:image/jpeg;base64,{image_base64}"
      },
    }, ],
  }],
)
print(response.choices[0].message.content)
