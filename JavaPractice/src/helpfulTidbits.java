import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Function;
import java.util.function.UnaryOperator;

public class helpfulTidbits {
    //a collection of useful stuff I probably should already have known how to do but didn't because I avoided java like the plague

    public static void main(String[] args) {
        System.out.println("Hello World");
        math(2, 10);


        var list1 = List.of("a", "b"); //an immutable list
        var list2 = new ArrayList<>(List.of(1, 2)); //a mutable list
        list2.add(3);

        Map<Integer, Integer> cache = new ConcurrentHashMap<>();


        //listComp(list1);
        //System.out.println(list1); //can't do this because list is immutable
        listComp2(list2);
        System.out.println(list2);

    }

    private static long uncached(long n) {
        long result = n;
        long m = n - 1;
        while (m > 1) {
            result = result * m;
            m -= 1;
        }
        return result;
    }


    public static void math(int x, int y) {
     //some math functions i will need

     System.out.println(Math.max(x, y));
     System.out.println(Math.min(x, y));
     System.out.println(Math.abs(x));
     System.out.println(Math.pow(x, y)); //x**y//
     System.out.println(Math.random()); //random float between 0 and 1
     System.out.println(Math.hypot(x, y)); //hypotenuse!
     System.out.println(Math.cosh(x)); //trig and hyperbolic trig included!
     System.out.println(Math.copySign(x, y)); //copy sign of y onto x

     //and many more useful ones to look at
    }

    public static void listComp(List<String> ls) {
        ls.replaceAll(String::toUpperCase); //or similar
    }

    public static void listComp2(List<Integer> ls) {
        //for custom replace all
        ls.replaceAll(new MyOperator());
    }

    public static void readingInContent(List<Integer> ls) {
        Scanner in = new Scanner(System.in);
        int value = in.nextInt(); //if we know it will be an int
        String otherValue = in.nextLine(); //For strings
    }

}

class MyOperator implements UnaryOperator<Integer>
{
    @Override
    public Integer apply(Integer x) {
        return x + 1;
    }
}



