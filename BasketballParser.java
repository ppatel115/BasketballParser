import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

// compile by javac BasketballParser.java
// then java BasketballParser

public class BasketballParser{
 public static void main(String[] args) throws FileNotFoundException{

   File text = new File("sample_input.txt");       // get from textise.net
   Scanner sc = new Scanner(text);

   String [] currentPlayer = {"Jalen Hudson", "Egor Koulechov", "KeVaughn Allen", "Chris Chiozza", "Keith Stone"};


   while(sc.hasNextLine()){
           String line = sc.nextLine();
           System.out.println(line);


         }



   sc.close();
 }
}
