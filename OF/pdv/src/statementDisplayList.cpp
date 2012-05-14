#include "statementDisplayList.h"

statementDisplayList::statementDisplayList(){
}

statementDisplayList::~statementDisplayList(){
}

void statementDisplayList::draw(int x, int y){
	int posYResum =0;
	for(int i=0;i<resum.size();i++){
		//
		fontManager::getInstance()->setTextColor();
		resum[i].text.draw(650,posYResum+100);
		//
		string tempStr = resum[i].id;
		int withID = fontManager::getInstance()->getTextFont()->stringWidth(tempStr)+2;
		int heightID = fontManager::getInstance()->getTextFont()->getLineHeight()+2;
		ofSetColor(0,0,0);
		ofRect(650,posYResum+100,withID,heightID);

		if(resum[i].result){
			colorPalette::getInstance()->setYesVotesColor();
		}else{
			colorPalette::getInstance()->setNoVotesColor();
		}
		fontManager::getInstance()->getTextFont()->drawString(tempStr,650,posYResum+100+heightID);
		//
		posYResum += resum[i].text.getTextHeight()+15;
	}
}

void statementDisplayList::load(){
	int totalHeight = 580;
	int height = 0;
	resum.erase(resum.begin(),resum.end());
	for(int i=votesManager::getInstance()->getTotalStatements()-1;i>0;i--){
		//
		statementListItem tempItem;
		ofxTextBox temp;
		temp.setFont(fontManager::getInstance()->getTextFont());
		temp.setBoxSize(320,400);
		temp.setText(votesManager::getInstance()->getStatementText(i));
		height += temp.getTextHeight()+15;

		tempItem.text = temp;
		tempItem.id = votesManager::getInstance()->getStatementId(i);
		tempItem.result = votesManager::getInstance()->getStatementResult(i);
		if(height<totalHeight){
			resum.push_back(tempItem);
		}else{
			if((height-15)<=totalHeight){
				resum.push_back(tempItem);
			}else{
				int linesToRemove = (int)ceil((((float)height-15.0f)-(float)totalHeight)/(float)temp.getLineHeight());
				temp.removeLinesFromBack(linesToRemove);
				if(temp.getTotalLines()>0){
					tempItem.text = temp;
					resum.push_back(tempItem);
				}
			}
			break;
		}
	}
}


void insert(string id, string statement){

}