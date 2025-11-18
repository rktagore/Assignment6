import tkinter as tk
import tkinter.font as tfont
from tkinter import ttk
window = tk.Tk()
window.title("My Application")
window.minsize(height=300,width=400)
custom_font=tfont.Font(family="Times New Roman",size=15,weight="bold")
label = ttk.Label(text="Hello World!",font=custom_font,padding=5)
label.pack()
label["text"]="Have a nice day!"
label.config(text="My Name App")
#fetch the value from the textbox and use it at any where(label)
def function_button():
    label.config(text=user_input.get())
#Entry component=>taking user input using Entry
user_input = ttk.Entry(width=30)
user_input.pack(pady=5)
#Buttons
button = ttk.Button(text="Click", command = function_button)
button.pack(pady=5)
#Quit the window by using button with the help of window.destroy method
quit_button =ttk.Button(text="Quit",command=window.destroy)
quit_button.pack(pady=5)
#Separator widget
sep = ttk.Separator(orient="horizontal") # we can utilised the entire horizontal line
sep.pack(fill='x',pady=5)
#Entry component is a single line textbox. for multiple line text box use Text widget:
text = tk.Text(height=5,width=25) #height=shows only 5lines and width=25 characters length
text.pack(pady=5)
'''
pady=10 for above and below space for selected widget, when widgets are in one below another. 
padx=10 for left and right space for selected widget, when widgets are in one after another
'''
text.focus()#for cursor location focus
text.insert("1.0","Enter your comments")#1.0 means first line and first character index is 0th i.e. default text
def text_function():
    text_data=text.get("1.0","end")
    print(text_data,end='')
#how does we retrieve fetch the entered text from text widget
text_button = ttk.Button(text="Get Text",command=text_function) #get text / fetch text / retrieve text
text_button.pack(pady=5)
#checkboxbutton widget
check_option = tk.BooleanVar()
def check_option_task():
    print(check_option.get(),type(check_option.get()))
check_button = ttk.Checkbutton(text = "Agree with the terms & conditions?", variable = check_option,
                               command = check_option_task)
check_button.pack() #to place it on the window use pack

#Radiobutton widget
radio_value = tk.StringVar()
def get_radio_value():
    print(radio_value.get())
option1 = ttk.Radiobutton(text="Male",variable=radio_value,value="Male",command=get_radio_value)
option2 = ttk.Radiobutton(text="Female",variable=radio_value,value="Female",command=get_radio_value)
option1.pack()
option2.pack()

#Combobox widget
selected_country = tk.StringVar()
countries = ttk.Combobox(textvariable=selected_country,values=("Australia","Canada","India","Sweden","US"))
countries["state"]="readonly"
countries.pack()
def display_country(event):
    msg = f"Selected country is {selected_country.get()}"
    country_label = ttk.Label(text = msg)
    country_label.pack()
countries.bind("<<ComboboxSelected>>",display_country)

#Listbox widget:
food_items=("Pizza","Burger","Garlic Bread","Nachos","Salad")
fav_food = tk.StringVar(value=food_items)
food_list = tk.Listbox(listvariable=fav_food,height=5,selectmode="extended") #by default one time only selected
food_list.pack()
def get_fav_food(event):
    food_indices = food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))
food_list.bind("<<ListboxSelect>>",get_fav_food)

#Spinbox widget:
counter = tk.IntVar(value=10)
def get_spin_box_value():
    print(f"Current spin box value:{spin_box.get()}")
spin_box = ttk.Spinbox(values=tuple(range(5,105,5)),textvariable=counter,wrap=True,command=get_spin_box_value)
spin_box.pack()
print(f"Initial value:{spin_box.get()}")

window.mainloop()
