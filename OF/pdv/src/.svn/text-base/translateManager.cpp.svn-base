#include "translateManager.h"

// SINGLETON initalizations
bool translateManager::instanceFlag = false;
translateManager* translateManager::single = NULL;

//--------------------------------------------------------------
translateManager* translateManager::getInstance()
{
    if(! instanceFlag)
    {
        single = new translateManager();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}
//--------------------------------------------------------------
translateManager::translateManager(){

}
//--------------------------------------------------------------
translateManager::~translateManager(){

}
//--------------------------------------------------------------

void translateManager::setup(){
	string file = "lang\\"+settingsManager::getInstance()->getLanguage()+".xml";
	xml.loadFile(file);
	int totalTerms = xml.getNumTags("term");
	for(int i=0;i<totalTerms;i++){
		string text = xml.getValue("term","",i);
		string id = xml.getAttribute("term","string","",i);
		std::transform(id.begin(), id.end(),id.begin(), ::tolower);
		translations[id] = text;
	}
}

//--------------------------------------------------------------

string translateManager::t(string word){
	std::transform(word.begin(),word.end(),word.begin(), ::tolower);
	string temp = "";
	if( translations.find(word) == translations.end() ){
		// not found
		cout << word+": Not found in dictonary of translated terms" << endl;
	}else{
		// found
		temp = translations[word];
	}
	return temp;
}