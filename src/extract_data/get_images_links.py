import urllib3, tqdm, pickle
from bs4 import BeautifulSoup as Soup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://scryfall.com"

def download_content(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
    return response.data.decode('utf-8')


def get_sets():
    content = download_content(base_url + '/sets')

    soup = Soup(content, "html.parser")
    soup = soup.find('table', {'class': 'checklist'})
    tr = soup.find_all('tr')[1:]

    sets = []
    for item in tr:
        href = item.find('a')['href']
        title = item.find_all('a')[1].text.strip().lower()
        if 'token' not in title:
            sets.append(href)

    return sets



def get_images_links(sets):
    all_images = []
    for magic_set in tqdm.tqdm(sets, desc='Find images links'):
        url = base_url+magic_set+'/'
        content = download_content(url)
        soup = Soup(content, "html.parser")
        tmp_all_imgs = soup.find_all('img', {'class': 'card'})
        all_images.extend(tmp_all_imgs)

    all_images_link = [tag['src'] for tag in all_images]

    return all_images_link

sets = get_sets()
print('Number of sets:',len(sets))
all_images_link = get_images_links(sets)
print('Number of images found', len(all_images_link))
print('Saving in data/')
pickle.dump(all_images_link, open('../../data/images_links.pkl', 'wb'))