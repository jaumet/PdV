#include "guiManager.h"

// SINGLETON initalizations
bool guiManager::instanceFlag = false;
guiManager* guiManager::single = NULL;

//--------------------------------------------------------------
guiManager* guiManager::getInstance()
{
    if(! instanceFlag)
    {
        single = new guiManager();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}
//--------------------------------------------------------------
guiManager::guiManager(){

	ofAddListener(ofEvents.update, this, &guiManager::update);
	ofAddListener(ofEvents.draw, this, &guiManager::draw);

	ofAddListener(ofEvents.keyPressed, this, &guiManager::keyPressed);
	ofAddListener(ofEvents.mousePressed, this, &guiManager::mousePressed);
	ofAddListener(ofEvents.mouseDragged, this, &guiManager::mouseDragged);
	ofAddListener(ofEvents.mouseReleased, this, &guiManager::mouseReleased);
}
//--------------------------------------------------------------
guiManager::~guiManager(){
}
//--------------------------------------------------------------
void guiManager::setup(){
	ofxControlPanel::setBackgroundColor(simpleColor(30, 30, 60, 200));
	ofxControlPanel::setTextColor(simpleColor(240, 50, 50, 255));

	gui.loadFont("fonts/MONACO.TTF", 8);
	gui.setup("test cv", 0, 0, ofGetWidth(), 700);
	gui.addPanel("background subtraction example", 4, false);
	
	//--------- PANEL 1
	gui.setWhichPanel(0);

	gui.setWhichColumn(0);

	lister.listDir("videos/");
	gui.addFileLister("image lister", &lister, 200, 300);
	gui.addButtonSlider("Voting time(seconds)", "VOTING_TIME", 30.0, 1.0, 300.0, false);

	// SETTINGS AND EVENTS
	// Load from xml!
	gui.loadSettings("controlPanelSettings.xml");

	visible = false;
}
//--------------------------------------------------------------
void guiManager::update(ofEventArgs & args){
	gui.update();
}
//--------------------------------------------------------------
void guiManager::draw(ofEventArgs & args){
	if(visible) gui.draw();
}
//--------------------------------------------------------------
void guiManager::keyPressed(ofKeyEventArgs & args){
	gui.keyPressed( args.key );
}
//--------------------------------------------------------------
void guiManager::mouseDragged(ofMouseEventArgs & args){
	gui.mouseDragged(args.x, args.y, args.button);
}
//--------------------------------------------------------------
bool guiManager::getVisible(){
	return visible;
}
//--------------------------------------------------------------
void guiManager::setVisible(bool value){
	visible = value;
}
//--------------------------------------------------------------
void guiManager::toggleVisible(){
	visible = !visible;
}

//--------------------------------------------------------------
void guiManager::mousePressed(ofMouseEventArgs & args){
	gui.mousePressed(args.x, args.y, args.button);
}

//--------------------------------------------------------------
void guiManager::mouseReleased(ofMouseEventArgs & args){
	gui.mouseReleased();
}
//--------------------------------------------------------------
