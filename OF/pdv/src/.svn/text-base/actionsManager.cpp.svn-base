#include "actionsManager.h"

actionsManager::actionsManager(){

}

actionsManager::~actionsManager(){

}

void actionsManager::setup(){
	loadAction("automatizations/startVotation.xml");
	loadAction("automatizations/endVotation.xml");
}

void actionsManager::loadAction(string file){
	xml.loadFile(file);
	xml.pushTag("action");
	int totalActions = xml.getNumTags("subAction");
	action tempAction;
	int posInit = file.rfind('/')+1;
	int posEnd = file.rfind('.');
	tempAction.name = file.substr(posInit,posEnd-posInit);
	tempAction.filename = file;
	for(int i=0;i<totalActions;i++){
		actionItem tempActionItem;
		string type = xml.getValue("subAction:type","",i);
		if(type=="mouse"){
			tempActionItem.type = mouseEvent; 
			tempActionItem.x = ofToInt(xml.getValue("subAction:x","",i));
			tempActionItem.y = ofToInt(xml.getValue("subAction:y","",i));
		}else if(type=="key"){
			tempActionItem.type = keyEvent; 
			tempActionItem.keys = xml.getValue("subAction:keys","",i);
		}
		tempActionItem.sleep = xml.getValue("subAction:sleep",0.0f,i);
		tempAction.actionList.push_back( tempActionItem);
	}
	xml.popTag();
	actionsList[tempAction.name] = tempAction;
}

void actionsManager::playAction(string file){
	vector<actionItem> tempActionList = actionsList[file].actionList;
	for(int i=0;i<tempActionList.size();i++){
		if(tempActionList[i].type==mouseEvent){
			ofxVirtualMouse::getInstance()->sendMouseDownAndUp(tempActionList[i].x,tempActionList[i].y);
			cout << "press mouse x:" << tempActionList[i].x  << " y:"<<tempActionList[i].y << endl;
		}else if(tempActionList[i].type==keyEvent){
			ofxVirtualKeyboard::getInstance()->sendKey((const char)tempActionList[i].keys.c_str());
			//cout << "press key" << tempActionList[i].keys << endl;
		}
		if(tempActionList[i].sleep>0) Sleep(tempActionList[i].sleep*1000);
	}
}