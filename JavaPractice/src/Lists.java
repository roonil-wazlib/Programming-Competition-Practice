import java.util.List;
import java.util.Scanner;

public class Lists {

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();

        //fastest way to read in lines competition format
        String[] ls = str.split(" ");
        System.out.println(ls);
    }

    public static void loopList(List<String> ls){
        //basic looping
        for (String x : ls){
            System.out.println(x);
        }
        //the closest we can get to enumerate in this sad language
        for (int i = 0; i < ls.size(); i++) {
            System.out.println(i + " " + ls.get(i));
        }

    }


}
