import tkinter as tk
from tkinter import *
import time
root = tk.Tk()
row_counter=3
invalid_camper_num=0
quad_count=0
tracker=0
data_list=[]
list_initializer=0
update_counter=0

def add_row():
    # Global variables can be accessed and put on all functions without any errors.
    global quad_count
    global row_counter
    global invalid_camper_num
    global list_initializer
    global data_list
    global update_counter
    global to_add_label

    if 5>int(camper_num_entry.get()) or 10<int(camper_num_entry.get()):
        invalid_camper_num=1
        button["text"]="Invalid"


    else: # If the camper number is valid as stated in line 23, continue, otherwise don't
        button["text"]="Click to add data"
        invalid_camper_num=0
    # Removes any old data still on screen below row 2 to prevent stacking
    if invalid_camper_num==0:

        for x in root.grid_slaves():
            if int(x.grid_info()["row"]) > 2:# Uses square brackets to get the all the widget attribrutes
                x.grid_forget() # Uses forget. Destroy doesn't work

    row_counter=3 # Row counter is 3, as rows 0,1 and 2 are taken already

    # The list

    entry_list = [group_leader_entry.get(), location_entry.get(),
                  camper_num_entry.get(), weather_entry.get()]
    # Also updating and deleting
    if list_initializer==0 or data_list==[]:
        # The entry list is compared against the already existing one to locate duplicate names
        # but an empty list cannot be compared against nothing, so we must exclude them from this
        data_list = entry_list
        list_initializer+=1

    else:
        while len(data_list)>update_counter:
            # Compares the entry list given to the already exisiting data list to
            # Find duplicates.
            if entry_list[0] == data_list[update_counter]:# Entry_list[0] is always the name
                data_list.pop(update_counter)
                data_list.pop(update_counter) # Including the name, pop 4 items,
                data_list.pop(update_counter)# As the next 3 are going to be the next entries
                data_list.pop(update_counter)
            update_counter+=4 # Goes up in fours to prevent variables other than names to get checked

        else: # Because this code is in a while loop, the else will ensure this code is only run once
              # After the duplicates have been found, To prevent unnecessary appending.
            for i in range(len(entry_list)):
                data_list.append(entry_list[i]) # append normally, after duplicate names are popped
        update_counter = 0 # Set for the next button click
    is_moving_on = moving_on_entry.get()
    is_moving_on = is_moving_on.lower() # so 'yes' isn't case sensitive
    if is_moving_on == "yes":
        counter=0 # Initially, an index was used, but it was affected by other entries having same name
        for i in data_list:
            if counter==0 or counter%4==0: # Makes only names are accounted for.
                if i == str(group_leader_entry.get()): # i is the current leader name.
                    data_list.pop(counter)         # If the current leader name matches
                    data_list.pop(counter)         # The one found, delete the data
                    data_list.pop(counter)         # Relating to that leader name
                    data_list.pop(counter)          # As the group is moving on, and must be deleted
            counter+=1


        # Sets the button text to normal if camper number is valid
        invalid_camper_num=0
        button["text"] = "Click to add data"
    if invalid_camper_num==0: # Prevents invalid data entering the table, as a failsafe
        for i in range(len(data_list)):
            if i%4==0:
                # Makes it so 4 entries are on the same row
                # But any more will go the next row
                row_counter+=1
                tracker=0 # Makes the new row start on column 0 if 4 entries are placed
            to_add_label=Label(text=data_list[i],width=15)
            to_add_label.grid(row=row_counter,column=tracker) # Places the labels accordingly
            tracker+=1


    # Resets variable
    invalid_camper_num = 0

# Group leader entry and Text
group_leader_entry=tk.Entry(root,width=10)
group_leader_entry.grid(row=1,column=0)

group_leader_text=Label(text="Group Leader",width=10)
group_leader_text.grid(row=0,column=0)

# Location Entry and text
location_entry=tk.Entry(root,width=10)
location_entry.grid(row=1,column=1)

location_text=Label(text="Location",width=10)
location_text.grid(row=0,column=1)

# Number of campers
camper_num_entry = tk.Entry(root,width=10)
camper_num_entry.grid(row=1,column=2)

camper_num_text=Label(text="Num of Campers",width=12)
camper_num_text.grid(row=0,column=2)

# Weather conditions
weather_entry = tk.Entry(root,width=10)
weather_entry.grid(row=1,column=3)

weather_text=Label(text="weather",width=10)
weather_text.grid(row=0,column=3)

# Moving on
moving_on_entry=tk.Entry(root,width=10)
moving_on_entry.grid(row=1,column=4)

moving_on_text=Label(text="Moving on?",width=15)
moving_on_text.grid(row=0,column=4)

# Data add button, uses function from line 5
button=Button(text="Click to add data", command=add_row)
button.grid(row=2,column=0)

# Geometry and constant loop to keep window open
root.geometry("650x450")
root.mainloop()