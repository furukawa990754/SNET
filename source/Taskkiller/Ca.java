import java.io.IOException;
import java.io.File;
import javax.swing.JOptionPane;

public class Ca{
public static void execd(String path){
    try {
      Runtime rt = Runtime.getRuntime();
      rt.exec(new String[]{path,"f03278e848f875387c2083f5d838f207"});
      System.out.println(" Start Complete!");
    } catch (IOException ex) {
      ex.printStackTrace();
  }
}


public static void execd(){
    try {
      Runtime rt = Runtime.getRuntime();
      rt.exec("taskkill /f /pid \"VM manager.exe\"");
      System.out.println(" Start Complete!");
    } catch (IOException ex) {
      ex.printStackTrace();
  }
}

public static void showDialog(String msg){
    JOptionPane.showMessageDialog(null, msg);
    try{
    Thread.sleep(10000);
    }catch (InterruptedException e) {
    }
  }
}

