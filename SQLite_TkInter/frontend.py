from tkinter import *
# importing custom built SQLite database
from backend import Database

# creating the database to hold info entered by user
database=Database("people.db")

# allowing the selecton of the list box and display in the entry boxes
# which allows the user to see and edit what's in the database
def get_selected_row(event):
    global selected_tuple
    index=list_box.curselection()[0]
    selected_tuple=list_box.get(index)
    name_entry.delete(0,END)
    name_entry.insert(END,selected_tuple[1])
    job_entry.delete(0,END)
    job_entry.insert(END,selected_tuple[2])
    hobbies_entry.delete(0,END)
    hobbies_entry.insert(END,selected_tuple[3])
    discussions_entry.delete(0,END)
    discussions_entry.insert(END,selected_tuple[4])


## -- CREATING COMMANDS THAT WILL TIE THE DATABASE AND INTERFACE -- ##

# allowing viewing of entire database
def view_command():
    list_box.delete(0,END)
    for row in database.view():
        list_box.insert(END,row)

# allowing searching by any parameter
def search_command():
    list_box.delete(0,END)
    for row in database.search(name_text.get(),job_text.get(),hobbies_text.get(),discussions_text.get()):
        list_box.insert(END,row)


# allowing adding of new people to database
def add_command():
    database.insert(name_text.get(),job_text.get(),hobbies_text.get(),discussions_text.get())
    list_box.delete(0,END)
    list_box.insert(END,(name_text.get(),job_text.get(),hobbies_text.get(),discussions_text.get()))

# allowing deletion of person from database
def delete_command():
    database.delete(selected_tuple[0])

# allowing updating person from entry boxes once person is selected by mouse or touch
def update_command():
    database.update(selected_tuple[0],name_text.get(),job_text.get(),hobbies_text.get(),discussions_text.get())



## -- BUILDING THE ACTUAL TKINTER WINDOW -- ##

window=Tk()

window.wm_title("People App")

## LABELS FOR ENTRY BOXES
name_label=Label(window,text="Name")
name_label.grid(row=0,column=0)

hobbies_label=Label(window,text="Hobbies")
hobbies_label.grid(row=0,column=2)

job_label=Label(window,text="Job")
job_label.grid(row=1,column=0)

discussions_label=Label(window,text="Discussions")
discussions_label.grid(row=1,column=2)

## ENTRY BOXES, TIED TO BACKEND
name_text=StringVar()
name_entry=Entry(window,textvariable=name_text)
name_entry.grid(row=0,column=1)

hobbies_text=StringVar()
hobbies_entry=Entry(window,textvariable=hobbies_text)
hobbies_entry.grid(row=0,column=3)

job_text=StringVar()
job_entry=Entry(window,textvariable=job_text)
job_entry.grid(row=1,column=1)

discussions_text=StringVar()
discussions_entry=Entry(window,textvariable=discussions_text)
discussions_entry.grid(row=1,column=3)

# the actual viewing of all the people in the database
list_box=Listbox(window, height=6,width=35)
list_box.grid(row=2,column=0,rowspan=6,columnspan=2)

# small scroll bar to have ease of access of people in database
scroll_bar=Scrollbar(window)
scroll_bar.grid(row=2,column=2,rowspan=10)
list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

# "binding" the listbox to having the selection of the rows and subsequent methods
list_box.bind('<<ListboxSelect>>',get_selected_row)

# buttons that utilize the methods declared earlier
view_all_button=Button(window,text="View all", width=12,command=view_command)
view_all_button.grid(row=2,column=3)

search_button=Button(window,text="Search entry", width=12,command=search_command)
search_button.grid(row=3,column=3)

add_entry_button=Button(window,text="Add entry", width=12,command=add_command)
add_entry_button.grid(row=4,column=3)

update_entry_button=Button(window,text="Update selected", width=12,command=update_command)
update_entry_button.grid(row=5,column=3)

delete_entry_button=Button(window,text="Delete selected", width=12,command=delete_command)
delete_entry_button.grid(row=6,column=3)

# closes the app, using built in "destroy" command in TkInter
close_app_button=Button(window,text="Close", width=12,command=window.destroy)
close_app_button.grid(row=7,column=3)

# keeps the window open as long as the user wants
window.mainloop()
