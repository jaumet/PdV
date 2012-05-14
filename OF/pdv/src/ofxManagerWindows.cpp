#include "ofxManagerWindows.h"

// SINGLETON initalizations
bool ofxManagerWindows::instanceFlag = false;
ofxManagerWindows* ofxManagerWindows::single = NULL;

//----------------------------------------------

ofxManagerWindows* ofxManagerWindows::getInstance()
{
    if(! instanceFlag)
    {
        single = new ofxManagerWindows();
        instanceFlag = true;
        return single;
    }else{
        return single;
    }
}

ofxManagerWindows::ofxManagerWindows(){

}

ofxManagerWindows::~ofxManagerWindows(){
}

void ofxManagerWindows::setWindowWithNoDecorated(string name){
	#ifdef WIN32  
    HWND hwnd = ::FindWindowA(0, name.c_str()); //NOTE, the windowtitle is crucial in order to find the handle, so you have to set it before!!!!  
    if (hwnd != NULL)  
    { 
		bool winStyleChanged = FALSE;  
		winStyleChanged = ModifyWindowStyle(hwnd, 0, WS_BORDER | WS_THICKFRAME | WS_CAPTION, FALSE);   //undecorate 
	}else{  
        printf("[WARNING] could NOT find window, title might be wrong\n");  
    }		
	#endif 
}

void ofxManagerWindows::setWindowWithDecorated(string name){
	#ifdef WIN32  
    HWND hwnd = ::FindWindowA(0, name.c_str()); //NOTE, the windowtitle is crucial in order to find the handle, so you have to set it before!!!!  
    if (hwnd != NULL)  
    { 
		bool winStyleChanged = FALSE;  
		winStyleChanged = ModifyWindowStyle(hwnd, 0, WS_BORDER | WS_DLGFRAME | WS_CAPTION, FALSE);   //undecorate 
	}else{  
        printf("[WARNING] could NOT find window, title might be wrong\n");  
    }		
	#endif 
}

void ofxManagerWindows::setWindowInPosition(string name,int x,int y){

	#ifdef WIN32  
    HWND hwnd = ::FindWindowA(0, name.c_str()); //NOTE, the windowtitle is crucial in order to find the handle, so you have to set it before!!!!  
    if (hwnd != NULL)  
    {  
        bool winStyleChanged = FALSE;  
        ::SetWindowPos(hwnd, NULL, 0, 0, 0, 0, SWP_NOZORDER | SWP_NOSIZE | SWP_SHOWWINDOW);    //NOTE: repaint glutwindow to update style  
    }else{  
        printf("[WARNING] could NOT find window, title might be wrong\n");  
    }		
	#endif 
}
      
bool ofxManagerWindows::ModifyWindowStyle(HWND hWnd, DWORD dwAdd, DWORD dwRemove, BOOL bEx)  
{  
	#ifdef WIN32  
    ::SetLastError(0);  
      
    DWORD dwStyle    = ::GetWindowLong(hWnd, (bEx ? GWL_EXSTYLE : GWL_STYLE));  
    DWORD dwNewStyle = (dwStyle & (~dwRemove)) | dwAdd;  
    ::SetWindowLong(hWnd, (bEx ? GWL_EXSTYLE : GWL_STYLE), dwNewStyle);  
      
    ::SetWindowPos(hWnd, NULL, 0, 0, 0, 0, SWP_NOZORDER | SWP_NOSIZE | SWP_NOMOVE | SWP_SHOWWINDOW | SWP_FRAMECHANGED);  
      
    //NOTE: this is necessary for updating visuals!!!  
    ::UpdateWindow(hWnd);  
    ::ShowWindow(hWnd, SW_SHOW);    //SW_SHOWNORMAL, SW_SHOWNA  
    ::SetFocus(hWnd);  
      
    return (::GetLastError() == 0);  
	#endif 
}  

void ofxManagerWindows::SetWindowAlwaysOnTop(string name) {  
#ifdef TARGET_WIN32  
    //get its handle "GLUT" = class name "ogl" = window   
    HWND hwnd = ::FindWindowA(0, name.c_str()); //NOTE, the windowtitle is crucial in order to find the handle, so you have to set it before!!!!  
    if (hwnd != NULL)  
    {  
		//set the window always-on-top  
		::SetWindowPos(hwnd, HWND_TOPMOST, NULL, NULL, NULL, NULL, SWP_NOREPOSITION | SWP_NOSIZE );  
	}
#endif  
  
#ifdef TARGET_OSX  
    // What goes here??  
#endif  
  
#ifdef TARGET_LINUX  
    // What goes here?  
#endif  
}  


void ofxManagerWindows::SetFocus(string name) {  
#ifdef TARGET_WIN32  
    //get its handle "GLUT" = class name "ogl" = window   
    HWND hwnd = ::FindWindowA(0, name.c_str()); //NOTE, the windowtitle is crucial in order to find the handle, so you have to set it before!!!!  
    if (hwnd != NULL)  
    {  
		::SetFocus(hwnd);
	}
#endif  
  
#ifdef TARGET_OSX  
    // What goes here??  
#endif  
  
#ifdef TARGET_LINUX  
    // What goes here?  
#endif  
}  
