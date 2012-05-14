#define _WIN32_WINNT 0x0501
#include <windows.h>
#include <winuser.h>

#include "ofMain.h"
#include "testApp.h"
#include "ofAppGlutWindow.h"
#include <assert.h>
	
#include <stdio.h>




//========================================================================
int main( ){
    ofAppGlutWindow window;
	ofSetupOpenGL(&window, 666+1024,768, OF_WINDOW);			// <-------- setup the GL context
	window.setWindowTitle("PdV_OF");  
   
	// this kicks off the running of my app
	// can be OF_WINDOW or OF_FULLSCREEN
	// pass in width and height too:
	ofRunApp( new testApp());
}
//========================================================================

