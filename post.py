import requests

class Post:
    def __init__(self, id):
        self.id = id
        self.blog_post = self.blog_data()
        if self.id < len(self.blog_post):
            self.title = self.blog_post[self.id]["title"]
            self.body = self.blog_post[self.id]["body"]
            self.subtitle = self.blog_post[self.id]["subtitle"]
        else:
            self.title = None
            self.body = None
            self.subtitle = None
        
    def blog_data(self):
        URL = "https://api.npoint.io/c2deeeed9f0f7f072d17"

        try:
            response = requests.get(URL)
            # Check if the response contains valid JSON
            if response.status_code == 200:
                try:
                    data = response.json()
                    self.blog_post = data
                    #print(self.blog_post)
                    return self.blog_post
                except requests.exceptions.JSONDecodeError:
                    print("Error: The response was not valid JSON.")
                    print("Raw response content:", response.text)
            else:
                print(f"Request failed with status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")