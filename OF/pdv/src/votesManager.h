#ifndef _VOTES_MANAGER_
#define _VOTES_MANAGER_

#include "ofMain.h"
#include "seatManager.h"
#include "ofxXmlSettings.h"
#include "ofxTimer.h"
#include "ofEvents.h"
#include "actionsManager.h"
#include "screensManager.h"

struct option{
	string title;
	int totalVotes;
	float percent;
};

struct votacion{
	string title;
	vector<option> options;
	map<string, int> seatVotes;
};

struct statementInfo{
	string text;
	string id;
	bool result;
};

class votesManager
{
// variables & methods for singleton
private:
static bool	instanceFlag;
static votesManager *single;	
public: 
static votesManager* getInstance();
// end singleton
public:
	votesManager();
	~votesManager();
	void setup();
	void reset();
	void startVotation();
	void prepareDebate();
	
	string getVotationID();
	void setVotationID(int i);
	void goNextVotation();
	void goToVotationResult();
	int getCurrentQuestionID();
	void drawFBOBegin();
	void drawFBOEnd();
	void drawFBO(int x, int y);
	ofFbo* getFBO();
	string getCurrentStatement();
	void timeOutVotation( ofEventArgs &e);
	void timeOutPRO( ofEventArgs &e);
	void timeOutCONTRA( ofEventArgs &e);
	bool getIsDebate();
	void nextScreen();
	void setNextVotationID();
	int getAnswerWinnerID();

	void startCountDown();

	ofEvent<ofEventArgs> nextScreenEvent;

	ofxTimer myOfxTimerVotation;
	ofxTimer myOfxTimerContra;
	ofxTimer myOfxTimerPro;
	ofxTimer *myOfxCurrentTimer;

	void setStartPerformance();
	float getElapsedTimeVotation();
	bool getStartPerformance();
	void setStartPerformance(bool value);
	int getTotalStatements();
	string getStatementText(int i);
	string getStatementId(int i);
	bool getStatementResult(int i);
	ofxTimer * getCurrentTimer();
	void setPauseTimer();
	void closeAllTimers();
	int lastStoredScreenShowed();
	void saveScreenShowed();
	string getResultStatement();
	string getCurrentVotation3digits();
private:
	void saveStatementVotation();
	ofxXmlSettings xmlSession;
	vector<statementInfo> statement;
	vector<ofImage> screensVotations;  
	int currentVotationID;
	int currentQuestionID;
	int currentAnswerWinnerID;

	ofFbo screenRenderOffline;
	
	double startTimeVotation;
	bool startPerformance;
	ofxXmlSettings XMLscreenShowed;
};

#endif

