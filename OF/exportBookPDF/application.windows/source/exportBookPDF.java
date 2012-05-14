import processing.core.*; 
import processing.xml.*; 

import processing.pdf.*; 

import java.applet.*; 
import java.awt.Dimension; 
import java.awt.Frame; 
import java.awt.event.MouseEvent; 
import java.awt.event.KeyEvent; 
import java.awt.event.FocusEvent; 
import java.awt.Image; 
import java.io.*; 
import java.net.*; 
import java.text.*; 
import java.util.*; 
import java.util.zip.*; 
import java.util.regex.*; 

public class exportBookPDF extends PApplet {

/**
 * RandomBook
 * 
 * Creates a 768 page book of random lines.
 */



PGraphicsPDF pdf;
File[] files;
String path;
 
public void setup() {
  size(1024, 768);
  // Path
  path = "C:\\PdV\\data\\png_export_export\\";
  println("Listing all filenames in a directory: ");
  String[] filenames = listFileNames(path);
  println(filenames);
  
  println("\nListing info about all files in a directory: ");
  files = listFiles(path);
  
  pdf = (PGraphicsPDF)beginRecord(PDF, "pdv_Book.pdf");
  beginRecord(pdf);
}

public void draw() {  
  background(255);
  
  for (int i = 0; i < files.length; i++) {
    File f = files[i];    
    println("Name: " + f.getName());
    println("Is directory: " + f.isDirectory());
    println("Size: " + f.length());
    String lastModified = new Date(f.lastModified()).toString();
    println("Last Modified: " + lastModified);
    println("-----------------------");
    
    if(!f.getName().equals(".svn")){
      String imagePath = path+f.getName();
      println(imagePath);
      PImage img = loadImage(imagePath);
      image(img,0,0);
      if( (i+1) < files.length)pdf.nextPage(); 
    }
  }
  
  endRecord();
  exit();  // Quit
}

// This function returns all the files in a directory as an array of Strings  
public String[] listFileNames(String dir) {
  File file = new File(dir);
  if (file.isDirectory()) {
    String names[] = file.list();
    return names;
  } else {
    // If it's not a directory
    return null;
  }
}

// This function returns all the files in a directory as an array of File objects
// This is useful if you want more info about the file
public File[] listFiles(String dir) {
  File file = new File(dir);
  if (file.isDirectory()) {
    File[] files = file.listFiles();
    return files;
  } else {
    // If it's not a directory
    return null;
  }
}
  static public void main(String args[]) {
    PApplet.main(new String[] { "--bgcolor=#D4D0C8", "exportBookPDF" });
  }
}
