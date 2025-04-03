import requests
url = "https://telegram.org/support"

data = {
    "problem": "This channel https://t.me/V3NOM_CHEAT is running illegal activities.\n"
    "He takes money from people to teach how to DDoS attacks on BGMI, hacking courses,\n"
    "and attacks on Indian government sites also. He also performs DDoS attacks on Telegram VCs.\n"
    "Now, the channel owner has cleared history, so please review his past week's logs.",
    "full_name": "@venomXcrazy",
    "email": "appyluci@gmail.com",
    "phone_number": "+918504016440",
}
response = requests.post(url, data=data)


if response.status_code == 200:
    print("Report submitted successfully!")
else:
    print(f"Failed to submit report. Status code: {response.status_code}")
# file owner @SOULCRACK
