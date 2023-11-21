import wikipediaapi
import wikipedia
import requests

def wiki():
    
    url = 'https://en.wikipedia.org/wiki/Cricket'
    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}

    response = requests.get(url, headers=headers)
    
    page_title = input("Enter the page title whose wikipedia content you wish to read: ")
    
    # Fetch the page

    # Print the page summary
    print("Page summary:")
    print(wikipedia.summary(page_title)[:200])  # Displaying only the first 200 characters for brevity

    # Print the full page text
    #print("\nFull page text:")
    print((wikipedia.page(page_title)).content)


if __name__ == "__main__":
    wiki()
