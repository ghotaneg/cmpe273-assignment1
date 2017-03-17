from flask import Flask
from github import Github
import sys

app = Flask(__name__)

# Store the github repo path provided in the docker run command. 
input_url = sys.argv[1]

# Extract the repo name from the input url.
input_repo_name = input_url.replace("https://github.com/","")

@app.route("/")
def home_page():
    return "Hello from Dockerized Flask App!!"

# Function to read the contents from any config file available in the git hub repo path provided.
@app.route("/v1/<config_filename>")
def read_config(config_filename):

    # Create a new object of Github class.
    g = Github()

    # Fetch the repository using get_repo() function.
    repository = g.get_repo(input_repo_name)

    # Fetch the contents of the filename typed in the URL which is stored in the config_filename variable.
    file = repository.get_contents(config_filename)

    # Return the contents of the config file read from the github repository.
    return file.decoded_content

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
