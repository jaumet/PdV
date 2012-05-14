#include "testApp.h"



//--------------------------------------------------------------
void testApp::setup(){
	settingsManager::getInstance()->setup();
	translateManager::getInstance()->setup();
	fontManager::getInstance()->setup();

	windowPosition.x = settingsManager::getInstance()->getScreenPositionX();
	windowPosition.y = 0;
	screenSelected = 0;

	screen0* myScreen0 = new screen0();
	myScreen0->setup();
	myscreens.push_back(myScreen0);

	screen1* myScreen1 = new screen1();
	myScreen1->setup();
	myscreens.push_back(myScreen1);

	screen2* myScreen2 = new screen2();
	myScreen2->setup();
	myscreens.push_back(myScreen2);

	screen3* myScreen3 = new screen3();
	myScreen3->setup();
	myscreens.push_back(myScreen3);
	/*
	screen4* myScreen4 = new screen4();
	myScreen4->setup();
	myscreens.push_back(myScreen4);
	*/
	myScreenInfo.setup();

	screensManager::getInstance()->setup();
	
	int totalSeats = seatManager::getInstance()->getTotalSeats();
	seatManager::getInstance()->setup();
	totalSeats = seatManager::getInstance()->getTotalSeats();
	
	votesManager::getInstance()->setup();
	myActionsManager.setup();
	
	// set windows not decorated
	ofxManagerWindows::getInstance()->setWindowWithNoDecorated("PdV_OF");

	grabber.initGrabber(320, 240);
	guiManager::getInstance()->setup();

	//MidiIn
	midiIn.listPorts();
	midiIn.openPort(0);
	midiIn.addListener(this);

	unsigned char a = midiIn.getPort();
	midiButtonNextLastPress = ofGetElapsedTimeMillis();
	midiButtonStartLastPress = ofGetElapsedTimeMillis();
	midiButtonStart = false;
	midiButtonNext = false;
	showBlackScreen = false;

	ofAddListener(votesManager::getInstance()->nextScreenEvent,this,&testApp::updateScreenSelected);
	showVizScreen = false;

	// PDF <--------------------------------------------------->
	pdfCounter = 0;

	// Setup SERIAL port - define in XML-File
	myScreenInfo.arduinoMouseConnected = serial.setup(settingsManager::getInstance()->getComPortName(),9600);	
}
//--------------------------------------------------------------

void testApp::update(){
	ofSetWindowPosition(windowPosition.x , windowPosition.y); 
	myscreens[screenSelected]->update();
	
	if(midiButtonStart && (ofGetElapsedTimeMillis()-midiButtonStartLastPress)>3000 ){
		midiButtonStartLastPress = ofGetElapsedTimef();
		midiButtonStart = false;
		startTheater();
	}

	if(midiButtonNext && (ofGetElapsedTimeMillis()-midiButtonNextLastPress)>3000 ){
		midiButtonNextLastPress = ofGetElapsedTimef();
		midiButtonNext = false;
		nextScreen();
	}
}

//--------------------------------------------------------------

void testApp::draw(){
	// Pantalles 1 
	myScreenInfo.draw(0,0);

	// Pantalles 2 projector
	myscreens[screenSelected]->draw(666,0);//200
	currentScreen.grabScreen(666,0,1024,768);
	// for debug
	currentScreen.draw(10,300,1024/1.7,768/1.7);
}

//--------------------------------------------------------------
void testApp::keyPressed(int key){
	// SPACE: Next screen
	// Show GUI to configure things

	if(settingsManager::getInstance()->getDebugMode() && key=='1'){
		seatManager::getInstance()->setAllSeatsYes();
	}

	if(settingsManager::getInstance()->getDebugMode() && key=='2'){
		seatManager::getInstance()->setAllSeatsNo();
	}

	// "S": Start voting
	if(key=='s'){
		startTheater();
	}

	// Next voting
	if(key=='n'){
		nextScreen();
	}

	// Pause
	if(key=='p'){
		votesManager::getInstance()->setPauseTimer();
	}

	// Reconect midi
	if(key=='m'){
		midiIn.openPort(0);
	}

	// Black screen
	if(key=='b'){
		showBlackScreen = !showBlackScreen;
	}
}

//--------------------------------------------------------------
void testApp::keyReleased(int key){

}

//--------------------------------------------------------------
void testApp::mouseMoved(int x, int y ){
	// Safety feature to not have the cursor appear in the screen 
	if(x>666){
		ofHideCursor();
	}else{
		ofShowCursor();
	}
}

