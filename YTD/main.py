import pytube
from tkinter import *
from PIL import ImageTk,Image

def clear(n):
    n.config(fg="#e6c860")

def click():

    if not e.get():
        new_label = Label(frame, text='Enter the link'.title(), fg="red", bg="#e6c860", font=("times new roman","15","bold"))
        new_label.place(relx=0.5, rely=0.65, anchor=CENTER)
        new_label.after(2000,clear,new_label)
    elif  "youtube.com" not in e.get() or "https://www.youtube.com/" not in e.get():

        new_label = Label(frame, text='Valid link'.title(), fg="red", bg="#e6c860",
                          font=("times new roman", "15", "bold"))
        new_label.place(relx=0.5, rely=0.65, anchor=CENTER)
        new_label.after(3000, clear, new_label)
    else:
        link = e.get()
        yt = pytube.YouTube(link)
        yt.streams.get_highest_resolution().download(output_path="./../Desktop")
        new_label=Label(frame,text='Download Succeed'.title(),fg="Green",bg="#e6c860",font=("times new roman","10","bold"))
        new_label.place(relx=0.5,rely=0.65,anchor=CENTER)
        new_label.after(3000,clear,new_label)


root=Tk()
root.title("YTD")
root.iconbitmap("youtube.ico")
root.geometry("860x920")
frame= Frame(root,width=850,height=916)
frame.pack()
frame.place(anchor='center',relx=0.5,rely=0.5)
button_pic=ImageTk.PhotoImage(Image.open("favicon.ico"))
background=ImageTk.PhotoImage(Image.open('Untitled-2.png'))
hm=Label(frame,image=background).pack()
e=Entry(frame,width=70,border=5)
e.place(relx=0.5, rely=0.6, anchor=CENTER)
download_b=Button(frame,text="Download",command=click,image=button_pic,padx=30,pady=50).place(relx=0.5, rely=0.75, anchor=CENTER)
root.mainloop()













# import geocoder as geo
#
# ip_address =geo.ip('me')
#
# print(ip_address)