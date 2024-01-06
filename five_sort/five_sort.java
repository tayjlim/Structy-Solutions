import java.util.List;
import java.util.Collections;
class Source {
  public static List<Integer> fiveSort(List<Integer> array) {
    // todo
    int left = 0;
    int right = array.size()-1;
    
    while (left < right){
      if (array.get(left) != 5){
        left +=1;
      }else if(array.get(right) == 5){
        right -=1;
      }
      else{
        Collections.swap(array,left,right);
      }
    }
    return array;
  }
​
  public static void run() {
    // this function behaves as `main()` for the 'run' command
    // you may sandbox in this function, but should not remove it
  }
}