//--------------------------------------------------------------
void testApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void testApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void testApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void testApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void testApp::newMidiMessage(ofxMidiEventArgs& eventArgs) {
	myScreenInfo.midiConnected = true;

	// Midi debug
	if(settingsManager::getInstance()->getDebugMode()){
		cout <<"MidiIn debug message" << endl;
		cout <<"1. keypressed Number:"<< (int)eventArgs.byteOne<< endl;
		cout <<"2. Value2:"<< (int)eventArgs.byteTwo<< endl;
		cout <<"3. id:"<< eventArgs.channel<< endl;
		cout <<"4. port:"<< eventArgs.port<< endl;
		cout <<"5. timestamp:"<<eventArgs.timestamp<< endl;
	}
	
	// Pause time
	if( eventArgs.byteOne== settingsManager::getInstance()->getMidikeyPauseKey() && eventArgs.byteTwo==settingsManager::getInstance()->getMidikeyPauseValue() ){
		cout << "Press Pause time MIDI!" << endl;	
		votesManager::getInstance()->setPauseTimer();
	}

	// Next screen
	if( eventArgs.byteOne== settingsManager::getInstance()->getMidikeyNextKey() && eventArgs.byteTwo==settingsManager::getInstance()->getMidikeyNextValue() ){
		cout << "Press Next screen MIDI!" << endl;	
		midiButtonNext = true;
	}

	// Start theater
	if( eventArgs.byteOne== settingsManager::getInstance()->getMidikeyStartKey() && eventArgs.byteTwo==settingsManager::getInstance()->getMidikeyStartValue() ){
		cout << "Press Start performance MIDI!" << endl;	
		midiButtonStart = true;
	}
}
//--------------------------------------------------------------
void testApp::startTheater(){
	
	if(!votesManager::getInstance()->getStartPerformance()){
		// Load all screens again
		screensManager::getInstance()->load();
		votesManager::getInstance()->setStartPerformance();
		nextScreen();
		if(ofToInt(screensManager::getInstance()->getScreenId())>1){
			int id = votesManager::getInstance()->lastStoredScreenShowed();
			votesManager::getInstance()->setVotationID(id);
		}
	}   
}

//--------------------------------------------------------------
void testApp::nextScreen(){
	
	if(votesManager::getInstance()->getStartPerformance()){
		// save screen
		saveScreenImageForPDF();

		if( myStatus == resultStatus ){
			votesManager::getInstance()->nextScreen();	
		}
		string typeScreen = screensManager::getInstance()->getScreenType();
		int id = screensManager::getInstance()->getSelectedScreen();
		// 1)QUESTION
		if( typeScreen=="question" && myStatus == votingStatus ){
			myStatus = resultStatus;
			myscreens[screenSelected]->unload();
			screenSelected = 2;
			
			// end votation
			press_SunVote();
			// call python script
			callPythonScripts::getInstance()->callScript("mdb2tsv.py");
			callPythonScripts::getInstance()->callScript(screensManager::getInstance()->getScreenScript());
			// load map.xml export by python script
			seatManager::getInstance()->loadFile();			
			myscreens[screenSelected]->load();
		}else if( typeScreen=="question" ){
			// start votation
			press_SunVote();
	
			myStatus = votingStatus;
			myscreens[screenSelected]->unload();
			screenSelected = 1;
			myscreens[screenSelected]->load();
			// Virtual key and mouse 
		}

		// 2)DEBATE
		if( typeScreen=="debate" && myStatus == votingStatus ){
			myStatus = resultStatus;
			myscreens[screenSelected]->unload();
			screenSelected = 2;
			votesManager::getInstance()->closeAllTimers();
			// end votation
			press_SunVote();
			// call python script
			callPythonScripts::getInstance()->callScript("mdb2tsv.py");
			callPythonScripts::getInstance()->callScript(screensManager::getInstance()->getScreenScript());
			// load map.xml export by python script
			seatManager::getInstance()->loadFile();
			myscreens[screenSelected]->load();
		}else if( typeScreen=="debate" ){
			// start votation
			press_SunVote();

			//votesManager::getInstance()->prepareDebate();

			myStatus = votingStatus;
			myscreens[screenSelected]->unload();
			screenSelected = 1;
			seatManager::getInstance()->loadFile();
			myscreens[screenSelected]->load();
		}

		// 3)TEXT
		if( typeScreen=="text"){
			callPythonScripts::getInstance()->callScript(screensManager::getInstance()->getScreenScript());
			seatManager::getInstance()->loadFile();
			myStatus = resultStatus;
			myscreens[screenSelected]->unload();
			screenSelected = 3;
			myscreens[screenSelected]->load();
		}
		
		// 4)STATEMENT
		if( typeScreen=="statement"){
			if(screensManager::getInstance()->getScreenScript()!=""){
				callPythonScripts::getInstance()->callScript(screensManager::getInstance()->getScreenScript());
			}
			seatManager::getInstance()->loadFile();
			myStatus = resultStatus;
			myscreens[screenSelected]->unload();
			screenSelected = 3;
			myscreens[screenSelected]->load();
		}

	}
}

