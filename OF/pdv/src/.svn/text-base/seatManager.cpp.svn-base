#include "seatManager.h"

// SINGLETON initalizations
bool seatManager::instanceFlag = false;
seatManager* seatManager::single = NULL;

//----------------------------------------------

seatManager* seatManager::getInstance()
{
    if(! instanceFlag)
    {
        single = new seatManager();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

seatManager::seatManager()
{

}

seatManager::~seatManager(){

}

void seatManager::setup()
{
	loadFile();
}

void seatManager::loadFile()
{
	const string line_delimiter = "\n";
	const string column_delimiter = "\t";

	if(seats.size()>1) seats.erase(seats.begin(),seats.end());

	// Load file
	string seatsFileName = settingsManager::getInstance()->getDataPath()+"map.tsv";//"map.tsv";//
	ofFile file =  ofFile(seatsFileName);
	//cout << "Loading map file: "<< seatsFileName << endl;
	string stringContent = file.readToBuffer().getText();
	//cout << stringContent  << endl;
	// Check if file have any line delimiter (looking if is well form)
	if(stringContent.find(line_delimiter)!=-1){
		// split by lines
		vector<string> lines = ofSplitString(stringContent,line_delimiter);
		//cout << "Lines map file: "<< lines.size() << endl;

		// to save errors
		if(lines.size()==0) return;
		// debug
		if((settingsManager::getInstance()->getTotalSeats()+1)!=lines.size()){ 
			cout << "Error map.tsv - lines:"+ofToString(lines.size()) << endl;
		}
		// total columns
		totalColumns = ofSplitString(lines[0],column_delimiter).size();
		//cout << "Columns map file: "<< totalColumns << endl;

		// split lines by columns
		for(int i=1;i<lines.size();i++)
		{
			if(lines[i].find(column_delimiter)!=-1)
			{
				vector<string> columns = ofSplitString(lines[i],column_delimiter); 
				if(columns.size() ==totalColumns){
					seats.push_back(columns);
				}else{
					cout <<"Error row with Less Columns than expected"<< endl;
				}
			}
		}
		//cout <<"Total seats at load:" << seats.size() << endl;
		//cout <<"Total columns at load:" << seats[0].size() << endl;
	}
}

int seatManager::getTotalSeats()
{
	return seats.size();
}

int seatManager::getTotalActiveSeats(){
	int temp = 0;
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)=="false") temp+=1; 
	}
	int total = getTotalSeats()-temp;
	return total;
}

ofVec2f seatManager::getSeatArToPixel(int i)
{
	ofVec2f temp = ofVec2f(0,0);
	if(i<0 || i>=seats.size()) return temp; 
	temp.x = ofToFloat(seats[i][4]);
	temp.y = ofToFloat(seats[i][5]);
	return temp;
}

ofVec2f seatManager::getSeatIdToPixel(int id)
{
	ofVec2f temp = ofVec2f(0,0);
	if(id<0 || id>=seats.size()) return temp; 
	temp.x = ofToFloat(seats[id][4]);
	temp.y = ofToFloat(seats[id][5]);
	return temp;
}

string seatManager::getSeatId(int id){
	return seats[id][0];
}

string seatManager::getkeyPadId(int id){
	return seats[id][1];
}

string seatManager::getXPixId(int id){
	return seats[id][4];
}

string seatManager::getSectionId(int id){
	return seats[id][5];
}

string seatManager::getYPixId(int id){
	return seats[id][6];
}

string seatManager::getGroupId(int id){
	return seats[id][7];
}

string seatManager::getTypeId(int id){
	return seats[id][8];
}

string seatManager::getActiveIdStr(int id){
	return seats[id][9];
}

void seatManager::setActiveIdStr(int id, string value){
	seats[id][9] = value;
}

string seatManager::getGenderId(int id){
	return seats[id][10];
}

string seatManager::getVoteId(int id){
	string temp = seats[id][9];
	std::transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
	return temp;
}

bool seatManager::getActiveId(int id){
	bool temp = true;
	string activeColumn = getActiveIdStr(id);
	std::transform(activeColumn.begin(), activeColumn.end(), activeColumn.begin(), ::tolower);
	if( activeColumn=="false" ) temp = false;
	return temp;
}

int seatManager::getTotalYesVotes(){
	int temp = 0;
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)=="yes") temp+=1; 
	}
	return temp;
}

int seatManager::getTotalNoVotes(){
	int temp = 0;
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)=="no") temp+=1; 
	}
	return temp;
}

int seatManager::getTotalAbsVotes(){
	int temp = 0;
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)=="abs") temp+=1; 
	}
	return temp;
}

