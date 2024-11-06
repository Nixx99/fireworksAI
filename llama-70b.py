from fireworks.client import Fireworks

client = Fireworks(api_key="fw_3Zj2zWvgHnju9iLwYGsFGuvb")
prompt = "provide one riddle with its answer."
response = client.chat.completions.create(
model="accounts/fireworks/models/llama-v3p1-70b-instruct",
messages=[{
   "role": "user",
   "content": prompt,
}],
)

print(response.choices[0].message.content)
