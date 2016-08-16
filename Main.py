from bs4 import BeautifulSoup
with open ('./index.html','r')as websitedata:
    Soup=BeautifulSoup(websitedata,'lxml')

titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')

for title,image,review,price,star in zip(titles,images,reviews,prices,stars):
    data={
        'title': title.get_text(),
        'review':review.get_text(),
        'price':review.get_text(),
        'image':image.get('src'),
        'star':len(star.find_all("span", class_='glyphicon glyphicon-star'))
    }
    print(data)
    
    
    
    # The consequence shows as below:
    {'review': '65 reviews', 'image': 'img/pic_0000_073a9256d9624c92a05dc680fc28865f.jpg', 'title': 'EarPod', 'star': 5, 'price': '65 reviews'}
{'review': '12 reviews', 'image': 'img/pic_0005_828148335519990171_c234285520ff.jpg', 'title': 'New Pocket', 'star': 4, 'price': '12 reviews'}
{'review': '31 reviews', 'image': 'img/pic_0006_949802399717918904_339a16e02268.jpg', 'title': 'New sunglasses', 'star': 4, 'price': '31 reviews'}
{'review': '6 reviews', 'image': 'img/pic_0008_975641865984412951_ade7a767cfc8.jpg', 'title': 'Art Cup', 'star': 3, 'price': '6 reviews'}
{'review': '18 reviews', 'image': 'img/pic_0001_160243060888837960_1c3bcd26f5fe.jpg', 'title': 'iphone gamepad', 'star': 4, 'price': '18 reviews'}
{'review': '18 reviews', 'image': 'img/pic_0002_556261037783915561_bf22b24b9e4e.jpg', 'title': 'Best Bed', 'star': 4, 'price': '18 reviews'}
{'review': '35 reviews', 'image': 'img/pic_0011_1032030741401174813_4e43d182fce7.jpg', 'title': 'iWatch', 'star': 4, 'price': '35 reviews'}
{'review': '8 reviews', 'image': 'img/pic_0010_1027323963916688311_09cc2d7648d9.jpg', 'title': 'Park tickets', 'star': 4, 'price': '8 reviews'}
