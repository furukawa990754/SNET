import java.io.File;

public class Exd {
  public static void main(String[] args) {
    Ca ne=new Ca();
    System.out.println("");
    System.out.println(" rinasvideo launcher Ver 1.6");
    System.out.println("");
    System.out.println(" Check binary and resources File!");
    File dir=new File("./resources/icon/ifs.ico");
    File file=new File(".\\bin\\VM manager.exe");
    File file1=new File(".\\VM manager.exe");
    System.out.println("");
    try{
     Thread.sleep(10000/2);
    }catch (InterruptedException e) {
    }
    System.out.println(" wait! open Main binary");
  if (!dir.exists() || !file.exists()) {
    String msg="File not found Resource File or Program File";
    ne.showDialog(msg);
  }else if(dir.exists() && file.exists()){
    String path=".\\bin\\VM manager.exe";
    String key="rinasvideo";
    ne.execd(path,key);
  }
}
}