int seatManager::getTotalBlockVotes(){
	int temp = 0;
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)=="block" ) temp+=1; 
	}
	return temp;
}

vector<string> seatManager::getPresidentList(){
	vector<string> temp;
	for(int i=0;i<getTotalSeats();i++){
		if(getTypeId(i)=="president") temp.push_back(ofToString(getSeatId(i)));
	}
	return temp;
}

vector<string> seatManager::getArmyList(){
	vector<string> temp;
	for(int i=0;i<getTotalSeats();i++){
		if(getTypeId(i)=="army") temp.push_back(ofToString(getSeatId(i)));
	}
	return temp;
}

vector<string> seatManager::getTribunalList(){
	vector<string> temp;
	for(int i=0;i<getTotalSeats();i++){
		if(getTypeId(i)=="tribunal") temp.push_back(ofToString(getSeatId(i)));
	}
	return temp;
}

int seatManager::getTotalManYes(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="m" && getActiveIdStr(i)=="yes" )totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalWomanYes(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="w" && getActiveIdStr(i)=="yes")totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalManNo(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="m" && getActiveIdStr(i)=="no" )totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalWomanNo(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="w" && getActiveIdStr(i)=="no" )totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalManAbs(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="m" && ( getActiveIdStr(i)=="abs" || getActiveIdStr(i)=="true" ) )totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalWomanAbs(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="w" && ( getActiveIdStr(i)=="abs" || getActiveIdStr(i)=="true" ) )totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalUnknowGenderAbs(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="null" && ( getActiveIdStr(i)=="abs" || getActiveIdStr(i)=="true" )) totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalMan(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="m" && getActiveIdStr(i)!="false" )totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalWoman(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="w" && getActiveIdStr(i)!="false" )totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalUnknowGender(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="null" && getActiveIdStr(i)!="false" ) totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalUnknowGenderYes(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="null" && getActiveIdStr(i)=="yes" ) totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalUnknowGenderNo(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="null" && getActiveIdStr(i)=="no" ) totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalManBlock(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="m" && getActiveIdStr(i)=="block" ) totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalWomanBlock(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="w" && getActiveIdStr(i)=="block" ) totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalUnknowGenderBlock(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getGenderId(i)=="null" && getActiveIdStr(i)=="block" ) totalTemp+=1;
	}
	return totalTemp;
}

// DYNAMIC TEXT FOR STATEMENTS
string  seatManager::getDynamicStament(string method, string statement){
	string temp = statement;
	if(method=="fillPeopleWithVoteAndBlock"){
		temp = fillPeopleWithVoteAndBlock(temp);
	}else if(method=="fillWithOnlyNonBlock"){
		temp = fillWithOnlyNonBlock(temp);
	}else if(method=="fillWith2President"){
		temp = fillWith2President(temp);
	}else if(method=="fillWithPresident"){
		temp = fillWithPresident(temp);
	}else if(method=="fillWith5NonBlock"){
		temp = fillWith5NonBlock(temp);
	}else if(method=="fillWith2Tribunal"){
		temp = fillWith2Tribunal(temp);
	}else if(method=="fillWith2Army"){
		temp = fillWith2Army(temp);
	}else if(method=="fillBlockPeopleAndNonBlock"){
		temp = fillBlockPeopleAndNonBlock(temp);
	}else if(method=="fillAbsWomanManPeople"){
		temp = fillAbsWomanManPeople(temp);
	}
	return temp;
}

// Screen 80 -OK
string seatManager::fillPeopleWithVoteAndBlock(string text){
	int posFirst = text.find("#");
    int posSecond = text.find("#",posFirst+1,1);
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1,(posSecond-posFirst)-1);
	string str3 = text.substr(posSecond+1, text.length()-(posSecond+1));
	int totalPeopleWhoCanVote = getTotalActiveSeats()-getTotalBlockVotes();
	int totalBlockSeats = getTotalBlockVotes();
	string temp = str1+ofToString(totalPeopleWhoCanVote)+str2+ofToString(totalBlockSeats)+str3;
	return temp;
}

// Screen 415 - cas per answer
string seatManager::fillAbsWomanManPeople(string text){
	
	string temp;
	int posFirst = text.find("#");
    int posSecond = text.find("#",posFirst+1,1);
	int posThird = text.find("#",posSecond+1,1);
	
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1,(posSecond-posFirst)-1);
	string str3 = text.substr(posSecond+1, (posThird-posSecond)-1);
	string str4 = text.substr(posThird+1, text.length()-(posThird+1));
	
	string totalWoman = ofToString(getTotalNoVotes());
	string totalMan = ofToString(getTotalYesVotes());
	string totalAbs = ofToString(getTotalAbsVotes());

	text = str1+totalWoman+str2+totalMan+str3+totalAbs+str4;
	return text;
}

