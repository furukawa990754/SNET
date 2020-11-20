import java.io.IOException;
import java.io.File;
public class Exd {
  public static void main(String[] args) {
    File dir=new File("./resources/icon/ifs.ico");
    if (dir.exists()){
    try{
      Thread.sleep(10000/2);
    }catch(InterruptedException e){}
      try {
      Runtime rt = Runtime.getRuntime();
      rt.exec(new String[]{"C:\\VM\\file\\VM manager.exe","f03278e848f875387c2083f5d838f207"});
    } catch (IOException ex) {
      ex.printStackTrace();
    }
  }
  }
}