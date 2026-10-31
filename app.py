from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def analyze_information(query, context_text=""):
    summary = f"Query '{query}' ke liye multi-source information analyze ki gayi hai."
    
    conflicts = [
        "Eligibility criteria alag-alag portals par alag hain (e.g., Annual Income limit ₹2 Lakh vs ₹2.5 Lakh).",
        "Application deadline official notification mein 15 Nov hai, jabki third-party sites par 30 Nov likha hai."
    ]
    
    missing_gaps = [
        "Income certificate state-level chahiye ya central-level, yeh clarify nahi hai.",
        "Renewal applicants ke liye minimum attendance percentage specification missing hai."
    ]
    
    verification_checklist = [
        "Official portal se latest notification PDF download karke cross-check karein.",
        "Authority helpline number par call karke income ceiling double-check karein.",
        "Required documents (Aadhaar link, Marksheet) ki issuing date verify karein."
    ]
    
    return {
        "summary": summary,
        "conflicts": conflicts,
        "missing_gaps": missing_gaps,
        "checklist": verification_checklist,
        "confidence_score": "72% (High Uncertainty Detected)"
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    query = data.get('query', '')
    sources = data.get('sources', '')
    
    if not query:
        return jsonify({"error": "Query enter karna zaroori hai"}), 400
        
    result = analyze_information(query, sources)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)