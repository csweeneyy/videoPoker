from images import Image



def negative():
    suits = ["clubs", "diamonds", "hearts", "spades"]
    ranks = ["ace",2,3,4,5,6,7,8,9,10,"jack","queen","king"]
    for x in suits:
        for y in ranks:
            i = Image(f"card_images/{x}_{y}.gif")
            for a in range(i.getHeight()):
                for b in range(i.getWidth()):
                    red, green, blue = i.getPixel(b, a)
                    red = 255 - red
                    green = 255 - green
                    blue = 255 - blue
                    i.setPixel(b, a, (red, green, blue))
            i.save(filename = f"inverted_card_images/{x}_{y}.gif")


if __name__ == '__main__':
    negative()