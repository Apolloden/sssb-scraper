from bs4 import BeautifulSoup
import requests

url = "https://sssb.se/widgets/?callback=jQuery17203404817715808992_1703443444188&widgets%5B%5D=alert&widgets%5B%5D=objektsummering%40lagenheter&widgets%5B%5D=objektfilter%40lagenheter&widgets%5B%5D=objektsortering%40lagenheter&widgets%5B%5D=objektlistabilder%40lagenheter&widgets%5B%5D=pagineringantal%40lagenheter&widgets%5B%5D=paginering%40lagenheter&widgets%5B%5D=pagineringgofirst%40lagenheter&widgets%5B%5D=pagineringgonew%40lagenheter&widgets%5B%5D=pagineringlista%40lagenheter&widgets%5B%5D=pagineringgoold%40lagenheter&widgets%5B%5D=pagineringgolast%40lagenheter"

# Make a request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the target <h3> element
    targets_h3 = soup.find_all("h3")

    for target_h3 in targets_h3:
        print(target_h3.text.strip())
    if target_h3:
        # Print the text content of the target <h3> element
        print("Text content of <h3>:", target_h3.text.strip())

        # Navigate to the parent element
        parent_div = target_h3.parent
        print("Parent <div> text content:", parent_div.text.strip())

        # Navigate to the next sibling element
        next_sibling_p = target_h3.find_next_sibling("p")
        if next_sibling_p:
            print("Next sibling <p> text content:", next_sibling_p.text.strip())
        else:
            print("No next sibling <p> found.")

    else:
        print("Target <h3> not found.")
else:
    print(f"Error: {response.status_code}")