
def scope_test():
    def localyaz():
        mesaj = "aaaaaaaaa"
        print("localspam",mesaj)
    
    def nonlocalyaz():
 
        mesaj = "bbbbbb"
        
    
    def globalyaz():
        global mesaj
        mesaj = "cccccccc"
        
mesaj="dddddd"
scope_test()
print(mesaj)
