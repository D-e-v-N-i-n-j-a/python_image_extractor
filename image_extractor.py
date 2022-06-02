from ast import Pass
import io
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import urllib.request
from bs4 import BeautifulSoup as bs
import re

class IMAGE_EXTRACTOR:
    def __init__(self,root):
        self.root = root
        self.root.title("IMAGE EXTRACTOR")
        self.root.geometry("500x500")
        searchBtn = StringVar()
        images = []
        def fetchImage():
            if searchBtn.get() == "":
               print("something went wrong")
            else: 
                page = urllib.request.urlopen(searchBtn.get())
                soup = bs(page,"html.parser")
                allImage = soup.body.findAll('img')
                for item in allImage:
                    images.append(item.get('src'))
                print(images)
                    
            
           
            
        
        
        title = Label(self.root,text="IMAGE EXTRACTOR",width=30,height=2,bg="#528BFF",fg="white",font=("Arial",20,"bold"))
        title.place(x=0,y=0)
        
        urlBox =  Entry(self.root,textvariable=searchBtn,width=90,bg="#E1E1ff")
        urlBox.place(x=0,y=100)
        
        btnSearch = Button(self.root,command=fetchImage,text="FETCH IMAGE")
        btnSearch.place(x=0,y=120)
        
        def readImages():
           
            for i in range(0,len(images)):
                
                im = Image.open(io.BytesIO(images[i]))
                image_ = ImageTk.PhotoImage(im)
                label1 = Label(self.root, image=image_)
                label1.place(x=0,y=0)
            
            
            
        







root = Tk()
obj = IMAGE_EXTRACTOR(root)
root.mainloop()
