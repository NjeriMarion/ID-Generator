from PIL import Image, ImageDraw, ImageFont
import random
import os
import datetime

image = Image.new('RGB', (1000, 900), (255,255,255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size = 40)
os.system("ID CARD Generator")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y\t ID CARD Generator\t %I:%M:%S %p")
print(reg_format_date)

(x,y) = (50,50)
message = input('\nEnter Company Name ')
company = message
color = 'rgb(0,0,0)'
font = ImageFont.truetype('arial.ttf', size = 80)
draw.text((x,y), message, fill = color , font=font)

(x,y) = (600, 75)
id_number = random.randint(1000,1000000000000)
message = str('ID ' +str(id_number))
color = 'rgb(0,0,0)'
font = ImageFont.truetype('arial.ttf', size = 40)
draw.text((x,y), message, fill=color ,font=font)

(x,y) = (50, 250)
message = input("Enter your Names: ")
name = message
color = 'rgb(0,0,0)'
font = ImageFont.truetype('arial.ttf', size = 45)
draw.text((x,y), message, fill=color, font=font)


(x,y) = (50, 350)
message = input('Enter Your Gender: ')
color = 'rgb(0,0,0)'
draw.text((x,y), message, fill=color, font=font)

(x,y) = (250,350)
message = input('Enter Your Age: ')
color = 'rgb(0,0,0)'
draw.text((x,y), message, fill=color, font=font)

image.save(str(name)+'.png')

print(('\n\n\nYour ID Successfully created ' +name+'.png'))
