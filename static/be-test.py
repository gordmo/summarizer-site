import requests

url = "http://localhost:5000/summarize"
data = {"text": "The World Health Organization (WHO) has declared COVID-19 a pandemic. This virus, which emerged in Wuhan, China in December 2019, has rapidly spread across the globe, causing widespread illness, death, and societal disruption. The pandemic has highlighted the importance of public health interventions such as social distancing, mask-wearing, and hand hygiene to slow the spread of the virus. In addition, the development of vaccines has been a critical tool in combating the pandemic. However, vaccine distribution has been uneven across countries, and some communities have been hesitant to receive the vaccine due to misinformation and mistrust. Despite these challenges, the world has made significant progress in controlling the pandemic through a combination of public health measures and vaccination campaigns. Moving forward, it will be important to continue these efforts and to address the systemic issues that have contributed to the pandemic's disproportionate impact on marginalized communities.", "percentage": 0.5}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())

if response.status_code == 200:
    print("Summary:", response.json()["summary"])
else:
    print("Error:", response.json()["error"])