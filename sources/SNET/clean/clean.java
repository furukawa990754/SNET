import java.io.File;
public class clean{
public static void main(String[] args){

File dir = new File("./resources/profile");
File[] dir2 = dir.listFiles();
for (int i = 0; i < dir2.length; i++) {
  if (dir2[i].exists() && dir2[i].isFile()) {
    dir2[i].delete();
    System.out.println("ファイル削除");
  }
}
}}