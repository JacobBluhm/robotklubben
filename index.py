from make_dic import *
from Tkinter import *



maengde_window = Tk()
Vvar = StringVar()
Tvar = StringVar()
#Gaskonstanten
R = 8.31
molekyle,n,m,mol,v,T = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
densitet, tryk = StringVar(), StringVar()

choices_V = { 'L','dL','cL','mL'}
choices_T = { 'Kelvin','Celsius','Fahrenheit'}

 
popupMenu_V = OptionMenu(maengde_window, Vvar, *choices_V)
popupMenu_T = OptionMenu(maengde_window, Tvar, *choices_T)

popupMenu_V.grid(row=6,column=4)
popupMenu_T.grid(row=7,column= 4)
def change_dropdown_V(*args):
    #Return
    print( Vvar.get() )
def change_dropdown_T(*args):
    print( Tvar.get() )    
#Hvad goer .trace()?
Vvar.trace('w', change_dropdown_V)
Vvar.set('L ')

Tvar.trace('w', change_dropdown_T)
Tvar.set('Celsius ')
maengde_window.title("Nemt, inc.")
maengde_window.geometry("720x500+300+150")

Label(maengde_window,text ="Maengde (enheder)").grid(row=0,column=0)

Label(maengde_window,text ="Molekyle:").grid(row=1,column=0)
Label(maengde_window,text ="M").grid(row=1,column=2)

Label(maengde_window,text ="Masse:").grid(row=2,column=0)
Label(maengde_window,text =" g").grid(row=2,column=4)

Label(maengde_window,text ="Stofmaengde").grid(row=3,column=0)
Label(maengde_window,text =" mol").grid(row=3,column=4)

Label(maengde_window,text ="Molar masse").grid(row=4,column=0)
Label(maengde_window,text =" g/mol").grid(row=4,column=4)

Label(maengde_window,text ="Input").grid(row=0,column=3)
Label(maengde_window,text ="Resultater").grid(row=0,column=6)

Label(maengde_window,text ="Densitet").grid(row=5,column=0)
Label(maengde_window,text ="g/L").grid(row=5,column=4)

Label(maengde_window,text ="Volumen").grid(row=6,column=0)

Label(maengde_window,text ="Temperatur").grid(row=7,column=0)
#Skal den med?? ->
Label(maengde_window,text ="Koncentration (mol/L)").grid(row=8,column=0)
Label(maengde_window,text =" mol/L").grid(row=8,column=4)

Label(maengde_window,text ="Tryk ").grid(row=9,column=0)
Label(maengde_window,text =" pascal").grid(row=9,column=4)

mol_l = Entry(maengde_window, textvariable= mol,width = 10).grid(row=1,column =1)
molekyle_input = Entry(maengde_window, textvariable = molekyle, width = 15).grid(row= 1,column=3)

n_input = Entry(maengde_window, textvariable= n, width = 15).grid(row=2,column = 3) 
m_input = Entry(maengde_window, textvariable= m, width = 15).grid(row=3,column = 3)
densitet_input = Entry(maengde_window, textvariable= densitet, width= 15).grid(row=5,column =3)
V_input = Entry(maengde_window, textvariable= v, width= 15).grid(row=6,column =3)
temperatur_input = Entry(maengde_window, textvariable= T, width= 15).grid(row=7,column =3)
tryk_input = Entry(maengde_window, textvariable= tryk, width= 15).grid(row=9,column =3)

def is_empty(x):
    for i in range(len(x)):
        x[i].replace(" ", "")
        if(x[i] == ""):
            x[i] = 0
    return x
def calc(x):
    moll = float(x[0])
    m = float(x[2])
    n = float(x[3])
    p = float(x[4])
    V = float(x[5])
    temperatur = float(x[6])
    tryk = float(x[7])
    print("sfss",moll)
    if(moll == 0):
        moll = 1
    try:
        M = float(make_dic(x[1]))
    except:
        M = float(0)
    print(moll,"moll")
######################## Beregner n

    try:
        if(n == ""):
            n = m/M
    except ZeroDivisionError:
        n = 0
######################## Beregner m
    if(m != ""):
        m = m
    elif(n*M == 0):
        m = p*V
    elif(p*V == 0):
        m = n*M
    else:
        print(m)
######################## Beregner p

    try:
        p = m/V
    except ZeroDivisionError:
        p = 0

####################### Beregner koncentration
    Label(maengde_window, text = " "*60).grid(row = 4,column= 6)
    Label(maengde_window, text = " "*60).grid(row=2,column = 6 )
    Label(maengde_window, text = " "*60).grid(row = 3,column= 6)
    Label(maengde_window, text = " "*60).grid(row = 5,column= 6)

    Label(maengde_window, text = M).grid(row = 4,column= 6)
    Label(maengde_window, text = m).grid(row=2,column = 6)
    Label(maengde_window, text = n).grid(row = 3,column= 6)
    Label(maengde_window, text = p).grid(row = 5,column= 6)



def callback():
    #Variabler = molekyle,n,m,mol_l 
    data = list()
    in_mol_l = mol.get()            # 0
    in_molekyle = molekyle.get()    # 1 
    in_m = m.get()                  # 2
    in_n = n.get()                  # 3
    in_densitet = densitet.get()    # 4
    in_v = v.get()                  # 5
    in_temp = T.get()               # 6
    in_tryk = tryk.get()            # 7
    data.append(in_mol_l),data.append(in_molekyle), data.append(in_n), data.append(in_m),data.append(in_densitet),
    data.append(in_v), data.append(in_temp)
    data.append(in_tryk)
    a = is_empty(data)
    calc(a)
button = Button(maengde_window, text= "Beregn", command=callback).grid(row = 10,column = 3)

maengde_window.mainloop()
