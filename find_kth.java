import java.util.*;

class Main {
    public static int findKthSmallest(List<Integer> A, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        pq.addAll(A.subList(0, k));
        for (int i=k; i< A.size(); i++) {
            if (A.get(i) < pq.peek()) {
                pq.poll();
                pq.add(A.get(i));
            }
        }
        return pq.peek();
    }
    public static void main(String[] args) {
        List<Integer> A = Arrays.asList(7, 4, 6, 3, 9, 1);
        int k = 3;
        System.out.println("K'th smallest element in the array is " +
                                   findKthSmallest(A, k));
    }
}
