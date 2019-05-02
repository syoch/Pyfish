import socket
class PyFish():
    socket_instance=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    head_set =bytes.fromhex('03')
    head_dump=bytes.fromhex('04')
    debug=0
    def debuglog(self,data):
        if self.debug==1:
            print("debug ",data)
    def __init__(self,ip,port,debug):
        self.debug=debug
        self.debuglog("connecting "+ip+":"+str(port))
        self.socket_instance.connect((ip,port))
    def poke(self,addr,value):
        memory_send=addr+value
        print(memory_send)
        memory_sendb=bytes.fromhex(memory_send)
        #poke
        self.socket_instance.send(self.head_set)
        self.socket_instance.send(memory_sendb)
    def peek(self,addr):
        if addr=="0":
            print("can't access Null(0)")
        self.debuglog("peek address "+addr)
        memory_start=hex(int(addr,16)+0)[2:]
        memory_end  =hex(int(addr,16)+4)[2:]
        memory_send =memory_start+memory_end
        memory_sendb=bytes.fromhex(memory_send)

        #peek
        self.socket_instance.send(self.head_dump)
        self.socket_instance.send(memory_sendb)
        self.socket_instance.settimeout(3)

        data=self.socket_instance.recv(1024)
        self.debuglog("   data "+data.hex())
        
        req=data.hex()[2::]
        self.debuglog("hexdata "+req)
        return int(req,16)
    def pointer_poke(self,addr,value,*offset):
        print(offset)
        for i in offset:
            if(int(addr,16)>0x500000000):
                print("wiiu freeze auto about function")
                return -1
            self.debuglog("offset"+str(i))
            self.debuglog(type(i))
            a=self.peek(addr)+i
            addr=hex(a)[2:]
        self.poke(addr,value)
        self.debuglog("wrieteing addres "+addr)
    def pointer_peek(self,addr,*offset):
        print(offset)
        for i in offset:
            if(int(addr,16)>0x500000000):
                print("wiiu freeze auto about function")
                return -1
            self.debuglog("offset"+str(i))
            self.debuglog(type(i))
            a=self.peek(addr)+i
            addr=hex(a)[2:]
        return self.peek(addr)
gecko=PyFish("192.168.3.3",7331,1)