import java.lang.reflect.Array;
import java.util.*;

public class RugOptimisation {

    public static void main(String[] args){
        //read in content
        Scanner in = new Scanner(System.in);
        String[] info = in.nextLine().split(" ");
        int size = Integer.parseInt(info[0]);
        int rug = Integer.parseInt(info[1]);

        var room = new ArrayList<String>();
        for (int i = 0; i < size; i++){
            room.add(in.nextLine());
        }
        Map<Integer, Integer> numWays = new HashMap<Integer, Integer>();

        for (int i = 0; i < size - rug + 1; i++){
            for (int j = 0; j < size - rug + 1; j++){
                int num = countDirty(i, j, rug, room);
                if (numWays.containsKey(num)){
                    numWays.replace(num, numWays.get(num) + 1);
                }else {
                    numWays.put(num, 1);
                }
            }
        }

        var output = new ArrayList<Integer>();
        for (int x : numWays.values()){
            output.add(x);
        }

        Collections.sort(output);
        for (int x : output){
            System.out.println(x + " " + numWays.get(x));
        }
    }


    public static int countDirty(int i, int j, int rug, ArrayList<String> room){
        if (rug == 1){
            return 0;
        }
        else {
            return countDirtyDown(i, j, rug, room) + countDirty(i-1, j, rug-1, room);
        }
    }

    public static int countDirtyDown(int i, int j, int rug, ArrayList<String> room){
        if (rug == 0 || j == 0) {
            return 0;
        }
        if (room.get(i).charAt(j) == 'D'){
            return 1 + countDirtyDown(i, j-1, rug-1, room);
        }else {
            return countDirtyDown(i, j-1, rug-1, room);
        }
    }
}
