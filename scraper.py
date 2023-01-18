import time

import discord
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class Info:
    def __init__(self, name, price, img, link):
        self.name = name
        self.price = price
        self.img = img
        self.link = link

    def __str__(self):
        return f"{self.name}, {self.price}"

    def __repr__(self):
        return f"{self.name}, {self.price}"


class Options:
    def __init__(self, item, location, distance):
        self.item = item
        self.location = location
        self.distance = distance

    def __str__(self):
        return f"{self.item}, {self.location}"

    def __repr__(self):
        return f"{self.item}, {self.location}"


def get_options(text: str):
    options = text.split(" ")
    options.pop(0)

    item = ""
    location = ""
    distance = ""

    print(options)

    for option in options:
        key, value = option.split("=")

        match key:
            case "item":
                item = value
            case "location":
                location = value
            case "distance":
                distance = value

    return Options(item, location, distance)


async def scrape(message: discord.Message):
    if len(message.content.split()) <= 1:
        return await message.channel.send('Please pass a parameter')

    options = get_options(message.content)

    driver.get(f"https://www.facebook.com/marketplace/kingston-ca/search/?query={options.item}")

    # wait for the page to load
    time.sleep(2)

    # click on div with class "x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz x1xmf6yo"
    driver.find_element(By.XPATH,
                        '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz x1xmf6yo"]') \
        .click()

    time.sleep(2)

    text_field = driver.find_element(By.XPATH,
                                     "//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4']")

    # clear the text field
    text_field.click()
    text_field.send_keys(Keys.CONTROL + "a")
    text_field.send_keys(Keys.DELETE)
    text_field.send_keys(options.location)

    time.sleep(2)


    option_list = driver.find_elements(By.XPATH,
                                       "//div[@class='x6s0dn4 x1ypdohk x78zum5 x6ikm8r x10wlt62 x1n2onr6 xi2jdih x1lq5wgf xgqcy7u x30kzoy x9jhf4c xdj266r xat24cr x1y1aw1k x1sxyh0 xwib8y2 xurb0ha']")

    # click on the first option
    option_list[0].click()

    time.sleep(2)

    driver.find_element(By.XPATH,
                         "//div[@class='xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 x1jchvi3 x1fcty0u x132q4wb xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x9desvi x1pi30zi x1a8lsjc x1n2onr6 x16tdsg8 xh8yej3 x1ja2u2z xzsf02u x1swvt13']")\
        .click()

    time.sleep(2)

    distsance_list = driver.find_elements(By.XPATH,
                                          "//div[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xjyslct x9f619 x1ypdohk x78zum5 x1q0g3np x2lah0s x13mpval x1w4qvff xdj266r xat24cr xz9dl7a x1sxyh0 xsag5q8 xurb0ha x1n2onr6 x16tdsg8 x1ja2u2z']")
    if options.distance == "1":
        distsance_list[0].click()
    elif options.distance == "2":
        distsance_list[1].click()
    elif options.distance == "5":
        distsance_list[2].click()
    elif options.distance == "10":
        distsance_list[3].click()
    elif options.distance == "20":
        distsance_list[4].click()
    elif options.distance == "40":
        distsance_list[5].click()
    elif options.distance == "60":
        distsance_list[6].click()
    elif options.distance == "65":
        distsance_list[7].click()
    elif options.distance == "80":
        distsance_list[8].click()
    elif options.distance == "100":
        distsance_list[9].click()
    elif options.distance == "250":
        distsance_list[10].click()
    elif options.distance == "500":
        distsance_list[11].click()
    else:
        distsance_list[0].click()

    time.sleep(2)

    # hit button with Apply text
    driver.find_element(By.XPATH,
                        "//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli xsyo7zv x16hj40l x10b6aqq x1yrsyyn']") \
        .click()


    # get all divs with x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e xnpuxes x291uyu x1uepa24 x1iorvi4 xjkvuk6
    # add them to a list
    items: list = driver.find_elements(By.XPATH,
                                       '//div[@class="x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e xnpuxes x291uyu x1uepa24 x1iorvi4 xjkvuk6"]')

    cleaned_data: list(Info) = []

    for item in items:
        try:
            # price is span with x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u
            price = item.find_element(By.XPATH,
                                      './/span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u"]')

            # name is span with x1lliihq x6ikm8r x10wlt62 x1n2onr6
            name = item.find_element(By.XPATH, './/span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6"]')

            # img is img with xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3
            img = item.find_element(By.XPATH, './/img[@class="xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3"]')

            link = item.find_element(By.XPATH, './/a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1lku1pv"]')


            # create an object of Info class
            info = Info(name.text, price.text, img.get_attribute('src'), link.get_attribute('href'))

            # add the object to the list
            cleaned_data.append(info)
        except:
            pass

    # account for price starting with C$
    cleaned_data = [item for item in cleaned_data if item.price.startswith('C$')]

    # sort the list by price but convert the price to a float also remove all commas
    sorted_data = sorted(cleaned_data, key=lambda x: float(x.price[2:].replace(',', '')))

    # send the list to the channel as formatted string with each item on a new line
    for item in sorted_data[:3]:
        await message.channel.send(f"{item.name} - {item.price} - {item.img} - {item.link}")

    return await message.channel.send('Done')
