#include "OSCManager.h"

OSCManager::OSCManager(){
	myOfxOscSender.setup("127.0.0.1",12000);
}

OSCManager::~OSCManager(){
	
}

void OSCManager::startVoting(){
	ofxOscMessage m;
	m.setAddress( "/startVoting" );
	myOfxOscSender.sendMessage( m );
}