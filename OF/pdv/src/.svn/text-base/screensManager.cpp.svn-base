#include "screensManager.h"

// SINGLETON initalizations
bool screensManager::instanceFlag = false;
screensManager* screensManager::single = NULL;


//----------------------------------------------

screensManager* screensManager::getInstance()
{
    if(! instanceFlag)
    {
        single = new screensManager();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

screensManager::screensManager()
{

}

screensManager::~screensManager()
{

}

void screensManager::setup()
{
	load();
}

void screensManager::load()
{
	// init selected question
	selectedScreen = settingsManager::getInstance()->getIdStartScreen();
	lastSelectedScreen = 0;
	if(screens.size()>0)screens.erase(screens.begin(), screens.end());
	if(screensId.size()>0)screensId.erase(screensId.begin(), screensId.end());
	// Load questions
	xml.loadFile(settingsManager::getInstance()->getDataPath()+"allContent_"+settingsManager::getInstance()->getLanguage()+".xml");
	xml.pushTag("allContent");
	int totalScreens = xml.getNumTags("screen");
	for(int i=0;i<totalScreens;i++){
		// Data in all types
		string id = xml.getValue("screen:id","",i);	
		string content = xml.getValue("screen:content","",i);
		string type = xml.getValue("screen:type","",i); //type: question/debate/message
		string script = xml.getValue("screen:script","",i);
		
		int timePro = 90;
		int timeContra = 60;
		int time = xml.getValue("screen:time",0,i);
		if(time==0){ time = 5; } 
		string pro = xml.getValue("screen:pro","",i);
		string contra = xml.getValue("screen:contra","",i);
		string action = xml.getValue("screen:action","",i);
		string of =  xml.getValue("screen:of","",i);
		string dynamicTextMethod = xml.getValue("screen:dynamic-text-call-method","",i);

		screenData tempScreen;
		tempScreen.time = time;
		tempScreen.timePro = timePro;
		tempScreen.timeContra = timeContra;
		tempScreen.id = id;
		tempScreen.text = content;
		tempScreen.type = type;
		tempScreen.action = action;
		
		tempScreen.dynamicTextMethod = dynamicTextMethod;
		tempScreen.of = of;
		if(script=="" && (type=="question" || type=="debate") ){
			script = "votation_results.py "+id;
		}
		tempScreen.script = script;
		tempScreen.pro = pro;
		tempScreen.contra = contra;
		tempScreen.hasAudioFile = false;

		if(type=="text" || type=="statement"){
			int link = xml.getValue("screen:link",0,i);
			tempScreen.link = link;
		}

		// Check which type screen
		if(type=="debate" || type=="question" ){
			xml.pushTag("screen",i);
			xml.pushTag("answers");
			int totalAnswersScreens = xml.getNumTags("reply");
			for(int j=0;j<totalAnswersScreens;j++){
				int link = xml.getValue("reply:link",0,j);	
				string text = xml.getValue("reply:text","",j);	
				string statement = xml.getValue("reply:statement","",j);
				string audioFile = xml.getValue("reply:audio-file","",j);
				dynamicTextMethod = xml.getValue("reply:dynamic-text-call-method","",j);

				if(audioFile!="") tempScreen.hasAudioFile = true;
				answer tempAnswer;
				tempAnswer.text = text;
				tempAnswer.dynamicTextMethod = dynamicTextMethod;
				tempAnswer.link = link;
				tempAnswer.audioFile = audioFile;
				tempAnswer.statement = statement;
				tempScreen.answers.push_back(tempAnswer);
			}
			xml.popTag();
			xml.popTag();
		}
		
		int idScreen = ofToInt(tempScreen.id);
		screens[idScreen] = tempScreen;
		screensId.push_back( idScreen );
	}
	// Sort list
	sort(screensId.begin(),screensId.end());
	// Save in map the array ID
	for(int i=0;i<screensId.size();i++){
		screens[screensId[i]].arId = i; 
	}
	// Count how many screens every part
	countScreensPart1 = 0;
	for(int i=0;i<screensId.size();i++){
		if(screensId[i]<1000) countScreensPart1 += 1;
	}
	countScreensPart2 = 0;
	for(int i=0;i<screensId.size();i++){
		if(screensId[i]>1000 && screensId[i]<2000) countScreensPart2 +=1;
	}
	countScreensPart3 = 0;
	for(int i=0;i<screensId.size();i++){
		if(screensId[i]>=2000) countScreensPart3 += 1;
	}
	// Count total link errors in XML
	totalXMLErrors = 0;
	for(int i=0;i<screensId.size();i++){
		if(getScreenHasBrokenLinks(i)){ 
			cout << "Error link in screen-id:"<< screensId[i] << endl;
			totalXMLErrors += 1;
		}
	}

	exportGraph();
}

void screensManager::exportGraph(){
	string fileName = "process.gv.txt";
	string tempExportFile = "";
	for(int i=0;i<screensId.size();i++){
		
	}
	ofFile temp;
}

string screensManager::getScreenType(){
	return screens[selectedScreen].type;
}

int screensManager::getIdQuestionWinner(int i){
	int id = screens[selectedScreen].answers[i].link;
	return id;
}

void screensManager::setSelectedScreen(int value){
	selectedScreen = value;
}

string screensManager::getDynamicTextMethod()
{
	return screens[selectedScreen].dynamicTextMethod;
}

string screensManager::getYesQuestionDynamicTextMethod(){
	return screens[selectedScreen].answers[0].dynamicTextMethod;
}

string screensManager::getNoQuestionDynamicTextMethod(){
	return screens[selectedScreen].answers[1].dynamicTextMethod;
}

string screensManager::getCurrentTextQuestion()
{
	return screens[selectedScreen].text;
}

string screensManager::getCurrentTextQuestion(int id)
{
	return screens[id].text;
}

int screensManager::getCurrentTotalAnswers()
{
	return screens[selectedScreen].answers.size();	
}

string screensManager::getCurrentAnswerText(int id)
{
	return screens[selectedScreen].answers[id].text;
}

int screensManager::getScreenLink(){
	return screens[selectedScreen].link;
}

string screensManager::getStatementOptionQuestion(string option){
	return "";
}

string screensManager::getStatementOptionQuestion(int i){
	return screens[selectedScreen].answers[i].statement;
}

void screensManager::subsChars(string & origString){  
	static charSubstitution chars[] = {    
                 {"À","\xC0"}, {"Á","\xC1"}, {"Â","\xC2"}, {"Ã","\xC3"}, {"Ã","\xC4"}, {"Å","\xC5"}, {"Æ","\xC6"},  
                 {"à","\xE0"}, {"á","\xE1"}, {"â","\xE2"}, {"ã","\xE3"}, {"ä","\xE4"}, {"å","\xE5"}, {"æ","\xE6"},  
                 {"Ç","\xC7"},  
                 {"ç","\xE7"},  
                 {"È","\xC8"}, {"É","\xC9"}, {"Ê","\xCA"}, {"Ë","\xCB"},  
                 {"è","\xE8"}, {"é","\xE9"}, {"ê","\xEA"}, {"ë","\xEB"},  
                 {"Ì","\xCC"}, {"Í","\xCD"}, {"Î","\xCE"}, {"Ï","\xCF"},  
                 {"ì","\xEC"}, {"í","\xED"}, {"î","\xEE"}, {"ï","\xEF"},  
                 {"Ñ","\xD1"},  
                 {"ñ","\xF1"},  
                 {"Ò","\xD2"}, {"Ó","\xD3"}, {"Ô","\xD4"}, {"Õ","\xD5"}, {"Ö","\xD6"}, {"Ø","\xD8"},  
                 {"ò","\xF2"}, {"ó","\xF3"}, {"ô","\xF4"}, {"õ","\xF5"}, {"ö","\xF6"}, {"ø","\xF8"},  
                 {"ß","\xDF"},  
                 {"Ù","\xD9"}, {"Ú","\xDA"}, {"Û","\xDB"}, {"Ü","\xDC"},  
                 {"ù","\xF9"}, {"ú","\xFA"}, {"û","\xFB"}, {"ü","\xFC"},  
                 {"ÿ","\xFF"}  
             }; 
          
	for(int i=0; i<56; i++){
         while(origString.find(chars[i].character)!=string::npos){  
			 //cout << origString.substr(origString.find(chars[i].character)+2)<< chars[i].code << endl;
			 //std::wcout << chars[i].code << endl;
			 origString = origString.substr(0,origString.find(chars[i].character))+ chars[i].code + origString.substr(origString.find(chars[i].character)+2);
         }  
    };  
}  

float screensManager::getTimerInMiliSeconds(){
	return screens[selectedScreen].time*1000;
}

float screensManager::getTimerProInMiliSeconds(){
	return screens[selectedScreen].timePro*1000;
}

float screensManager::getTimerContraInMiliSeconds(){
	return screens[selectedScreen].timeContra*1000;
}

string screensManager::getTextAnswerYes(){
	return screens[selectedScreen].answers[0].text;
}

string screensManager::getTextAnswerNo(){
	return screens[selectedScreen].answers[1].text;
}

string screensManager::getIdQuestionYesWinner(){
	return ofToString(getIdQuestionWinner(0));
}

string screensManager::getIdQuestionNoWinner(){
	return ofToString(getIdQuestionWinner(1));
}

void screensManager::setIdQuestionYesWinner(){
	lastSelectedScreen = selectedScreen;
	selectedScreen = getIdQuestionWinner(0);
}

void screensManager::setIdQuestionNoWinner(){
	lastSelectedScreen = selectedScreen;
	selectedScreen = getIdQuestionWinner(1);
}

bool screensManager::getIdSoundQuestion(){
	return screens[selectedScreen].hasAudioFile;
}

string screensManager::getIdSoundPath(int i){
	return screens[selectedScreen].answers[i].audioFile;
}

int screensManager::getSelectedScreen(){
	return selectedScreen;
}

string screensManager::getScreenId(){
	return screens[selectedScreen].id;
}

void screensManager::setScreenLinkAsSelectedScreen(){
	setSelectedScreen(getScreenLink());
}

int screensManager::getCurrentTotalScreens(){
	return screens.size();
}

string screensManager::getIdScreenType(int i){
	int id= getIdScreen(i);
	return screens[id].type;
}

int screensManager::getIdScreen(int i){
	return screensId[i];
}

bool screensManager::getIsIdScreen(int i){
	bool temp = false;
	map<int,screenData>::iterator it;
	it = screens.find(i);
	if(it!=screens.end())temp = true;
	return temp;
}

bool screensManager::getScreenHasBrokenLinks(int i){
	bool temp = false;
	int id = getIdScreen(i);
	string typeScreen = screens[id].type;
	
	if( typeScreen=="question" || typeScreen=="debate" ){
		if( screens[id].answers.size()==2 ){
			if(!getIsIdScreen(screens[id].answers[0].link)) temp = true;
			if(!getIsIdScreen(screens[id].answers[1].link)) temp = true;
		}else{
			temp = true;
		}
	}else if( typeScreen=="statement" || typeScreen=="text" ){
		if( !getIsIdScreen(screens[id].link) ){
			temp = true;
		}
	}
	return temp;
}

int screensManager::getTotalScreensPart1(){
	return countScreensPart1;
}

int screensManager::getTotalScreensPart2(){
	return countScreensPart2;
}

int screensManager::getTotalScreensPart3(){
	return countScreensPart3;
}

int screensManager::getTotalXMLErrors(){
	return totalXMLErrors;
}

int screensManager::getScreenArId(){
	return screens[selectedScreen].arId;
}

bool screensManager::getScreenHaveTextInProContra(){
	return screens[selectedScreen].pro!="" && screens[selectedScreen].contra!="";
}

string screensManager::getScreenProText(){
	return screens[selectedScreen].pro;
}

string screensManager::getScreenContraText(){
	return screens[selectedScreen].contra;
}

string screensManager::getActionId(){
	return screens[selectedScreen].action;
}

string screensManager::getOFId(){
	return screens[selectedScreen].of;
}

bool screensManager::setOFHaveThis(string value){
	return getOFId()==value;
}

string screensManager::getScreenScript(){
	return screens[selectedScreen].script;
}

