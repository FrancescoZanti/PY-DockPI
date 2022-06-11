import os 

from tkinter import *      #Import Tkinter
from tkinter.ttk import *

from time import strftime

from mod_clock import *
from mod_feed import *


## Env Variables ##
MOD_FEED_URL = os.environ['MOD_FEED_URL']
##



root = Tk()               #Bind Tkinter to the root object
root.title('Clock')
root.attributes('-fullscreen', True)
root.configure(background='black')
root.config(cursor=None)


lbl = Label(root, font = ('ds-digital', 80, 'bold'),
            background = 'black',
            foreground = 'white')

lbl2 = Label(root, font = ('ds-digital', 40, 'bold'),
            background = 'black',
            foreground = 'white')

lbl3 = Label(root, font = ('ds-digital', 10, 'bold'),
            background = 'black',
            foreground = 'white')


  
lbl.config(text = time())
lbl.after(1000, time)
lbl2.config(text = date())
lbl2.after(1000, date)
lbl3.config(text = get_feed(MOD_FEED_URL) )
lbl3.after(1000, get_feed)




# Placing clock at the centre
# of the tkinter window
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl2.place(relx=0.8, rely=0.2, anchor=CENTER)
lbl3.place(relx=0.5, rely=0.8, anchor=CENTER)

time()

date()
  
root.mainloop()