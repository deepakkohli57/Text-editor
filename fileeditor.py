import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser,font,filedialog,messagebox
import os

main_application=tk.Tk()
main_application.geometry("1200x800")
main_application.title('vsEditor')
main_application.wm_iconbitmap('icon.ico')
############################### ----main_menu---- ######################################
############################### ----End main_menu---- ######################################

main_menu=tk.Menu()
#file_icon
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')


file=tk.Menu(main_menu,tearoff=False)


#edit
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')

edit=tk.Menu(main_menu,tearoff=False)

#viewicon
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')


view=tk.Menu(main_menu,tearoff=False)

#color_theme_icon
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')


color_theme=tk.Menu(main_menu,tearoff=False)
theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}


#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color_theme',menu=color_theme)
############################### ----Toolbar---- ######################################
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuples=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row=0,column=0)

#sizebox
size_tuple=tuple(range(8,80,2))
size_var=tk.IntVar()
size_box=ttk.Combobox(tool_bar,width=10,textvariable=size_var,state='readonly')
size_box['values']=size_tuple
size_box.current(8)
size_box.grid(row=0,column=1,padx=5)


#bold_btn
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#italic_btn
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

#underline_btn
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4)

#font_color_btn
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

#align-left
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6)

#align-center
align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7)

#align-right
align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8)
############################### ----End Toolbar---- ######################################

############################### ----Texteditor---- ######################################
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(fill=tk.Y,side=tk.RIGHT)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#text-editor functionality
current_font_family= 'Arial'
current_font_size= 12
def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)    
text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

size_box.bind("<<ComboboxSelected>>",change_font_size)    

#######---Button Functionality------################
#bold_btn
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_btn.configure(command=change_bold)   

#italic_btn
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))  

italic_btn.configure(command=change_italic)

#underline_btn
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))  

underline_btn.configure(command=change_underline)

#font_color_functionality
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

#align_left
def change_align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=change_align_left) 


def change_align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=change_align_right) 



def change_align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=change_align_center) 
############################### ----End Texteditor---- ######################################

############################### ----Status bar---- ######################################
status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        character=len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f"Character={character} words={words}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",changed)        
############################### ---End Status bar---- ######################################


############################### ----main_menu functionality---- ######################################
#new
url=''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)


#file_commands
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='ctrl+N',command=new_file)

#open_functionality
def open_file(event=None):
    global url
    url=tk.filedialog.askopenfilename(initialdir=os.getcwd(),title='Open File',filetypes=(('Text files','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return

    except:
        return
    main_application.title(os.path.basename(url))    


file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='ctrl+O',command=open_file)
def save_file():
  try:  
    global url
    if url:
        content=str(text_editor.get(1.0,tk.END))
        with open(url,'w',encoding='utf') as fw:
           fw.write(content)
    else:
        url=tk.filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text files','*.txt'),('All Files','*.*')))
        content2=text_editor.get(1.0,tk.END)
        url.write(content2)
        url.close()
  except:
      return      

file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='ctrl+S',command=save_file)
#save_as functionality
def save_as(event=None):
  try:  
    global url
    content=text_editor.get(1.0,tk.END)
    url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text files','*.txt'),('All files','*.*')))
    url.write(content)
    url.close()
  except:
      return

file.add_command(label='Save_As',image=save_as_icon,compound=tk.LEFT,accelerator='ctrl+shift+s',command=save_as)

def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed: 
            msgbox=messagebox.askyesnocancel('Warning!','Do you want to save this file ?')
            if msgbox is True:
                if url:
                  content=text_editor.get(1.0,tk.END)
                  with open(url,'w',encoding='utf-8') as filewrite:
                    filewrite.write(content)
                    main_application.destroy()
                else:
                  content2=str(text_editor.get(1.0,tk.END))
                  url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('All file','*.*')))
                  url.write(content2)
                  url.close()
                  main_application.destroy()
            
            elif msgbox is False:
              main_application.destroy() 
        else:
            main_application.destroy()
    except:
        return

file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='ctrl+f4',command=exit_func)

#edit_commands
edit.add_command(label='Copy',compound=tk.LEFT,image=copy_icon,accelerator='ctrl+c',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='Paste',compound=tk.LEFT,image=paste_icon,accelerator='ctrl+v',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut',compound=tk.LEFT,image=cut_icon,accelerator='ctrl+x', command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear_all',compound=tk.LEFT,image=clear_all_icon,accelerator='ctrl+a',command=lambda:text_editor.delete(1.0,tk.END))
def find(event=None):

    def find_func(event=None):
       word=nameentry.get()
       text_editor.tag_remove('match','1.0',tk.END)
       matches=0
       if word:
         start_pos=1.0
         while True:
            start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
            if not start_pos:
             break
            end_pos=f'{start_pos}+{len(word)}c'
            text_editor.tag_add('match',start_pos,end_pos)
            matches+=1
            start_pos=end_pos
            text_editor.tag_config('match',foreground='red',background='yellow')



    def replace_func(event=None):
        word=nameentry.get()
        replace_text=replaceentry.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    finddialog=tk.Toplevel()
    finddialog.geometry('450x250+500+200')
    finddialog.title('Find and Replace')
    finddialog.resizable(0,0)


    #label frame
    labelframe=ttk.LabelFrame(finddialog,text='Find and Replace')
    labelframe.pack(pady=20)

    #label
    namelabel=ttk.Label(labelframe,text='Name')
    replacelabel=ttk.Label(labelframe,text='Replace:')

    #entry
    nameentry=ttk.Entry(labelframe,width=24)
    replaceentry=ttk.Entry(labelframe,width=24)
    
    #button
    findbtn=ttk.Button(labelframe,text='Find',command=find_func)
    replacebtn=ttk.Button(labelframe,text='Replace',command=replace_func)

    #grid
   
    namelabel.grid(row=0,column=0,padx=4,pady=4)
    replacelabel.grid(row=1,column=0,padx=4,pady=4)
    nameentry.grid(row=0,column=1,padx=4,pady=4)
    replaceentry.grid(row=1,column=1,padx=4,pady=4)
    findbtn.grid(row=2,column=0,padx=8,pady=8)
    replacebtn.grid(row=2,column=1,padx=8,pady=8)

    finddialog.mainloop()


edit.add_command(label='Find',compound=tk.LEFT,image=find_icon,accelerator='ctrl+f',command=find)
#view functionality
show_toolbar=tk.BooleanVar()
show_toolbar=True
show_statusbar=tk.BooleanVar()
show_statusbar=True

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True

        
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True
           

#view_check_button
view.add_checkbutton(label='Toolbar',image=tool_bar_icon,variable=show_toolbar,command=hide_toolbar,onvalue=True,offvalue=0,compound=tk.LEFT)
view.add_checkbutton(label='Status bar',image=status_bar_icon,compound=tk.LEFT,onvalue=1,offvalue=False,variable=show_statusbar,command=hide_statusbar)


#functionality colortheme
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1

########----main-application shortcut keys----##############

main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Shift-s>",save_as)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find)



############################### ----main_menu functionality---- ######################################
main_application.config(menu=main_menu)
main_application.mainloop()