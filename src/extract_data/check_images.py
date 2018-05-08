import imghdr, os, shutil
from PIL import Image
import tqdm
import pickle

before_8ed = pickle.load(open('../../data/sets_before_8ed.pkl', 'rb'))

print('Il y a ', len(os.listdir('../../data/cards')), 'images')
error = 0
for name in tqdm.tqdm(os.listdir('../../data/cards')):
    if 'jpeg' != imghdr.what('../../data/cards/'+name):
        error += 1
        os.remove('../../data/cards/'+name)
        continue

    try:
        image = Image.open('../../data/cards/'+name)
    except:
        error += 1
        continue

    if image.mode != 'RGB':
        error += 1
        os.remove('../../data/cards/' + name)
        continue

    if '(' in name:
        error += 1
        os.remove('../../data/cards/' + name)
        continue

    set = name.split('_')[0]

    if set in before_8ed:
        error += 1
        os.remove('../../data/cards/' + name)
        continue

    if ' ' in name:
        error += 1
        new_name = name.replace(' ', '_')
        os.rename('../../data/cards/'+name, '../../data/cards/'+new_name)


    #try:
    #    image.save('../../data/cards/'+name)
    #except:
    #    os.remove('../../data/cards/' + name)





print(error)
#imghdr.what('/tmp/bass')