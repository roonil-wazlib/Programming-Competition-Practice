import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class GoldbachConjecture {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int value = in.nextInt();
        System.out.println(goldbach(value, primeSeive(value)));
    }

    public static List<Integer> primeSeive(int n){
        var primes = new ArrayList<Integer>();
        for (int i = 2; i < n + 1; i++) {
            primes.add(i);
        }

        for (int i = 0; i < Math.sqrt(n); i++) {

            int prime = primes.get(i);
            if (prime != -1) {
                int j = 2 * prime;
                while (true) {
                    if (j-2 >= primes.size()) {
                        break;
                    } else {
                        primes.set(j-2, -1);
                    }
                    j += prime;
                }
            }
        }

        var output = new ArrayList<Integer>();

        for (int x : primes) {
            if (x != -1){
                output.add(x);
            }
        }
        return output;
    }


    public static int goldbach(int value, List<Integer> primes) {
        if (value < 3) {
            return 0;
        }
        else {
            for (int i : primes) {
                if (primes.contains(value - i)) {
                    return( 1 + goldbach(value - i - i, primes));
                }
            }
        }
        return -1;
    }
}
