class queue(object):
    try:
        from ami import AMIClient, SimpleAction, EventListener
	import random
    except:
        print 'You need to install asterisk-ami (pip install asterisk-ami) first!'
        exit()

    from time import sleep
    import os, sys

    def __init__(self, login='', secret='', address='', port='5038', queue=''):
        self.sys.stderr = self.os.devnull
	self.complited=False
        self.members = []
        self.queue = queue
        self.client = self.AMIClient(address=address, port=int(port))
        self.client.login(username=login, secret=secret)
	self.actID=str(self.random.randint(10000,30000))
        self.action = self.SimpleAction('QueueStatus', Queue=self.queue, ActionID=self.actID)
        self.client.add_event_listener(self.event_QueueMember, white_list=['QueueMember'])
	self.client.add_event_listener(self.event_QueueStatusComplete, white_list=['QueueStatusComplete'])
        self.resp = self.client.send_action(self.action)
        self.sleep(0.01)
	while not self.complited:
	    sleep(0.01)
        self.client.logoff()
        self.free()
	self.agents=len(self.members)
	

    def event_QueueStatusComplete(self,event,**kwargs):
	if event.keys['ActionID']==self.actID: self.complited=True

    def event_QueueMember(self, event, **kwargs):
        self.members.append(event.keys)

    def free(self):
	self.freeagents = 0
        for member in self.members:
	    if member['Status'] == '1' and member['InCall']=='0' and member['Paused']== '0' and member['ActionID']==self.actID:
		
                self.freeagents += 1
	return self.freeagents
        
        


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 6:
	q=queue(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	print q.agents
	print q.freeagents
        q=None
    else:
        print 'Usage: python queueami.py ami_login ami_pass ami_host ami_port queue'
