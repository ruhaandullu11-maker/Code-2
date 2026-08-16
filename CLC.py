import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x300")
window.resizable()

def pressnumber(number):
  textbox = entrylabel.cget('text')
  entrylabel.configure(text = textbox + str(number))

def pressoperator(operator):

  textbox = entrylabel.cget('text')
  textexp = expresslabel.cget('text')

  expresslabel.configure(text = textexp + textbox + operator)
  entrylabel.configure(text = '')

def pressclear():
  expresslabel.configure(text = '')
  entrylabel.configure(text = '')

def pressequals():

  textbox = entrylabel.cget('text')
  textexp = expresslabel.cget('text')

  expresslabel.configure(text = textexp + textbox + ' = ')

  try:
    ans = eval(textexp + textbox)
    entrylabel.configure(text = str(ans))
  except:
    entrylabel.configure(text = 'ERROR')


expresslabel = tk.Label(window, text = '', background = 'HotPink', width = 36, height= 3, borderwidth = 3, relief = 'ridge', anchor = tk.E)
expresslabel.grid(column = 0, row = 0, columnspan = 5)


entrylabel = tk.Label(window, text = '', background = 'HotPink', font = ('Arial bold', 15), width = 22, height= 3, borderwidth = 3, relief = 'ridge', anchor = tk.E)
entrylabel.grid(column = 0, row = 1, columnspan = 5)




tk.Button(text = ' 7 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(7)).grid(row =2, column = 0, sticky = tk.NSEW)
tk.Button(text = ' 8 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(8)).grid(row = 2, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 9 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(9)).grid(row=2, column = 2, sticky= tk.NSEW)
tk.Button(text = ' / ', fg = 'black', background = 'gold', command= lambda: pressoperator('/')).grid(row=2, column = 3, sticky= tk.NSEW)
tk.Button(text = ' C ', fg = 'black', background = 'turquoise', command = pressclear).grid(row=2, column = 4, rowspan= 2, sticky= tk.NSEW)


tk.Button(text = ' 4 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(4)).grid(row=3, column = 0, sticky= tk.NSEW)
tk.Button(text = ' 5 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(5)).grid(row=3, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 6 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(6)).grid(row=3, column = 2, sticky= tk.NSEW)
tk.Button(text = ' * ', fg = 'black', background = 'gold', command= lambda: pressoperator('*')).grid(row=3, column = 3, sticky= tk.NSEW)



tk.Button(text = ' 1 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(1)).grid(row=4, column = 0, sticky= tk.NSEW)
tk.Button(text = ' 2 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(2)).grid(row=4, column = 1, sticky= tk.NSEW)
tk.Button(text = ' 3 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(3)).grid(row=4, column = 2, sticky= tk.NSEW)
tk.Button(text = ' - ', fg = 'black', background = 'gold', command= lambda: pressoperator('-')).grid(row=4, column = 3, sticky= tk.NSEW)
tk.Button(text = ' = ', fg = 'black', background = 'turquoise', command= pressequals).grid(row=4, column = 4, rowspan= 2, sticky= tk.NSEW)




tk.Button(text = ' 0 ', fg = 'black', background = 'orange red', command= lambda: pressnumber(0)).grid(row=5, column = 0, columnspan = 2, sticky= tk.NSEW)
tk.Button(text = ' . ', fg = 'black', background = 'gold', command= lambda: pressnumber('.')).grid(row=5, column = 2, sticky= tk.NSEW)
tk.Button(text = ' + ', fg = 'black', background = 'gold', command= lambda: pressoperator('+')).grid(row=5, column = 3, sticky= tk.NSEW)
tk.mainloop()