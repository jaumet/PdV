#include "ofxKeyAndMouseLogger.h"

ofxKeyAndMouseLogger::ofxKeyAndMouseLogger() {
	startThread(true, false);

	#ifdef TARGET_WIN32
	ready = false;
	#endif
}

void ofxKeyAndMouseLogger::sendMousePress(int x, int y, int button) {
	ofMouseEventArgs mousePress;
	mousePress.x = x;
	mousePress.y = y;
	mousePress.button = button;
	ofNotifyEvent(mousePressed, mousePress);
}

void ofxKeyAndMouseLogger::sendMouseRelease(int x, int y, int button) {
	ofMouseEventArgs mouseRelease;
	mouseRelease.x = x;
	mouseRelease.y = y;
	mouseRelease.button = button;
	ofNotifyEvent(mouseReleased, mouseRelease);
}

void ofxKeyAndMouseLogger::sendMouseMove(int x, int y) {
	ofMouseEventArgs mouseMove;
	mouseMove.x = x;
	mouseMove.y = y;
	ofNotifyEvent(mouseMoved, mouseMove);
}

void ofxKeyAndMouseLogger::sendKeyPress(int key) {
	ofKeyEventArgs keyPress;
	keyPress.key = key;
	ofNotifyEvent(keyPressed, keyPress);
}

void ofxKeyAndMouseLogger::sendKeyRelease(int key) {
	ofKeyEventArgs keyRelease;
	keyRelease.key = key;
	ofNotifyEvent(keyReleased, keyRelease);
}

void ofxKeyAndMouseLogger::threadedFunction() {
	while( isThreadRunning() != 0 ){

		#ifdef TARGET_WIN32
		lock();
		// load all key states. uses both normal and async
		// because async is more accurate  and includes
		// repeated keys, while normal gives direction.
		// http://msdn.microsoft.com/en-us/library/ms646293(VS.85).aspx
		for (unsigned int key = 0; key < 256; key++) {
			keyStates[key] = GetKeyState(key);
			asyncKeyStates[key] = GetAsyncKeyState(key);
		}

		// check for changes and send updates
		for (unsigned int key = 0; key < 256; key++) {
			char curKeyState = keyStates[key];
			char curAsyncKeyState = asyncKeyStates[key];
			bool changed =
				curKeyState != prevKeyStates[key] ||
				curAsyncKeyState != prevAsyncKeyStates[key];
			if(ready && changed) {
				bool keyDown = 0x80 & curKeyState;
				bool repeat = !(0x01 & curAsyncKeyState);
				WORD buffer[2] = {0, 0};
				int bufferSize = ToAscii(key, 0, (PBYTE) keyStates, buffer, 0);
				int translated = virtualKeyToOF(key, buffer);
				if(translated != 0)
					if(keyDown && !repeat)
						sendKeyPress(translated);
					else if(!keyDown)
						sendKeyRelease(translated);
				/*
				// there is a lot more happening than this code reports,
				// uncomment this printf to see what else is detectable.
				printf("%i: ToAscii={%x, %x}[%i], dir=%i, repeat=%i\n",
					key, buffer[0], buffer[1], bufferSize, keyDown, repeat);
				*/
			}
			prevKeyStates[key] = curKeyState;
			prevAsyncKeyStates[key] = curAsyncKeyState;
		}

		// mouse events

		POINT p;
		GetCursorPos(&p);
		//cout <<"Get position x:"<< p.x <<" y:"<< p.y << endl;
			
		// DETECT MOUSE MOVE EVENT
		
		if( mousePos[0]!=NULL && ( mousePos[0] != p.x || mousePos[1] != p.y) ){
			sendMouseMove(p.x, p.y);
		}
		mousePos[0] = p.x; 
		mousePos[1] = p.y; 
		
		
		// DETECT MOUSE EVENTS
		mouseStates = GetKeyState(VK_LBUTTON);
		asyncMouseStates = GetAsyncKeyState(VK_LBUTTON);

		char curMouseState = mouseStates;
		char curAsyncMouseState = asyncMouseStates;
		bool changed =
				curMouseState != prevMouseStates ||
				curAsyncMouseState != prevAsyncMouseStates;

		if(ready && changed){
			bool keyDown = 0x80 & curMouseState;
			bool repeat = !(0x01 & curAsyncMouseState);
			if( keyDown && !repeat ){
				sendMousePress(p.x, p.y, 0);
				//cout << "Mouse_Pressed" << endl;
			}else if(!keyDown){
				sendMouseRelease(p.x, p.y, 0);
				//cout << "Mouse_Release" << endl;
			}

		}
		prevMouseStates = curMouseState;
		prevAsyncMouseStates = curAsyncMouseState;

		/*
		if(GetSystemMetrics(SM_SWAPBUTTON)){
			cout << "Has swapped mouse buttons" << endl;
		}
		*/

		ready = true;
		unlock();
		#endif

		// on windows:
		// 1 ms: tons of cpu usage, everything is in order
		// 10 ms: less cpu usage, some out of order keys
		// 100 ms: much less cpu usage, repeated keys are missed
		ofSleepMillis(10);
	}
}

#ifdef TARGET_WIN32
int ofxKeyAndMouseLogger::virtualKeyToOF(int key, WORD buffer[]) {
	switch(key) {
		case VK_F1: return OF_KEY_F1; break;
		case VK_F2: return OF_KEY_F2; break;
		case VK_F3: return OF_KEY_F3; break;
		case VK_F4: return OF_KEY_F4; break;
		case VK_F5: return OF_KEY_F5; break;
		case VK_F6: return OF_KEY_F6; break;
		case VK_F7: return OF_KEY_F7; break;
		case VK_F8: return OF_KEY_F8; break;
		case VK_F9: return OF_KEY_F9; break;
		case VK_F10: return OF_KEY_F10; break;
		case VK_LEFT: return OF_KEY_LEFT; break;
		case VK_UP: return OF_KEY_UP; break;
		case VK_RIGHT: return OF_KEY_RIGHT; break;
		case VK_DOWN: return OF_KEY_DOWN; break;
		case VK_PRIOR: return OF_KEY_PAGE_UP; break;
		case VK_NEXT: return OF_KEY_PAGE_DOWN; break;
		case VK_HOME: return OF_KEY_HOME; break;
		case VK_END: return OF_KEY_END; break;
		case VK_INSERT: return OF_KEY_INSERT; break;
	}
	return buffer[0];
}
#endif
