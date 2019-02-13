// The prime factors of 13195 are 5, 7, 13 and 29.
// 
// What is the largest prime factor of the number 600851475143 ?
// ---------------------------------------------------------------
// Note: 	since the input is so large, I have to use "long" instead 
//			of "int" throughout the code
package Problems1_10;
import java.util.ArrayList;
import java.util.Collections;

public class Problem3 {
	
	// FUNCTION: find the factors of number x
	public static ArrayList<Long> find_factors(long x){
		// Initialize emtpy arraylist
		ArrayList<Long> factors = new ArrayList<Long>(); 
		
		// Go from 1 to sqrt(x)
		for(long n = 1; n < Math.sqrt(x); n++) {
			if(x % n == 0) {				
				factors.add(n);
				factors.add(x/n);
			}
		}
		Collections.sort(factors);
		return factors;
	}
	
	// FUNCTION: determine if x is a prime number
	public static boolean is_prime(long x) {
		if(x >= 2) {
			for(long i = 2; i < x; i++) {
				if((x % i) == 0 ) {
					return false;
				}
			} 
		} else {
			return false;
		}
		return true;
	}
	
	// MAIN
	public static void main(String[] args) {
		// Initialise my output
		ArrayList<Long> factors = new ArrayList<Long>();
		// Compute the factors of 600851475143
		long x = 600851475143L;		
		factors = find_factors(x);
		
		// Find the highest numbers
		long prime = 0;
		for(long f: factors) {
			// If it's a prime, add it to an arraylist
			// Since factors is already sorted, the last one is necessarily the highest prime number
			if(is_prime(f)){
				prime = f;
			}
		}
		// Result
		System.out.println("The max of the prime numbers, also factors of input is:");
		System.out.println(prime);
	}
}
