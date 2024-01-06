import java.util.List;
import java.util.HashMap;
​
class Source {
  public static List<Integer> pairProduct(List<Integer> numbers, int target) {
  HashMap<Integer, Integer> hash = new HashMap<>();
  for (int index = 0; index < numbers.size(); index++){
    // looping through the numbers 
    int number = numbers.get(index); // store numbers[index];
    int answer = target/number;
    if(hash.containsKey(answer)){
      return List.of(hash.get(answer),index);
    }
    hash.put(number,index);
    
  }
    
    
    return null;
  }
​
  public static void run() {
    // this function behaves as `main()` for the 'run' command
    // you may sandbox in this function , but should not remove it
  }
}
​