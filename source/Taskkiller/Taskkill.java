import java.io.File;


public class Taskkill {
  public static void main(String[] args) {
    Ca ne=new Ca();
    System.out.println("");
    System.out.println(" Taskkill Ver 1.5");
    System.out.println("");
    System.out.println(" Check binary and resources File!");
    File dir=new File("./resources/icon/ifs.ico");
    System.out.println("");
    try{
     Thread.sleep(10000/2);
    }catch (InterruptedException e) {
    }
    System.out.println(" wait! open Main binary");
    ne.execd();
 }
}

