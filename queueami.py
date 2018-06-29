
class queue(object):
    try:
        from ami import AMIClient, SimpleAction, EventListener
    except:
        print 'You need to install asterisk-ami (pip install asterisk-ami) first!'
        exit()

    from time import sleep
    import os, sys

    def __init__(self, login='', secret='', address='', port='5038', queue=''):
        self.sys.stderr = self.os.devnull
        self.members = []
        self.queue = queue
        self.client = self.AMIClient(address=address, port=int(port))
        self.client.login(username=login, secret=secret)
        self.action = self.SimpleAction('QueueStatus', Queue=self.queue)
        self.client.add_event_listener(self.event_listener, white_list=['QueueMember'])
        self.resp = self.client.send_action(self.action)
        self.sleep(0.1)
        self.resp.response
        self.client.logoff()
        self.free()
	self.agents=len(self.members)

    def event_listener(self, event, **kwargs):
        self.members.append(event.keys)

    def free(self):
        self.freeagents = 0
        for member in self.members:
	    if member['Status'] == '1' and member['InCall']==0 and member['Paused']== '0':
                self.freeagents += 1

        
        


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 6:
	print queue(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]).agents
        print queue(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]).freeagents
    else:
        print 'Usage: ami.py ami_login ami_pass ami_host ami_port queue'

