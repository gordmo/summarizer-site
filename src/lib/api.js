// src/lib/api.js
async function summarizeText(text) {
    const response = await fetch(url = "http://localhost:5000/summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });
  
    if (response.ok) {
      const data = await response.json();
      return data.summary;
    } else {
      throw new Error("Error summarizing text");
    }
  }
  
  export { summarizeText };