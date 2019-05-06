#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""

from socket import AF_INET,socket,SOCK_STREAM
from threading import Thread
import tkinter
import DES


iv = '2132435465768797'

def receive():
	"""Handles receiving messages."""
	while True:	
		try:
			msg = client_socket.recv(BUFSIZ).decode("utf8")	
			msg_list.insert(tkinter.END,msg)
			
		except OSError: #client may leave the chat
			break
		
			
def send(event=None):
	"""handles sending of messages"""
	msg = my_msg.get()
	my_msg.set("") #clears input
	l=make_chat_simple.get()
	if l == 1:
		msg = msg+"339907754822691632510668191263508344339\nThisi$atest"
		print(msg)
		client_socket.send(bytes(msg,"utf8"))
		print("this is %d" % l)
		
	elif l == 0:
		client_socket.send(bytes(msg,"utf8"))
		print(check)
	
	
	if msg == "{quit}":
		client_socket.close()
		top.quit()

def broadcast(msg, prefix=""):  # prefix is for name identification.
	"""Broadcasts a message to all the clients."""
	sock.send(bytes(prefix, "utf8")+msg)

		
		
def on_closing(event=None):
	"""time when window is closed"""
	my_msg.set("{quit}")
	send()
	
def decrypt():
	msg = my_decrypt.get()
	l = DES.decrypt(iv,KEY,msg)
	msg_list.insert(tkinter.END,l)
	
def on_click():
	l=make_chat_simple.get()
	
top = tkinter.Tk()
top.title("chat me")

messages_frame = tkinter.Frame(top)

my_msg = tkinter.StringVar() #message to be send
my_msg.set("type here")




scrollbar = tkinter.Scrollbar(messages_frame) # navigate




my_decrypt = tkinter.StringVar() #convert message
my_decrypt.set("")



#message frame
msg_list = tkinter.Listbox(messages_frame,height=15,width=50,yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
msg_list.pack()

messages_frame.pack()

make_chat_simple = tkinter.IntVar()
check = make_chat_simple.get()
check_box = tkinter.Checkbutton(top,variable=make_chat_simple, text="Make it plain chat",command=on_click)
check_box.pack()


#input field for user
entry_field = tkinter.Entry(top,textvariable=my_msg)
entry_field.bind("<Return>",send)
entry_field.pack()
send_button = tkinter.Button(top,text="Send",command=send)
send_button.pack()

#input 
entry_field = tkinter.Entry(top,textvariable=my_decrypt)
entry_field.bind("<Return>",send)
entry_field.pack()
send_button = tkinter.Button(top,text="Decrypt",command=decrypt)
send_button.pack()

top.protocol("WM_DELETE_WINDOW",on_closing)

HOST = '127.0.0.1'#input('Enter host: ')
PORT = 33000

if not PORT:
	PORT = 33000
else:
	PORT = int(PORT)


KEY = input("Insert the key to see the decerypted message: ")
BUFSIZ = 1024
ADDR = (HOST,PORT)
client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() #start GUI
		
