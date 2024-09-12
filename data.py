import requests
import csv
from keys import api_key

def fetch_books(query,limit):
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{query}&maxResults={limit}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def get_links(volume_info):
    links = {}
    if 'previewLink' in volume_info:
        links['preview'] = volume_info['previewLink']
    return links

def get_genre(query):
    limit = 20
    books_data = fetch_books(query,limit)
    get_details(books_data)

def get_details(books_data):
    filename = "data.csv"
    f = open(filename, "w+")
    f.close()
    if books_data:
        for book in books_data.get("items", []):
            volume_info = book.get("volumeInfo", {})
            title = volume_info.get("title", "Unknown Title")
            authors = ", ".join(volume_info.get("authors", ["Unknown Author"]))
            description = volume_info.get("description", "No description available")
            original_release = volume_info.get("publishedDate", "Unknown Date")
            language = volume_info.get("language", "Unknown Language")

            links = get_links(volume_info)
            if 'preview' in links:
                 preview=links['preview']
            
            with open('data.csv', 'a') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow([title, authors, description, original_release,language,preview])
            
            # print(f"TITLE: {title}")
            # print(f"AUTHORS: {authors}")
            # print(f"DESCRIPTION: {description}")
            # print(f"LANGUAGE: {language}")
            # print(f"ORIGINAL RELEASE DATE: {original_release}")
            # links = get_links(volume_info)
            # if 'preview' in links:
            #     preview=links['preview']
            #     print(f"PREVIEW: {preview}")
            # preview_links.update({title:preview})
            # print()
            # print()

def fetch_preview_link(name):
    url = f"https://www.googleapis.com/books/v1/volumes?q={name}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def preview_links(name):
    data = fetch_preview_link(name)
    if data:
        for info in data.get("items", []):
            volume_info = info.get("volumeInfo", {})
            links = get_links(volume_info)
            if 'preview' in links:
                link = links['preview']
                break
            else:
                link=''
    return link

