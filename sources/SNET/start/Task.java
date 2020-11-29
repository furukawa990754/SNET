import java.io.IOException;
import java.io.File;
import javax.swing.JOptionPane;

public class Task{
public static void execd(String path,String key,String keys){
    try {
      Runtime rt = Runtime.getRuntime();
      rt.exec(new String[]{path,key,keys});
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

