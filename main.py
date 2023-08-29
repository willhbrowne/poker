'''
Created on Jan 18, 2023

@author: willbrowne

Main Class
Attributes: none
List Methods: .index()
'''

from deck import Deck
from hand import Hand
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


if __name__ == '__main__':
    
    for x in range (100):
        hand1 = Hand()
        hand2 = Hand()
        hand3 = Hand()
        hand4 = Hand()
        
        poker_game = (hand1, hand2, hand3, hand4)
        
        deck = Deck()
        deck.shuffle()
        
        for i in range(len(poker_game) * 5):
            poker_game[i%len(poker_game)].add_card(deck.deal_card())
    
        
        winner = Hand()
        winner_true = 0
        for i in range(len(poker_game)):
            wins = 0
            for y in range(len(poker_game)):
                if not i == y:
                    if (poker_game[i].compare(poker_game[y]) == 1):
                        wins += 1
                if wins == len(poker_game) - 1:
                    winner_true = 1
                    winner = poker_game[i]
                    break
            
         
        def make_row(im1, im2, im3, im4, im5):
            row = Image.new('RGB', (im1.width * 7, im1.height))
            row.paste(im1, (0,0))
            row.paste(im2, (im1.width, 0))
            row.paste(im3,(im1.width + im2.width, 0))
            row.paste(im4, (im1.width + im2.width + im3.width, 0))
            row.paste(im5, (im1.width + im2.width + im3.width + im4.width, 0))
            return row
        
        def make_column(im1, im2, im3, im4):
            column = Image.new('RGB', (im1.width, im1.height * 4))
            column.paste(im1, (0,0))
            column.paste(im2, (0, im1.height))
            column.paste(im3, (0, im1.height + im2.height))
            column.paste(im4, (0, im1.height + im2.height + im3.height))
            return column
        
        hand_one = make_row(Image.open("cards/" + poker_game[0].get_hand()[0].image_file_name()),
                        Image.open("cards/" + poker_game[0].get_hand()[1].image_file_name()),
                        Image.open("cards/" + poker_game[0].get_hand()[2].image_file_name()),
                        Image.open("cards/" + poker_game[0].get_hand()[3].image_file_name()),
                        Image.open("cards/" + poker_game[0].get_hand()[4].image_file_name()))
        
        hand_two = make_row(Image.open("cards/" + poker_game[1].get_hand()[0].image_file_name()),
                        Image.open("cards/" + poker_game[1].get_hand()[1].image_file_name()),
                        Image.open("cards/" + poker_game[1].get_hand()[2].image_file_name()),
                        Image.open("cards/" + poker_game[1].get_hand()[3].image_file_name()),
                        Image.open("cards/" + poker_game[1].get_hand()[4].image_file_name()))
        
        hand_three = make_row(Image.open("cards/" + poker_game[2].get_hand()[0].image_file_name()),
                        Image.open("cards/" + poker_game[2].get_hand()[1].image_file_name()),
                        Image.open("cards/" + poker_game[2].get_hand()[2].image_file_name()),
                        Image.open("cards/" + poker_game[2].get_hand()[3].image_file_name()),
                        Image.open("cards/" + poker_game[2].get_hand()[4].image_file_name()))
        
        hand_four = make_row(Image.open("cards/" + poker_game[3].get_hand()[0].image_file_name()),
                        Image.open("cards/" + poker_game[3].get_hand()[1].image_file_name()),
                        Image.open("cards/" + poker_game[3].get_hand()[2].image_file_name()),
                        Image.open("cards/" + poker_game[3].get_hand()[3].image_file_name()),
                        Image.open("cards/" + poker_game[3].get_hand()[4].image_file_name()))
    
        img = make_column(hand_one, hand_two, hand_three, hand_four)
        
        d = ImageDraw.Draw(img)
        
        myFont = ImageFont.truetype("Arial.ttf", 20)
        
        d.text((img.width-190, 60), poker_game[0].get_hand_type(), font=myFont, fill=(255, 255, 255))
        d.text((img.width-190, 200), poker_game[1].get_hand_type(), font=myFont, fill=(255, 255, 255))
        d.text((img.width-190, 340), poker_game[2].get_hand_type(), font=myFont, fill=(255, 255, 255))
        d.text((img.width-190, 480), poker_game[3].get_hand_type(), font=myFont, fill=(255, 255, 255))
            
        if (poker_game.index(winner) == 0):
            d.text((img.width-190, 90), "WINNER!", font=myFont, fill=(255, 0, 0))
        if (poker_game.index(winner) == 1):
            d.text((img.width-190, 230), "WINNER!", font=myFont, fill=(255, 0, 0))
        if (poker_game.index(winner) == 2):
            d.text((img.width-190, 370), "WINNER!", font=myFont, fill=(255, 0, 0))
        if (poker_game.index(winner) == 3):
            d.text((img.width-190, 510), "WINNER!", font=myFont, fill=(255, 0, 0))
        if (winner_true == 0):
            d.text((img.width-100, 265), "TIE", font=ImageFont.truetype("Arial.ttf", 40), fill=(255, 0, 0))
            
        img.show()
 
    