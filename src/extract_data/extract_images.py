import wget, pickle, tqdm

destination = "../data/cards/"

images_links = pickle.load(open('../data/images_links.pkl', 'rb'))

count = 0

for i, link in enumerate(images_links):
    destination_card = '_'.join(link.split('?')[0].split('/')[-2:])
    print(link)
    try:
        wget.download(link, destination+destination_card)
        count += 1
    except:
        continue
    print(i, '/', len(images_links))

print(count, 'images downloaded')