#!/usr/bin/env python3
"""
Web Hosting Panel Testing Tool
Start this file to run the testing panel
"""

from flask import Flask, jsonify, render_template_string, request
import json
import sys
from main import run_all_tests, test_system_resources, test_server_status

app = Flask(__name__)

# HTML Template for Web Interface
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Web Hosting Panel Tester</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        h1 {
            color: #667eea;
            text-align: center;
        }
        .test-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .test-card {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 15px;
            border-left: 4px solid #667eea;
        }
        .test-card h3 {
            margin-top: 0;
            color: #667eea;
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin: 10px 5px;
        }
        button:hover {
            background: #764ba2;
        }
        .result {
            background: #e9ecef;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
            font-family: monospace;
            font-size: 12px;
            overflow-x: auto;
        }
        .success {
            color: green;
            font-weight: bold;
        }
        .error {
            color: red;
            font-weight: bold;
        }
        .status {
            text-align: center;
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }
        .status.online {
            background: #d4edda;
            color: #155724;
        }
        .status.offline {
            background: #f8d7da;
            color: #721c24;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌐 Web Hosting Panel Testing Tool</h1>
        
        <div style="text-align: center;">
            <button onclick="runAllTests()">Run All Tests</button>
            <button onclick="runSystemTest()">System Resources</button>
            <button onclick="runServerTest()">Server Status</button>
        </div>
        
        <div id="results" class="test-grid">
            <div class="test-card">
                <h3>📊 Test Results</h3>
                <div id="result-content">Click a button to start testing...</div>
            </div>
        </div>
    </div>

    <script>
        async function runAllTests() {
            const response = await fetch('/api/run_all_tests');
            const data = await response.json();
            displayResults(data);
        }
        
        async function runSystemTest() {
            const response = await fetch('/api/system_resources');
            const data = await response.json();
            displayResults({system_resources: data});
        }
        
        async function runServerTest() {
            const response = await fetch('/api/server_status');
            const data = await response.json();
            displayResults({server_status: data});
        }
        
        function displayResults(data) {
            const resultDiv = document.getElementById('result-content');
            resultDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    """Home page - Testing Panel Interface"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/run_all_tests')
def api_run_all_tests():
    """Run all tests and return results"""
    results = run_all_tests()
    return jsonify(results)

@app.route('/api/system_resources')
def api_system_resources():
    """Get system resources only"""
    resources = test_system_resources()
    return jsonify(resources)

@app.route('/api/server_status')
def api_server_status():
    """Get server status only"""
    status = test_server_status()
    return jsonify(status)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Testing panel is running'})

def main():
    """Start the web hosting panel testing interface"""
    print("=" * 50)
    print("🚀 Web Hosting Panel Testing Tool")
    print("=" * 50)
    print("📋 Starting web interface...")
    print("🌐 Access the testing panel at: http://localhost:5000")
    print("🔧 API endpoints:")
    print("   - /api/run_all_tests - Run all tests")
    print("   - /api/system_resources - Check system resources")
    print("   - /api/server_status - Check server status")
    print("   - /health - Health check")
    print("=" * 50)
    print("⚠️  Press CTRL+C to stop the server")
    print("=" * 50)
    
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down testing panel...")
        return 0
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
