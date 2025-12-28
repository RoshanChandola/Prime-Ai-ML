#message class
class Message:
    message_counter=1
    def __init__(self,sender,content):
        self.sender=sender
        self.content=content
        self.id=Message.message_counter
        Message.message_counter+=1
        
        def __str__(self):
            return f"Message ID: {self.id}, Sender: {self.sender}, Content: {self.content}"
#user class

class User:
    def __init__(self,username):
        self.username=username
        self.chatroom=None
        
    def join_chatroom(self,chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
           chatroom.add_user(self)
           self.chatroom=chatroom
           print(f"{self.username} joined the chatroom.{chatroom.name}")
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left the chatroom.{self.chatroom.name}")
            self.chatroom=None
    def send_message(self,content):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom can't send any message.")
        else:
            self.chatroom.broadcast(self,content)
#chatroom class
class ChatRoom:
    def __init__(self,name):
        self.name=name
        self.users=[]
        self.messages=[]
        
    def add_user(self,user):
        self.users.append(user)
    def remove_user(self,user):
        self.users.remove(user)
    def broadcast(self,sender,content):
        message=Message(sender,content)
        self.messages.append(message)
        print(f"{sender.username} sent a message: {content}")
    def show_chat_history(self):
        print(f"Chat History for {self.name}:")
        for msg in self.messages:
            print(msg.content)
        print()
        
#example usage
if __name__=="__main__":
    room=ChatRoom("Python Lounge")
    
    user1=User("Roshan")
    user2=User("Amit")
    user3=User("Uday")
    user1.join_chatroom(room)
    user2.join_chatroom(room)
    user1.send_message("Hello everyone!")
    user2.send_message("Hi Roshan!")
    user3.join_chatroom(room)
    user3.send_message("Hey folks!")    
    user1.leave_chatroom()
    user3.send_message("Where did Roshan go?")  
    room.show_chat_history()
    user2.leave_chatroom()
    user3.leave_chatroom()
   