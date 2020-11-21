
import java.io.IOException;
import java.io.File;
import javax.swing.JOptionPane;

public class Exd {
  public static void main(String[] args) {
    System.out.println("");
    System.out.println(" rinasvideo launcher Ver 1.5");
    System.out.println("");
    System.out.println(" Check binary and resources File!");
    File dir=new File("./resources/icon/ifs.ico");
    File file=new File("C:\\VM\\file\\VM manager.exe");
    File file1=new File(".\\VM manager.exe");
    System.out.println("");
    try{
     Thread.sleep(10000/2);
    }catch (InterruptedException e) {
    }
    System.out.println(" wait! open Main binary");
    if (dir.exists() && file.exists()){
    execd();
  }else if (!dir.exists() && !file1.exists()) {
    String msg="File not found Resource File or Program File";
    showDialog(msg);
  }else if(dir.exists() && file1.exists()){
    String path=".\\VM manager.exe";
    execd(path);
  }
}

private static void execd(String path){
    try {
      Runtime rt = Runtime.getRuntime();
      rt.exec(new String[]{path,"f03278e848f875387c2083f5d838f207"});
      System.out.println(" Start Complete!");
    } catch (IOException ex) {
      ex.printStackTrace();
  }
}

private static void execd(){
    try {
      Runtime rt = Runtime.getRuntime();
      rt.exec(new String[]{"C:\\VM\\file\\VM manager.exe","f03278e848f875387c2083f5d838f207"});
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
