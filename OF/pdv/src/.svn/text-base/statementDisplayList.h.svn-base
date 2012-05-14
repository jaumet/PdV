#ifndef _STATEMENT_DISPLAY_LIST_
#define _STATEMENT_DISPLAY_LIST_

#include "ofMain.h"
#include "fontManager.h"
#include "ofxTextBox.h"
#include "votesManager.h"
#include "colorPalette.h"

struct statementListItem{
	ofxTextBox text;
	string id;
	bool result;
};

class statementDisplayList
{
public:
	statementDisplayList();
	~statementDisplayList();
	void draw(int x, int y);
	void load();
	void insert(string id, string statement);

private:
	vector<statementListItem> resum;
};

#endif