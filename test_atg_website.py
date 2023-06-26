import unittest
import requests

class ATGWorldWebsiteTest(unittest.TestCase):

    def test_website_loading(self):
        url = "https://www.atg.world/"
        print("Input target URL for unit testing is provided: " + str(url))

        try:
            # Send an HTTP GET request to the website
            response = requests.get(url)
            print("GET request to the target URL is initiated..")

            # Check the response status code
            print("Fetching the results..")
            if response.status_code == 200:
                # Print statements for logging
                print("Website loaded successfully!")
                print("Status Code: " + str(response.status_code))
            else:
                print("Website has some issue")
                print("Status Code: " + str(response.status_code))

        except requests.exceptions.RequestException as e:
            print("GET request to the target URL is initiated..")
            print("Fetching the results..")
            print("An error occurred while making the request:")
            print(str(e))
            #hlo

if __name__ == "__main__":
    unittest.main()
