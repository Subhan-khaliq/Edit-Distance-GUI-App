list1=["Vidmate","Ytube","Iphone","Andriod","Pakistan","Lazy","Crazy","Fancy","Lenz","Gorgeous","Charming","Awsome","Great","Radiculus","Beautiful","Help","Hello","Yellow","People","subha"]

def editDistance(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if (str1[m - 1] == str2[n - 1]):
        cost = 0
    else:
        cost = 2

    return min(editDistance(str1, str2, m - 1, n) + 1,
               editDistance(str1, str2, m, n - 1) + 1,   
               editDistance(str1, str2, m-1, n - 1) + cost)

def suggestion(x):
    y=[]
    t=[]
    dist=0
    output=[]
    for i in range(len(list1)):
        dist=editDistance(x,list1[i],len(x),len(list1[i]))
        y.append(dist)
        t.append(list1[i])
    #For popup 3 names of minimum edit Distance
    for i in range(3):
        p=min(y)
        g=y.index(p)
        output.append(t[g])
        t.pop(g)
        y.pop(g)
    return output

import tkinter as tk
root=tk.Tk()
root.title("Suggestion APP") 
# setting the windows size
root.geometry("300x200")
def submit():
    name=name_entry.get()
    output=suggestion(name)
    change(output)
    name_label = tk.Label(root, text = 'Word', font=('calibre',15, 'bold'))
def reset():
    name_entry.delete(0,'end')
def change(ran_text):
    name_label1.config(text=ran_text,font=(0,15,'bold'))
    name_label1.grid(row=4,column=2,columnspan=2,sticky='nsew',pady=5)
name_label = tk.Label(root, text = 'Word', font=('calibre',15, 'bold'),fg="white",
    bg="black")
name_label1 = tk.Label(root, text = '', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,font=('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit,fg="white",
    bg="Red",)
sub_btn1=tk.Button(root,text = 'Cancel', command = reset,fg="white",
    bg="Orange",)
sub_btn2=tk.Button(root, text="Exit", command=root.destroy,fg="white",
    bg="blue",)
name_label.grid(row=0,column=1)
name_entry.grid(row=0,column=2)
sub_btn.grid(row=2,column=1)
sub_btn1.grid(row=2,column=2)
sub_btn2.grid(row=2,column=3)
root.mainloop()