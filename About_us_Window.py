from tkinter import *
from PIL import Image , ImageTk,ImageDraw, ImageFilter
import sys


main = Tk()
main.title("About Us")
main.resizable(False,False)

     
          
# EDIT HERE•••••••••••••••••••••••••••••••••••••••••••••••••••••••EDIT HERE

def Datas(): # Edit Datas Here !
     __Id__(
          4980,               # Index_Number (in Integer)
          None,               # Profile_Pic path must be square like 300x300,600x600,1090x1090
          "I.Fname Lname",    # Name
          None,               # Date of Birth format = YYYY-MM-DD
          None,               # Expert in (Fields that you are in expert level) like : Music editing $MAXIMUM_LETTERS :119$
          None,               # Email_Address
          None,               # Instagram_Id
          None                # Facebook_Id
          )                   # If you like to be this field empty then type None
     __Id__(
          4000,
          "PPs\\icon.ico",
          "U.Yuwan Kumar",
          "2002-04-02",
          "Programming(Python,Java,Pascal),VFX ,Video Editing,3D Modeling,Cinema 4D,Photo Shop,Adobe Illustrater",
          "yuwankmr@gmail.com",
          None,
          None
          )
     __Id__(
          4080,
          None,
          "I.Fname Lname",
          None,
          None,
          None,
          None,
          None
          )
     __Id__(
          4080,
          None,
          "I.Fname Lname",
          None,
          None,
          None,
          None,
          None
          )
     
# EDIT HERE•••••••••••••••••••••••••••••••••••••••••••••••••••••••EDIT HERE

canvas = Canvas(main,height = 400,width = 800,background = 'gray70')
canvas.pack()

canvas.create_rectangle(110,400,805,806,fill = 'white',activefill = 'gray95',width=0)
# Close Button
canvas.create_rectangle(745,410,795,460,fill = 'white',activefill = 'gray75',width = 0)
canvas.create_text(770,430,text = 'x',fill = 'light gray',font = ('bold',50))

# 0_Info
head_color = 'black'
content_color = 'gray40'
offset_y = 30
offset_x = 10

# content lenth : 44
sub_name        = canvas.create_text(450,450,text = "Name",font = ('bold',50),fill= content_color,tag = 'text',activefill = head_color)
sub_index_head  = canvas.create_text(200+offset_x,590-offset_y,text = "Index_no :",font = ('bold',18),fill= head_color,tag = 'text')
sub_batch_head  = canvas.create_text(200+offset_x,625-offset_y,text = "Batch      :",font = ('bold',18),fill= head_color,tag = 'text')
sub_dob___head  = canvas.create_text(200+offset_x,660-offset_y,text = "D.O.B      :",font = ('bold',18),fill= head_color,tag = 'text')
subexpert_head  = canvas.create_text(200+offset_x,695-offset_y,text = "Expert in  :",font = ('bold',18),fill= head_color,tag = 'text')
sub_index       = canvas.create_text(510+offset_x,590-offset_y,text = "                                            ",font = ('bold',18),fill= content_color,tag = 'text',activefill = head_color)
sub_batch       = canvas.create_text(510+offset_x,625-offset_y,text = "2018-O/L & 2021-A/L (Commerce)                ",font = ('bold',18),fill= content_color,tag = 'text',activefill = head_color)
sub_dob         = canvas.create_text(510+offset_x,660-offset_y,text = "                                            ",font = ('bold',18),fill= content_color,tag = 'text',activefill = head_color)
sub_expert      = canvas.create_text(510+offset_x,695-offset_y,text = "                                            ",font = ('bold',18),fill= content_color,tag = 'text',activefill = head_color)
sub_expert_2    = canvas.create_text(510+offset_x,730-offset_y,text = "                                            ",font = ('bold',18),fill= content_color,tag = 'text',activefill = head_color)
sub_expert_3    = canvas.create_text(510+offset_x,765-offset_y,text = "                                            ",font = ('bold',18),fill= content_color,tag = 'text',activefill = head_color)

sub_email_head  = canvas.create_text(200+offset_x,790-offset_y,text = "e-mail address:",font = ('bold',10),fill= head_color,activefill = 'black',tag = 'text')
sub_insta_head  = canvas.create_text(475+offset_x,790-offset_y,text = "Instagram Id  :",font = ('bold',10),fill= head_color,activefill = 'black',tag = 'text')
sub_faceb_head  = canvas.create_text(675+offset_x,790-offset_y,text = "Facebook Id   :",font = ('bold',10),fill= head_color,activefill = 'black',tag = 'text')
sub_email       = canvas.create_text(200+offset_x,810-offset_y,text = "                                            ",font = ('bold',10,'underline'),fill= content_color,activefill = 'orange',tag = 'text')
sub_insta       = canvas.create_text(500+offset_x,810-offset_y,text = "             insta_Id                       ",font = ('bold',10),fill= content_color,activefill = 'red',tag = 'text')
sub_faceb       = canvas.create_text(700+offset_x,810-offset_y,text = "             faceb_Id                       ",font = ('bold',10),fill= content_color,activefill = 'blue',tag = 'text')

i = -1
count = -1
positions,pos_x ,pos_y,index_no,profile_paths,index_no,names,dob,expert,email,insta,facebc = [[0,0],[1,0],[0,1],[1,1]],[],[],[],[],[],[],[],[],[],[],[]

