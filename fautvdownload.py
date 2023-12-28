import requests
from dotenv import load_dotenv
import argparse
import subprocess
import os
import re


def get_download_url(url, cookies):
    # Make a GET request (you can also use POST, PUT, DELETE, etc.)
    response = requests.get(url, cookies=cookies)

    # Regular expression pattern
    pattern = r'"https?://[^"]*playlist\.m3u8[^"]*"'

    # Find match 
    match = re.search(pattern, response.text) 
    if match is None:
        print(f'No match found for {url}')  
        print(response.text)
        return None
    # Remove the double quotes
    match = match.replace('"', '')
    # Return the match
    return match

def download_file(uri, filename):
    # use ffmpeg to download the file
    command = [
        'ffmpeg',
        '-i',
        uri,
        '-c', 'copy',
        '-bsf:a', 'aac_adtstoasc',
        filename
    ]

    subprocess.run(command)


def get_cookies():
    # Get the cookies from the .env file
    load_dotenv()
    cookies = {
        #'csrf_cookie_name': os.getenv('CSRF_COOKIE_NAME'),
        'session_ci': os.getenv('SESSION_CI'),
        #'SimpleSAMLSessionID': os.getenv('SIMPLE_SAML_SESSION_ID'),
    }
    return cookies


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ids', help='The ids of the videos to download', nargs='+')
    parser.add_argument('--output', help='The output file names', nargs='+')
    args = parser.parse_args()

    if len(args.ids) != len(args.output):
        print('The number of ids and output file names must be the same')
        return

    urls = [f'https://www.fau.tv/clip/id/{id}' for id in args.ids]
    # Get cookies from .env file
    cookies = get_cookies()
    print(cookies)
    # Get the download URL
    download_urls = [get_download_url(url, cookies) for url in urls]
    print(download_urls)

    # Download the file
    for i, download_url in enumerate(download_urls):
        if download_url is not None:
            download_file(download_url, args.output[i])


if __name__ == '__main__':
    main()