// Screen 450 i 430 -OK
string seatManager::fillWith2President(string text){
	string temp;
	int posFirst = text.find("#");
    int posSecond = text.find("#",posFirst+1,1);
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1,(posSecond-posFirst)-1);
	string str3 = text.substr(posSecond+1, text.length()-(posSecond+1));
	
	vector<string> president = getPresidentList();
	if(president.size()==2){
		temp = str1+president[0]+str2+president[1]+str3;
	}
	return temp;
}

// Screen 495 i 500 (2 variables) -OK
string seatManager::fillWith2Army(string text){
	string temp;
	int posFirst = text.find("#");
    int posSecond = text.find("#",posFirst+1,1);
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1,(posSecond-posFirst)-1);
	string str3 = text.substr(posSecond+1, text.length()-(posSecond+1));
	
	vector<string> army = getArmyList();
	if(army.size()==2){
		temp = str1+army[0]+str2+army[1]+str3;
	}
	return temp;
}

// Screen 1015 (1 variables) -OK
string seatManager::fillBlockPeopleAndNonBlock(string text){
	int posFirst = text.find("#");
    int posSecond = text.find("#",posFirst+1,1);
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1,(posSecond-posFirst)-1);

	int totalPeopleWhoCanVote = getTotalActiveSeats()-getTotalBlockVotes();
	int totalBlockSeats = getTotalBlockVotes();
	string temp = str1+ofToString(totalPeopleWhoCanVote)+str2;
	return temp;
}

// Screen 1230, 1240 i 1215 (2 variables) -OK
string seatManager::fillWith2Tribunal(string text){
	string temp;
	int posFirst = text.find("#");
    int posSecond = text.find("#",posFirst+1,1);
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1,(posSecond-posFirst)-1);
	string str3 = text.substr(posSecond+1, text.length()-(posSecond+1));
	
	vector<string> tribunal = getTribunalList();
	if(tribunal.size()==2){
		temp = str1+tribunal[0]+str2+tribunal[1]+str3;
	}
	return temp;
}

// Screen 2005 - OK
string seatManager::fillWith5NonBlock(string text){
	string temp;
	int posFirst = text.find("#");
    int posSecond = text.find("#",posFirst+1,1);	
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1,(posSecond-posFirst-1));

	vector<string> block = getPeopleNonBlockList();
	if(block.size()>1){
		string tempAll;
		for(int i=0;i<block.size();i++){
			tempAll+=block[i];
			if(i+2<block.size()){
				tempAll+=",";
			}else if(i+1<block.size()){
				tempAll+=" "+translateManager::getInstance()->t("and")+" ";
			}
		}
		temp = str1+tempAll+str2;    
	}
	return temp;
}

// Screen 2105 - OK
string seatManager::fillWithPresident(string text){
	string temp;
	int posFirst = text.find("#");
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1, text.length()-(posFirst+1));
	vector<string> president = getPresidentList();
	if(president.size()==1){
		temp = str1+president[0]+str2;
	}
	return temp;
}

// Screen 2200 i 2195 - OK
string seatManager::fillWithOnlyNonBlock(string text){
	string temp;
	int posFirst = text.find("#");
	string str1 = text.substr(0,posFirst);
	string str2 = text.substr(posFirst+1, text.length()-(posFirst+1));
	vector<string> nonBlockPeople = getPeopleNonBlockList();
	if(nonBlockPeople.size()==1){
		temp = str1+nonBlockPeople[0]+str2;
	}
	return temp;
}

int seatManager::getTotalBlockNonPeople(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)!="true" || getActiveIdStr(i)!="yes" || getActiveIdStr(i)!="no" || getActiveIdStr(i)!="abs" ) totalTemp+=1;
	}
	return totalTemp;
}

int seatManager::getTotalEmptySeats(){
	int totalTemp = 0; 
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)!="false" ) totalTemp+=1;
	}
	return totalTemp;
}

vector<string> seatManager::getPeopleNonBlockList(){
	vector<string> temp;
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)!="block" && getActiveIdStr(i)!="false") temp.push_back(ofToString(getSeatId(i)));
	}
	return temp;
}


void seatManager::setAllSeatsYes(){
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)!="false" && getActiveIdStr(i)!="block"){
			setActiveIdStr(i,"yes");
		}
	}
}

void seatManager::setAllSeatsNo(){
	for(int i=0;i<getTotalSeats();i++){
		if(getActiveIdStr(i)!="false" && getActiveIdStr(i)!="block" ){
			setActiveIdStr(i,"no");
		}
	}
}