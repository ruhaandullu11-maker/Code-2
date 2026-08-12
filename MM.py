import tkinter as tk

stationsL = ['Gare', 'Lac', 'Musée Olympique', 'Centre ville', 'Flon', 'Place du mar.', 'Complexe sportif']

stationpL = ['Tuilière', 'Ouchy', 'Flon', 'Lausanne Sud', 'Le Mont', 'Lausanne ouest', 'Terminus']



def calculate():


  start = startstation.get()
  stop = stopstation.get()

    
  if start in stationsL:
    startline = stationsL
  else:
    startline = stationpL

  if stop in stationsL:
    stopline = stationsL
  else:
    stopline = stationpL

  if startline is stopline:
      numstops = abs(startline.index(start) - startline.index(stop))
  else:
  
    numstops = startline.index(start) - startline.index('Flon')
    numstops = abs(numstops) + abs(stopline.index('Flon') - stopline.index(stop))
  fare = numstops * 1.5
  farelabel.configure(text = 'Price = CHF ' + str(fare))


window = tk.Tk()
window.title("Imaginary Lausanne Metro Map")
window.configure(bg='DarkTurquoise')
window.geometry("600x600+10+0")  




canvas = tk.Canvas(window, width = 550, height=500)
canvas.pack()


xs = 50
ys = 200
rstation = 6
dstation = 70



for station in stationsL:
  if station != stationsL[-1]:
    canvas.create_line(xs, ys, xs + dstation, ys, fill = 'maroon')
  canvas.create_oval(xs - rstation, ys - rstation, xs + rstation, ys + rstation, fill = 'maroon')
  canvas.create_text(xs, ys + 30, text = station, fill = 'maroon', font = ('Helvetica 6 bold'))
  xs = xs + dstation



xs = 330
ys = 40
rstation = 6
dstation = 70

for station in stationpL:
  if station != stationpL[-1]:
    canvas.create_line(xs, ys, xs, ys + dstation, fill = 'LightPink4')
  canvas.create_oval(xs - rstation, ys - rstation, xs + rstation, ys + rstation, fill = 'LightPink4')
  canvas.create_text(xs + 40, ys, text = station, fill = 'LightPink4', font = ('Helvetica 6 bold'))
  ys = ys + dstation


sLpL = stationsL  + stationpL
sLpL.remove('Flon')

canvas.create_text(30, 250, text='Start')
startstation = tk.StringVar()
dropstart = tk.OptionMenu(window, startstation, *  sLpL)
dropstart.place(x = 30, y = 270)

canvas.create_text(240, 250, text='End')
stopstation = tk.StringVar()
dropstop = tk.OptionMenu(window, stopstation, * sLpL)
dropstop.place(x = 240, y = 270)




button = tk.Button(text="Calculate Ticket Price", command = calculate)
button.pack()



farelabel = tk.Label(window, text='Price = ', font = ('Helvetica 12 bold'))
farelabel.pack() 
tk.mainloop()