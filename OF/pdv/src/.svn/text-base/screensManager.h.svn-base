#ifndef _OFX_QUESTION_MANAGER_
#define _OFX_QUESTION_MANAGER_

#include "ofMain.h"
#include "ofxXmlSettings.h"
#include <cstdlib>
#include <iostream>
#include <wchar.h>
#include "settingsManager.h"

struct answer{
	string text;
	int link;
	string statement;
	string audioFile;
	string dynamicTextMethod;
};

struct screenData{
	string of;
	int arId;
	string id;
	string text;
	int time;
	int timeContra;
	int timePro;
	string type;
	string script;
	string pro;
	string contra;
	int link;
	bool hasAudioFile;
	vector<answer> answers;
	string action;
	string dynamicTextMethod;
};

typedef struct{
	string character;  
    string code;  
}charSubstitution;  

class screensManager
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static screensManager *single;	
public: 
static screensManager* getInstance();
// end singleton
public:
	screensManager();
	~screensManager();
	void setup();
	string getCurrentTextQuestion();
	int getCurrentTotalAnswers();
	string getCurrentTextQuestion(int id);
	string getCurrentAnswerText(int id);
	string getStatementOptionQuestion(string option);
	string getStatementOptionQuestion(int i);
	void subsChars(string & origString);
	void load();
	string getDynamicTextMethod();
	string getYesQuestionDynamicTextMethod();
	string getNoQuestionDynamicTextMethod();
	string getScreenScript();
	string getOFId();
	string getActionId();
	string getScreenId();
	int getScreenLink(); // only for screen type-text
	string getScreenType();
	string getIdQuestionYesWinner();
	string getIdQuestionNoWinner();
	float getTimerInMiliSeconds();
	float getTimerProInMiliSeconds();
	float getTimerContraInMiliSeconds();
	void setIdQuestionYesWinner();
	void setIdQuestionNoWinner();
	int getIdQuestionWinner(int i);
	void setSelectedScreen(int value);
	int getSelectedScreen();
	bool getIdSoundQuestion();
	string getIdSoundPath(int i);
	void setScreenLinkAsSelectedScreen();
	int getCurrentTotalScreens();
	string getIdScreenType(int i);
	int getIdScreen(int i);
	bool getIsIdScreen(int i);
	bool getScreenHasBrokenLinks(int i);
	bool getScreenHaveTextInProContra();
	string getScreenProText();
	string getScreenContraText();

	int getTotalScreensPart1();
	int getTotalScreensPart2();
	int getTotalScreensPart3();
	int getTotalXMLErrors();
	int getScreenArId();
	bool setOFHaveThis(string value);

	void exportGraph();

	string getTextAnswerYes();
	string getTextAnswerNo();

private:
	
	ofxXmlSettings xml;
	vector<int> screensId;
	map<int,screenData> screens;
	int selectedScreen;
	int lastSelectedScreen;
	int countScreensPart1;
	int countScreensPart2;
	int countScreensPart3;
	int totalXMLErrors;
};

#endif

