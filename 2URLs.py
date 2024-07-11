import requests
from time import sleep


def download_urls(urls):
    max_retries = 3
    for url in urls:
        retries = 0
        while retries < max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an Exception for Bad Responses
                print(f"Content from {url}:")
                print(response.text)
                break  # Break the Retry Loop if Successful
            except requests.exceptions.RequestException as e:
                retries += 1
                print(f"Error downloading {url}: {e}")
                if retries < max_retries:
                    print(f"Retrying ({retries}/{max_retries})")
                    sleep(1)  # Wait for 1 Second Before Retrying
                else:
                    print(f"Failed to download {url} after {max_retries} retries.")


def main():
    urls = []
    while True:
        url = input("Enter a URL (or 'Done'/'done' to finish): ")
        if url.lower() == "done":
            break
        urls.append(url)

    if urls:
        download_urls(urls)  # Call the Function
    else:
        print("No URLs provided.")  # Inform if No URLs were Entered


if __name__ == "__main__":
    main()