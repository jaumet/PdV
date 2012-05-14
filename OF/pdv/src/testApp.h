#ifndef _TEST_APP
#define _TEST_APP

#define _WIN32_WINNT 0x0501
#include <windows.h>
#include <winuser.h>

#include "ofMain.h"
#include "ofxVirtualMouse.h"
#include "ofxVirtualKeyboard.h"
#include "ofxManagerWindows.h"
#include "guiManager.h"

#include "seatManager.h"
#include "screensManager.h"
#include "ofxTimer.h"
#include "votesManager.h"
#include "actionsManager.h"
#include "fontManager.h";

#include "screen.h"
#include "screen0.h"
#include "screen1.h"
#include "screen2.h"
#include "screen3.h"
#include "screenInfo.h"
#include <vector>

#include "OSCManager.h"	
#include "ofxMidi.h"
#include "callPythonScripts.h"
#include "exportPDF.h"

#include "ofxKeyAndMouseLogger.h"
#include "statusProgramLog.h"
#include "translateManager.h"
enum status{nonStatus=0,votingStatus=1,resultStatus=2};

class testApp : public ofBaseApp, public ofxMidiListener{

	public:
		void setup();
		void update();
		void draw();
		void exit();
		void keyPressed  (int key);
		void keyReleased(int key);
		void mouseMoved(int x, int y );
		void mouseDragged(int x, int y, int button);
		void mousePressed(int x, int y, int button);
		void mouseReleased(int x, int y, int button);
		void windowResized(int w, int h);
		// method receive Midi-In
		void newMidiMessage(ofxMidiEventArgs& eventArgs);
		void startTheater();
		void nextScreen();
		void backScreen();
		void updateScreenSelected(ofEventArgs &e);
	private:
		ofPoint windowPosition;
		vector<screen*> myscreens;
		
		seatManager mySeatManager;
		votesManager myVotesManager;
		int screenSelected;
		actionsManager myActionsManager;
		ofVideoGrabber grabber;
		
		exportPDF myExportPDF;
		bool showBlackScreen;
		bool showVizScreen;
		ofxMidiIn midiIn;
		OSCManager myOSCManager;
		status myStatus;
		
		//ofxKeyAndMouseLogger logger;
		//void loggerKeyPressed(ofKeyEventArgs& keyEvent);
		//void loggerMouseReleased(ofMouseEventArgs& keyEvent);

		screenInfo myScreenInfo;

		int pdfCounter;
		ofImage currentScreen;
		void saveScreenImageForPDF();
		void press_SunVote();

		statusProgramLog myLogger;
		bool midiButtonNext;
		bool midiButtonStart;
		float midiButtonNextLastPress;
		float midiButtonStartLastPress;

		ofSerial serial;
};

#endif
