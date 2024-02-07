from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post_request():
    if request.method == 'POST':
        data = request.get_json()
        # Do something with the data
        return 'Received POST request with data: {}'.format(data)
    else:
        return 'Invalid request method'

if __name__ == '__main__':
    app.run()
