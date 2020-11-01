import COVID19Py
import tkinter as tki
from tkinter import *
from PIL import ImageTk,Image



# this will get all the data at once 
covid19 = COVID19Py.COVID19()
data = covid19.getAll()



#converting data dictionry into two part 1st overall data 
latest_data = data['latest']

#data by the locations 
all_country_data = data['locations']

#list of all the country from the data
countries_list = []  # this is our country lsit

for country in all_country_data:
    countries_list.append(country['country'])

all_country_data.append({
        'country': 'no data',
        'country_population': 'no data',
        'coordinates': {
            'latitude': '41.1533',
            'longitude': '20.1683'
        },
        'latest': {
            'confirmed': 'no data',
            'deaths': 'no data',
            'recovered': 'no data'
        }
})


root = Tk()
root.title('corona virus tracker by shj')
root.iconbitmap('icon.ico')
root.geometry('600x600')
root.configure(background='white')

mylabel10 = Label(root,text='Enter  ',bg="white", fg="white", font="none 24 bold")
mylabel10.grid(row=1,column=1)


mylabel1 = Label(root)
mylabel2 = Label(root)
mylabel3 = Label(root)
mylabel4 = Label(root)

#show result

def search_result(serch_index):
    global country_name 
    global coutry_population
    global country_data_confirm
    global country_data_death
    global mylabel1
    global mylabel2
    global mylabel3
    global mylabel4
    
    #next line will print data in the terminal
    country_name ="Name of the country          "+ str(all_country_data[serch_index]['country']) 
    coutry_population ="population of the country       "+ str(all_country_data[serch_index]['country_population'])
    country_data_confirm ="latest confirmed cases           "+ str(all_country_data[serch_index]['latest']['confirmed'])
    country_data_death ="latest confirmed deaths            "+ str(all_country_data[serch_index]['latest']['deaths'])
   
    mylabel1.destroy()
    mylabel2.destroy()
    mylabel3.destroy()
    mylabel4.destroy()
    
    mylabel1 =Label(root,text=country_data_confirm,bg="white", fg="#138808", font="none 14 bold")
    mylabel1.grid(column=2, row = 18)
    mylabel2 =Label(root,text=country_data_death,bg="white", fg="#138808", font="none 14 bold")
    mylabel2.grid(column=2, row = 19)
    mylabel3 =Label(root,text=country_name,bg="white", fg="#138808", font="none 14 bold")
    mylabel3.grid(column=2, row = 20)
    mylabel4 =Label(root,text=coutry_population, bg="white", fg="#138808", font="none 14 bold")
    mylabel4.grid(column=2, row = 21)
   
   

my_img1 = ImageTk.PhotoImage(Image.open("corona1.jpg"))   
my_label5= Label(image=my_img1)
my_label5.grid(column=2, row = 10)
    


mylabel =Label(root,text="Enter the country name",bg="orange red", fg="white", font="none 24 bold")
mylabel.grid(column=2, row = 12,padx=10,pady=10)

serchbox = Entry(root,bg="#000080", fg="white", font="none 14 bold")
serchbox.grid(column=2, row = 14 ,padx=10,pady=10)


#function to search string in text 
def find():
    try:
        search_index = countries_list.index(serchbox.get().title())
        search_result(search_index)
    except:
        search_result(-1)
        
mybutton = Button(root,text="   Find      ",command =find,bg="#000080", fg="white", font="none 14 bold")
mybutton.grid(column=2, row = 16)



root.mainloop()