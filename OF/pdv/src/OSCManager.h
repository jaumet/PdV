// ***********************************************************************
// This class is to comunicated to sound programming done in superCollider
// ***********************************************************************
#ifndef _OSC_MANAGER_
#define _OSC_MANAGER_

#include "ofMain.h"
#include "ofxOSC.h"

class OSCManager{
public:
	OSCManager();
	~OSCManager();
	void startVoting();
private:
	ofxOscSender myOfxOscSender;
	
};

#endif