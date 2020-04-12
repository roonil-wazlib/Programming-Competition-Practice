import java.util.HashMap;

class Caching {
    public static HashMap<Long, Long> cache = new HashMap<>();

    public static void main(String[] args){

        System.out.println(factorial(10));
        System.out.println(cache);
    }

    public static long factorial(long n) {
        return cache.computeIfAbsent(n, x -> uncached(x));
    }

    private static long uncached(long n) {
        if (n == 0){
            return 1;
        }
        return n * uncached(n-1);
    }
}