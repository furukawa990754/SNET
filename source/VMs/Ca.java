import java.io.IOException;
import java.io.File;
import javax.swing.JOptionPane;

public class Ca{
public static void execd(String path,String key){
    try {
      Runtime rt = Runtime.getRuntime();
      rt.exec(new String[]{path,"startvm",key});
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

