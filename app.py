import sys

from slack_api import WebClient


def main():
    print("Hello")
    client = WebClient()
    api_response = client.api_test()
    print(api_response)


if __name__ == "__main__":
    main()
