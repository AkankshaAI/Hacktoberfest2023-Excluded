package DSA_450;
import java.util.*;
public class setTowarrUnion {
    public static void main(String[] args) {
        int []a={1,2,3,4,5};
        int []b={1,2,433,21,5};
        Set<Integer> s=HashSet<>();
        for(int i=0;i<a.length;i++){
        s.add(a[i]);
        }
        for(int i=0;i<b.length;i++){
        s.add(b[i]);
        }
         s.size();
    }
}
