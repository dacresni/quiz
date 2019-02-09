import json, requests, unittest 
from itertools import islice
from flask import Flask, jsonify
DOMAIN= "https://api.github.com"
app = Flask(__name__)
@app.route("/<github_id>/")
def followers(github_id):
    follower_ids = []
    """Write an API endpoint that accepts a GitHub ID and returns Follower GitHub ID’s (up to 5 Followers total) associated with the passed in GitHub ID.  Retrieve data up to 3 levels deep, repeating the process of retrieving Followers (up to 5 Followers total) for each Follower found.  Data should be returned in JSON format """
    def pull(id,num):
        if num <= 0:
          return jsonify(follower_ids)
        num -= 1
        followers = requests.get(DOMAIN+"/users/{0}/followers".format(github_id)).json()
        print(followers)
        f = islice(followers,5)
        for user in f : 
          id = user["login"]
          follower_ids.append(id)
          pull(id,num)
    pull(id,3)
    
def bounus(github_id):
    """Write an API endpoint that accepts a GitHub ID and retrieves the Repository names (up to 3 Repositories total) associated with the passed in GitHub ID, along with the Stargazer GitHub ID’s (up to 3 Stargazers total) associated with each Repository.  Retrieve data up to 3 levels deep, repeating the process of retrieving the associated Repositories (up to 3 Repositories total) for each Stargazer (up to 3 Stargazers total) found.  Data should be returned in JSON format.  """
    pass

