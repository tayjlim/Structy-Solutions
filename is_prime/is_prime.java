class Source {
  public static boolean isPrime(int number) {
    // todo
    if (number < 2) {
      return false;
    }
    //return true or false if a number is a prime number
    
    // a prime number is only divisible by its self and 1 
    
    // nothing else 
    for (int i =2 ; i<=Math.sqrt(number); i+=1){
      if (number %i == 0){
        return false;
      }
    }
    return true ;
  }
​
  public static void run() {
    // this function behaves as `main()` for the 'run' command
    // you may sandbox in this function, but should not remove it
  }
}