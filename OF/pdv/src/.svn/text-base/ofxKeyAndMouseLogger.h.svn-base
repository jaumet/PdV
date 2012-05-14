#pragma once

#include "ofMain.h"
#include "ofThread.h"

class ofxKeyAndMouseLogger : ofThread {
public:
	ofxKeyAndMouseLogger();
	ofEvent<ofKeyEventArgs> keyPressed, keyReleased;
	ofEvent<ofMouseEventArgs> mousePressed, mouseReleased, mouseMoved;
protected:
	void sendKeyPress(int key);
	void sendKeyRelease(int key);
	void sendMousePress(int x, int y, int button);
	void sendMouseRelease(int x, int y, int button);
	void sendMouseMove(int x, int y);
	void threadedFunction();

	#ifdef TARGET_WIN32
	char
		keyStates[256],
		prevKeyStates[256],
		asyncKeyStates[256],
		prevAsyncKeyStates[256];
	bool ready;
	int mousePos[2];

	char
		mouseStates,
		prevMouseStates,
		asyncMouseStates,
		prevAsyncMouseStates;

	int virtualKeyToOF(int key, WORD buffer[]);
	#endif
};
