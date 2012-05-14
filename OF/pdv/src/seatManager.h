#ifndef _SEAT_MANAGER_
#define _SEAT_MANAGER_

#include "settingsManager.h"
#include "ofMain.h"
#include "ofxXmlSettings.h"
#include "translateManager.h"

#include <exception>
using namespace std;

class seatManager{
// variables & methods for singleton
private:
static bool	instanceFlag;
static seatManager *single;	
public: 
static seatManager* getInstance();
// end singleton
public:
	seatManager();
	~seatManager();

	// General methods
	void setup();
	void loadFile();
	ofVec2f getSeatArToPixel(int i);
	ofVec2f getSeatIdToPixel(int id);
	int getTotalSeats();
	
	// Seat column get methods
	string getGenderId(int id);
	string getSeatId(int id);
	string getkeyPadId(int id);
	string getXPixId(int id);
	string getYPixId(int id);
	string getActiveIdStr(int id);
	string getSectionId(int id);
	string getVoteId(int id);
	string getGroupId(int id);
	string getTypeId(int id);
	bool getActiveId(int id);
	void setActiveIdStr(int id, string value);
	// Votation
	int getTotalYesVotes();
	int getTotalNoVotes();
	int getTotalAbsVotes();
	int getTotalBlockVotes();
	int getTotalActiveSeats();
	int getTotalEmptySeats();

	// Types
	vector<string> getPresidentList();
	vector<string> getArmyList();
	vector<string> getTribunalList();

	// Gender calculations
	int getTotalMan();
	int getTotalWoman();
	int getTotalUnknowGender();
	int getTotalManAbs();
	int getTotalWomanAbs();
	int getTotalUnknowGenderAbs();
	int getTotalManYes();
	int getTotalWomanYes();
	int getTotalUnknowGenderYes();
	int getTotalManNo();
	int getTotalWomanNo();
	int getTotalUnknowGenderNo();
	int getTotalManBlock();
	int getTotalWomanBlock();
	int getTotalUnknowGenderBlock();

	// Methods for dynamic text
	string  getDynamicStament(string method, string statement);
	int getTotalBlockNonPeople();
	vector<string> getPeopleNonBlockList();

	// Dynamic text in statements
	string fillPeopleWithVoteAndBlock(string text);
	string fillWithOnlyNonBlock(string text);
	string fillWithPresident(string text);
	string fillWith2President(string text);
	string fillWith5NonBlock(string text);
	string fillWith2Tribunal(string text);
	string fillBlockPeopleAndNonBlock(string text);
	string fillWith2Army(string text);
	string fillAbsWomanManPeople(string text);

	// debug method
	void setAllSeatsYes();
	void setAllSeatsNo();
private:
	vector<vector <string>> seats;
	int totalColumns;
};

#endif