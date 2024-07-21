import logging # you may want to log stuff as you go
from simulator import A, B # use these to identify between hosts A and B

class Pkt:

    def __init__(self):
        # do not change these attrs or the simulator will break
        self.seqnum = None
        self.checksum = None
        self.payload = ""

    def make_checksum(self):
        checksum_value = 0
        for i in self.payload:
            value = ord(i)
            checksum_value += value
            checksum_value += self.seqnum #checksum = ord of string + seqnum 
        return checksum_value


    def verify_checksum(self):
        sum = self.checksum
        for i in self.payload:
            num = ord(i)
            sum -= num
        sum -= self.seqnum #!!!!!!!!change once implement seqnums
        if sum == 0:
            return True
        else:
            return False

    def __str__(self):
        return ""

class RDT:

    def __init__(self, sim):
        self.sim = sim # you'll need this to interact with the simulator
        self.pkt = Pkt()
        self.timer_started = False

    def rdt_sendA(self, msg):
        #Called from layer 5 at A, it should transport the msg to B
        packet = Pkt()
        packet.seqnum = 0
        packet.payload = msg
        packet.checksum = packet.make_checksum()
        #SUDOPACKET FOR TIMEOUT
        self.pkt.seqnum = 0
        self.pkt.payload = msg
        self.pkt.checksum = packet.checksum
        self.sim.tolayer3(A, packet) # sender side call
        if self.timer_started == False:
            self.timer_started = True
            self.sim.start_timer(A, 5)
            
        print("SEND A: packet sent")
        #implement timer start

        

    def rdt_rcvA(self, pkt):
        # print("recv a")

        # print("\n checksum: " + str(pkt.checksum) + " ")
        # print("\n verified checksum: " + str(pkt.verify_checksum()))
        # """Called from layer 3 when a packet arrives for layer 4 at A."""

        if pkt.payload == "ACK":
            print("RCV A: ack received")
            #stop timer
            if self.timer_started == True:
                self.timer_started = False
                self.sim.stop_timer(A)
        
        if pkt.payload == "NACK":
            print("RCV A: nack recieved")
            #stop timer
            if self.timer_started == True:
                self.timer_started = False
                self.sim.stop_timer(A)
            #resend packet
            if self.timer_started == False:
                self.timer_started = True
                self.sim.start_timer(A, 5)
                self.sim.tolayer3(A, pkt)
            #restart timer

        else:
            print("RCV A: invalid payload")


    def timer_interruptA(self):
        """Called when A's timer goes off."""
        #send a starts recieve a stops this is the timout fucntion
        print("TIMER INTERRUPT: called")
        if self.timer_started == False:
            self.timer_started = True
            self.sim.start_timer(A, 5)
            self.sim.tolayer3(A,self.pkt)
        else:
            self.sim.tolayer3(A,self.pkt)


    def rdt_rcvB(self, pkt): #when recieve packet extract message
        """Called from layer 3 when a packet arrives for layer 4 at B."""
        print("RCV B: packet recieved")
        if pkt.verify_checksum(): #fix checksumming
            print("RCV B: checksum valid")


            #return ack
            ack = Pkt()
            ack.seqnum = 0
            ack.payload = "ACK"
            ack.checksum = ack.make_checksum()
            self.sim.tolayer3(B, ack)
            #send message
            msg = pkt.payload
            self.sim.tolayer5(B,msg)
            print("RCV B: ack sent")
        else:
            #return nack?
            print
            packet = Pkt()
            packet.seqnum = 0 #prev_seq + 1
            packet.payload = "NACK"
            packet.checksum = packet.make_checksum()
            self.sim.tolayer3(B, packet)
            print("RCV B: nack sent")
