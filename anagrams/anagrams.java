import java.util.HashMap;
​
class Source {
  public static HashMap<Character, Integer> charCount(String s) {
    // make a hashmap called count
    HashMap<Character, Integer> count = new HashMap<Character, Integer>();
    System.out.print(s);
    for (char c : s.toCharArray()) {// for c in s:
      if (count.get(c) == null) {// if count.get(c) count[c] == null
        count.put(c, 0);// if count[c] is null make it 0
      }
      int current = count.get(c);// get the value 
      count.put(c, current + 1);//increment the value of the key by 1
    }
    System.out.print(count);
    return count;
  }
​
  public static boolean anagrams(String s1, String s2) {
    return charCount(s1).equals(charCount(s2));// if the hashes are equal then we return true or false
  }
​
  public static void run() {
    // this function behaves as `main()` for the 'run' command
    // you may sandbox in this function, but should not remove it
    Source.anagrams("restful", "fluster"); // -> true
  }
}