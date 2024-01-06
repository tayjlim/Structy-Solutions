import java.util.List;
import java.util.HashMap;
class Source {
  public static List<Integer> pairSum(List<Integer> numbers, int target) {
  HashMap<Integer, Integer> hash = new HashMap<>();
  for (int index = 0; index<numbers.size();index++){
    int num = numbers.get(index); // element in the array
    int answer = target - num;
    if (hash.containsKey(answer)){
      return List.of(hash.get(answer),index);
    }
    //update the hashmap
    hash.put(num, index);
  }
    // todo
    return null;
  }
​
  public static void run() {
    // this function behaves as `main()` for the 'run' command
    // you may sandbox in this function , but should not remove it
  }
}
​