from tkinter import *
from tkinter import ttk

# from request_packet import tcp
import request_packet as rp
from datetime import datetime

root = Tk()
root.title("PACKET SENDER")

#frame creation
frame = LabelFrame(root, padx= 5, pady = 5)
frame.pack(padx = 10, pady = 10)

#packet name textbox
PN = Entry(frame, bg = "black", fg = "white", width = 100)
PN.pack()
PN.insert(0, "Packet Name: ")

#ascii textbox 
add_ascii = Entry(frame, bg = "grey", width = 100)
add_ascii.pack()
add_ascii.insert(1, "ASCII: ")

#hexadecimal textbox  
add_hex = Entry(frame, bg = "grey", width = 100)
add_hex.pack()
add_hex.insert(2, "Hexa-Decimal: ")

#ip address textbox
add_IP = Entry(frame, bg = "grey", width = 100)
add_IP.pack()
add_IP.insert(3, "Address:")

#port textbox
add_port = Entry(frame, bg = "grey", width = 100)
add_port.pack()
add_port.insert(3, "Port No.:")

#path textbox
add_path = Entry(frame, bg = "grey", width = 100)
add_path.pack()
add_path.insert(3, "Path:")

#data textbox
add_data = Entry(frame, bg = "grey", width = 100)
add_data.pack()
add_data.insert(3, "Data:")


def send_packet():
    packetName = PN.get()
    asciiName = add_ascii.get()
    hexValue = add_hex.get()
    ipValue = add_IP.get()
    portValue = add_port.get()
    pathValue = add_path.get()
    dataValue = add_data.get()
    dropDownValue = clicked.get()


    # print(f"{packetName} {asciiName} {hexValue} {ipValue} {portValue} {dropDownValue}")
    if dropDownValue=="TCP":
        result = rp.tcp(ipValue,int(portValue))
        print(result)
        my_tree.insert(parent ='',index=0,values=(str(datetime.now()).split(" ")[1].split(".")[0],result[0],result[1],ipValue,portValue,'TCP',result[2],result[3]))

    elif dropDownValue=="UDP":
        rp.udp(host=ipValue,port=int(portValue))
        # result = rp.udp(host=ipValue,port=int(portValue))
        # print(f"Result: {result}")
        my_tree.insert(parent ='',iid=1,index=0,values=(str(datetime.now()).split(" ")[1].split(".")[0],result[0],result[1],ipValue,portValue,'UDP',result[2],result[3]))

    elif dropDownValue=="SSL":
        rp.ssl(host=ipValue,port=int(portValue))

    elif dropDownValue=="HTTP GET":
        result = rp.httpGet(host=ipValue)
        my_tree.insert(parent ='',index=0,values=(str(datetime.now()).split(" ")[1].split(".")[0],result[0],result[1],ipValue,portValue,'HTTP GET',result[2],result[3]))

    elif dropDownValue=="HTTPS GET":
        result = rp.httpsGet(host=ipValue)
        my_tree.insert(parent ='',index=0,values=(str(datetime.now()).split(" ")[1].split(".")[0],result[0],result[1],ipValue,portValue,'HTTPS GET',result[2],result[3]))

    elif dropDownValue=="HTTP POST":
        result = rp.httpPost(host=ipValue,path=pathValue,data=dataValue)
        my_tree.insert(parent ='',index=0,values=(str(datetime.now()).split(" ")[1].split(".")[0],result[0],result[1],ipValue,portValue,'HTTP POST',result[2],result[3]))

    elif dropDownValue=="HTTPS POST":
        result = rp.httpsPost(host=ipValue,path=pathValue,data=dataValue)
        my_tree.insert(parent ='',index=0,values=(str(datetime.now()).split(" ")[1].split(".")[0],result[0],result[1],ipValue,portValue,'HTTPS POST',result[2],result[3]))

#send button
sendButton = Button(frame, text = "SEND", fg= "black", command=send_packet).pack()#add send function
# sendButton = Button(frame, text = "SEND", fg= "black").pack()#add send function
# sendButton.pack()



#drop button for method
clicked = StringVar()
clicked.set("TCP")

drop = OptionMenu(frame, clicked, "TCP","UDP","SSL","HTTP GET","HTTP POST","HTTPS GET","HTTPS POST")
drop.pack()



#-------------------second window--------------------------

#frame creation
frame1 = LabelFrame(root, padx= 15, pady = 15)
frame1.pack(padx = 20, pady = 20)

my_tree = ttk.Treeview(frame1)
#define coloumns
my_tree['columns'] = ("Time", "From IP", "From Port", "To Address", "To Port", "Method", "ASCII","Hexa-Decimal")
#Formate coloumns
my_tree.column("#0", width = 50)
my_tree.column("Time", anchor = W, width = 120)
my_tree.column("From IP", anchor = W, width = 120)
my_tree.column("From Port", anchor = W, width = 120)
my_tree.column("To Address", anchor = CENTER, width = 120)
my_tree.column("To Port", anchor = W, width = 120)
my_tree.column("Method", anchor = W, width = 120)
my_tree.column("ASCII", anchor = W, width = 120)
my_tree.column("Hexa-Decimal", anchor = W, width = 120)

#HEADINGS
my_tree.heading("#0", text = "Serial No", anchor = W)
my_tree.heading("Time", text = "Time", anchor = W)
my_tree.heading("From IP", text = "From IP", anchor = W)
my_tree.heading("From Port", text = "From Port", anchor = W)
my_tree.heading("To Address", text = "To Address", anchor = CENTER)
my_tree.heading("To Port", text = "To Port", anchor = W)
my_tree.heading("Method", text = "Method", anchor = W)
my_tree.heading("ASCII", text = "ASCII", anchor = W)
my_tree.heading("Hexa-Decimal", text = "Hexa-Decimal", anchor = W)

#----------------------------ADD DATA----------------------------------

my_tree.pack(pady = 20)
root.mainloop()