//--------------------------------------------------------------
void testApp::updateScreenSelected(ofEventArgs &e){
	nextScreen();
}

//--------------------------------------------------------------
/*
void testApp::loggerKeyPressed(ofKeyEventArgs& keyEvent) {
	char key = (char)keyEvent.key;
	cout << "press Key:" << key << endl;
}


void testApp::loggerMouseReleased(ofMouseEventArgs& mouseEvent) {
	cout << "Press Key x:" << mouseEvent.x<< " y:" << mouseEvent.y << endl;
}
*/
void testApp::exit(){
	//logger.stopThread();
	serial.close();
}

void testApp::saveScreenImageForPDF(){
	// save image
	string counter = ofToString(pdfCounter);
	if(counter.length()==1) counter = "00"+counter;
	if(counter.length()==2) counter = "0"+counter;
	currentScreen.saveImage(settingsManager::getInstance()->getDataPath()+"png_export_export\\pdv_"+counter+".png"); 
	pdfCounter++;
}

void testApp::press_SunVote(){
	// move mouse
	ofVec2f buttonPos = settingsManager::getInstance()->getPositionStartButtonSunVote();
	SetCursorPos(buttonPos.x,buttonPos.y);

	// move mouse 2 change
	double fScreenWidth    = ::GetSystemMetrics( SM_CXSCREEN )-1; 
	double fScreenHeight  = ::GetSystemMetrics( SM_CYSCREEN )-1; 
	double fx = buttonPos.x*(65535.0f/fScreenWidth);
	double fy = buttonPos.y*(65535.0f/fScreenHeight);

	// mouse
	INPUT  input={0};
	input.type = INPUT_MOUSE;
	input.mi.mouseData = 0;
	input.mi.dx = fx;
	input.mi.dy = fy;

	input.mi.dwFlags  = MOUSEEVENTF_MOVE|MOUSEEVENTF_ABSOLUTE;
	::SendInput(1,&input,sizeof(INPUT));

	// send this char to trigger the mousepress in arduino
	serial.writeByte('p');
	// sleep some time to recover from time to press
	Sleep(1500);
}



void keyPress(char c){
	KEYBDINPUT kb={0};
    INPUT Input={0};

    //keydown
    kb.wVk    =  0;/*enter unicode here VK_BACKSPACE*/
    kb.wScan = VkKeyScan(c);
    kb.dwFlags = KEYEVENTF_UNICODE; // KEYEVENTF_UNICODE=4
    Input.type = INPUT_KEYBOARD;
    Input.ki = kb;

    ::SendInput(1,&Input,sizeof(Input));

    //keyup
    kb.wVk    =  0;/*enter unicode here*/;
    kb.wScan = VkKeyScan(c);
    kb.dwFlags = KEYEVENTF_UNICODE|KEYEVENTF_KEYUP; //KEYEVENTF_UNICODE=4
    Input.type = INPUT_KEYBOARD;
    Input.ki = kb;

    int retval = ::SendInput(1,&Input,sizeof(Input));
	if(retval > 0) 
    { 
      _tprintf(_T("SendInput sent %i"), retval); 
    } 
    else 
    { 
      _tprintf(_T("Unable to send input commands. Error is: %i"), GetLastError()); 
    } 
}
  

void LeftClick (int x, int y )
{  
  double fScreenWidth    = ::GetSystemMetrics( SM_CXSCREEN )-1; 
  double fScreenHeight  = ::GetSystemMetrics( SM_CYSCREEN )-1; 
  double fx = x*(65535.0f/fScreenWidth);
  double fy = y*(65535.0f/fScreenHeight);

  // mouse
  INPUT  input={0};
  input.type = INPUT_MOUSE;
  input.mi.mouseData = 0;
  input.mi.dx = fx;
  input.mi.dy = fy;

   input.mi.dwFlags  = MOUSEEVENTF_MOVE|MOUSEEVENTF_ABSOLUTE;
  ::SendInput(1,&input,sizeof(INPUT));

  // left down 
  input.mi.dwFlags  = MOUSEEVENTF_LEFTDOWN;
  ::SendInput(1,&input,sizeof(INPUT));
  // left up
  input.mi.dwFlags  = MOUSEEVENTF_LEFTUP;
  ::SendInput(1,&input,sizeof(INPUT));
  
}