def click(event):
     global i,index_no,profile_paths,index_no,names,dob,expert,email,insta,facebc
     ex = event.x
     ey = event.y
     def view_datas():
          canvas.itemconfig('img_box',fill = 'gray95')
          canvas.itemconfig('img_box_'+str(card),fill = 'gray')
          canvas.itemconfig(sub_name,text = names[card])
          canvas.itemconfig(sub_index,text = str(index_no[card])+" "*60)
          canvas.itemconfig(sub_dob,text = str(dob[card])+" "*50)
          for s in range(len(str(expert[card])),119):
               expert[card] = str(expert[card])+' '
          if expert[card][39] != ' ':
               canvas.itemconfig(sub_expert,text = expert[card][:39]+'-')
          else:
               canvas.itemconfig(sub_expert,text = expert[card][:39]+' ')
          if expert[card][79] != ' ':
               canvas.itemconfig(sub_expert_2,text = expert[card][39:79]+'-')
          else:
               canvas.itemconfig(sub_expert_2,text = expert[card][39:79]+' ')
          canvas.itemconfig(sub_expert_3,text = expert[card][79:119])
          canvas.itemconfig(sub_email,text = str(email[card]))
          canvas.itemconfig(sub_insta,text = str(insta[card]))
          canvas.itemconfig(sub_faceb,text = str(facebc[card]))
     def up():
          global i
          i += 1
          canvas.move('all',0,i-2*i)
          if i == -1:
               None
          elif i < 28:
               canvas.after(5,up)
     if i < 28:
          if  ((ex>0)and(ex<400))and((ey>0)and(ey<200)):
               up()
               card = 0
          elif((ex>400)and(ex<800))and((ey>0)and(ey<200)):
               up()
               card = 1
          elif((ex>0)and(ex<400))and((ey>200)and(ey<400)):
               up()
               card = 2
          elif((ex>400)and(ex<800))and((ey>200)and(ey<400)):
               up()
               card = 3
          view_datas()
     elif  ((ex>745)and(ex<795))and((ey>0)and(ey<50)):
          i = -29
          up()
     elif ((ex>0)and(ex<110)):
          if  ((ey>0)and(ey<100)):
               card = 0
          elif(ey>100)and(ey<200):
               card = 1
          elif(ey>200)and(ey<300):
               card = 2
          elif(ey>300)and(ey<400):
               card = 3
          view_datas()

def __Id__(index_number , profile_pic , name , DOB  , expert_in  , email_address , instagram_id , facebook_id ):
     global count,profile_paths,pos_x,pos_y,index_no,names,dob,expert,email,insta,facebc
     count += 1
     positionx = positions[count][0]
     positiony = positions[count][1]
     profile_paths.append(profile_pic)
     pos_x.append(positionx)
     pos_y.append(positiony)
     index_no.append(index_number)
     names.append(name)
     dob.append(DOB)
     expert.append(expert_in)
     email.append(email_address)
     insta.append(instagram_id)
     facebc.append(facebook_id)
     index = "card_"+str(index_number)

# Bg_Card
     canvas.create_rectangle(positionx*400,positiony*200,(positionx+1)*402,(positiony+1)*202,fill = 'gray',activefill = 'white',outline = 'white',tag = (index,str(count)))   
     
# Index_Number
     canvas.create_text(positionx*400+85,positiony*200+175,text = index_number,fill = 'white',justify = 'left',font = ('Bold',30),activefill = 'black')
     
# D.O.B
     #canvas.create_text(positionx*400+270,positiony*200+50,text = DOB,fill = 'gray25',justify = 'left',font = ('bold',10,''),activefill = 'black')
# Name
     if name != None:
          spaces = ' '*(13-len(name))
          canvas.create_text(positionx*400+280,positiony*200+75,text = name+spaces,fill = 'gray25',justify = 'left',font = ('bold',25,''),activefill = 'black')

     # Batch
     batch = '2018-O/L & 2021-A/L(Commerce)'
     canvas.create_text(positionx*400+280,positiony*200+100,text = batch,fill = 'gray25',justify = 'left',font = ('bold',10,''),activefill = 'black')

     
Datas()

# Profile_Pictures
for q in range(0,len(profile_paths)):
     canvas.create_rectangle(102,q*100+402,110,q*100+508,fill = 'gray95',width = 0,tag = ('img_box_'+str(q),'img_box'))
     try:
          pp2 = Image.open(profile_paths[q]).resize((150,150))
          pp100 = Image.open(profile_paths[q]).resize((100,100))
          pp100 = ImageTk.PhotoImage(pp100)

          def crop(img,width,height):
               img_width , img_height = img.size
               return img.crop(((img_width - width) // 2,(img_height-height) //2, (img_width+width)//2,(img_height+height)//2))

          def circle(img,radius = 1.5,offset = 0):
               offset = radius*2+offset
               mask = Image.new('L',img.size,0)
               draw = ImageDraw.Draw(mask)
               draw.ellipse((offset,offset,img.size[0]-offset,img.size[1]-offset),fill = 255)
               mask = mask.filter(ImageFilter.GaussianBlur(radius))
               result = img.copy()
               result.putalpha(mask)
               return result
          ppl = crop(pp2 , 150,150)
          ppl = circle(ppl)

          #ppl.save(f'profile_'+str(q)+'.png')
          ppl = ImageTk.PhotoImage(ppl)
     
          canvas.create_image(pos_x[q]*400+80,pos_y[q]*200+80,image = ppl )
          canvas.create_image(52,q*100+450,image = pp100 )
     except:
          a = canvas.create_oval(pos_x[q]*400+10,pos_y[q]*200+10,pos_x[q]*400+150,pos_y[q]*200+150,fill = 'light blue', outline = 'white',width = 6,tag = str(q))
          canvas.create_text(pos_x[q]*400+80,pos_y[q]*200+80,text = 'O',fill = 'white',justify = 'center',font = ('Bold',100))

def double(event):
     None
canvas.bind('<Button-1>',click)
canvas.bind('<Double-1>',double)
main.mainloop()


