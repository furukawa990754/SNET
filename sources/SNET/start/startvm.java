import java.io.File;


public class startvm {
  public static void main(String[] args) {
    Task ne=new Task();
    System.out.println("");
    System.out.println(" Taskkill Ver 1.5");
    System.out.println("");
    System.out.println(" Check binary and resources File!");
    File dir=new File("./resources/icon/ifs.ico");
    System.out.println("");
    System.out.println(" wait! open Main binary");
    String path="VBoxManage.exe";
    String keys=args[0];
    String key="startvm";
    ne.execd(path,key,keys);
 }
}

