#include "callPythonScripts.h"

// SINGLETON initalizations
bool callPythonScripts::instanceFlag = false;
callPythonScripts* callPythonScripts::single = NULL;

//----------------------------------------------

callPythonScripts* callPythonScripts::getInstance()
{
    if(! instanceFlag)
    {
        single = new callPythonScripts();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

callPythonScripts::callPythonScripts(){
	
}

callPythonScripts::~callPythonScripts(){
}

void callPythonScripts::callScript(string script){
	#ifdef TARGET_WIN32
	path = "C:\\PdV\\python\\";
	string command = "python "+path+script;
	cout << "Called to python:"<< command << endl;
	system(command.c_str());
	Sleep(500);
	#endif
}
